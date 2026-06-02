from __future__ import annotations

import csv
import datetime as dt
import math
import random
import uuid
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    requisition_id: str
    job_family: str
    location: str
    source_channel: str
    application_date: str
    gender_group: str
    race_ethnicity_group: str


def _iso_date(d: dt.date) -> str:
    return d.isoformat()


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def _sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def generate(seed: int = 7, n_candidates: int = 5000) -> dict[str, list[dict[str, object]]]:
    rng = random.Random(seed)

    job_families = ["Engineering", "Operations", "Corporate", "Customer"]
    locations = ["Seattle", "Remote", "Other"]
    source_channels = ["Referral", "Job board", "Campus", "Agency"]

    gender_groups = ["Women", "Men", "Nonbinary/Other", "Unknown"]
    gender_probs = [0.40, 0.50, 0.03, 0.07]

    race_groups = [
        "Asian",
        "Black",
        "Hispanic/Latino",
        "White",
        "Two+",
        "Unknown",
    ]
    race_probs = [0.16, 0.07, 0.10, 0.55, 0.05, 0.07]

    start_date = dt.date(2025, 1, 1)
    end_date = dt.date(2025, 12, 31)
    date_span = (end_date - start_date).days

    candidates: list[Candidate] = []
    assessments: list[dict[str, object]] = []
    pipeline_events: list[dict[str, object]] = []
    outcomes: list[dict[str, object]] = []

    for i in range(n_candidates):
        candidate_id = f"C{i+1:05d}"
        requisition_id = f"R{rng.randint(1000, 1999)}"
        job_family = rng.choice(job_families)
        location = rng.choice(locations)
        source_channel = rng.choice(source_channels)

        application_date = _iso_date(start_date + dt.timedelta(days=rng.randint(0, date_span)))

        gender_group = rng.choices(gender_groups, weights=gender_probs, k=1)[0]
        race_group = rng.choices(race_groups, weights=race_probs, k=1)[0]

        candidates.append(
            Candidate(
                candidate_id=candidate_id,
                requisition_id=requisition_id,
                job_family=job_family,
                location=location,
                source_channel=source_channel,
                application_date=application_date,
                gender_group=gender_group,
                race_ethnicity_group=race_group,
            )
        )

        # latent ability proxy (synthetic)
        ability = rng.gauss(0.0, 1.0)
        referral_boost = 0.25 if source_channel == "Referral" else 0.0
        noise = rng.gauss(0.0, 0.35)

        # screening probability (synthetic)
        screen_p = _sigmoid(-0.2 + 0.8 * ability + referral_boost + noise)
        screened_in = rng.random() < screen_p

        # pipeline: applied always exists
        pipeline_events.append(
            {
                "event_id": str(uuid.uuid4()),
                "candidate_id": candidate_id,
                "stage": "applied",
                "stage_date": application_date,
                "stage_outcome": "pass",
            }
        )

        pipeline_events.append(
            {
                "event_id": str(uuid.uuid4()),
                "candidate_id": candidate_id,
                "stage": "screen",
                "stage_date": application_date,
                "stage_outcome": "pass" if screened_in else "fail",
            }
        )

        if not screened_in:
            continue

        # assessment: cognitive-like score with minor group shift to create a fairness-screen example
        group_shift = 0.0
        if race_group in {"Black", "Hispanic/Latino"}:
            group_shift = -0.15
        if gender_group == "Women":
            group_shift += 0.05

        raw_score = 50.0 + 10.0 * (ability + group_shift) + rng.gauss(0.0, 6.0)
        raw_score = _clamp(raw_score, 0.0, 100.0)

        standard_score = (raw_score - 50.0) / 10.0
        passed_assessment = raw_score >= 55.0

        assessment_date = _iso_date(dt.date.fromisoformat(application_date) + dt.timedelta(days=rng.randint(1, 14)))

        assessments.append(
            {
                "assessment_id": str(uuid.uuid4()),
                "candidate_id": candidate_id,
                "assessment_type": "work_sample",
                "assessment_date": assessment_date,
                "raw_score": round(raw_score, 2),
                "standard_score": round(standard_score, 3),
                "passed_flag": 1 if passed_assessment else 0,
            }
        )

        pipeline_events.append(
            {
                "event_id": str(uuid.uuid4()),
                "candidate_id": candidate_id,
                "stage": "assessment",
                "stage_date": assessment_date,
                "stage_outcome": "pass" if passed_assessment else "fail",
            }
        )

        if not passed_assessment:
            continue

        # interview stage (synthetic)
        interview_p = _sigmoid(-0.1 + 0.7 * ability + rng.gauss(0.0, 0.25))
        passed_interview = rng.random() < interview_p
        interview_date = _iso_date(dt.date.fromisoformat(assessment_date) + dt.timedelta(days=rng.randint(3, 21)))

        pipeline_events.append(
            {
                "event_id": str(uuid.uuid4()),
                "candidate_id": candidate_id,
                "stage": "interview",
                "stage_date": interview_date,
                "stage_outcome": "pass" if passed_interview else "fail",
            }
        )

        if not passed_interview:
            continue

        # offer stage
        offer_p = _sigmoid(-0.05 + 0.6 * ability + rng.gauss(0.0, 0.2))
        got_offer = rng.random() < offer_p
        offer_date = _iso_date(dt.date.fromisoformat(interview_date) + dt.timedelta(days=rng.randint(2, 14)))

        pipeline_events.append(
            {
                "event_id": str(uuid.uuid4()),
                "candidate_id": candidate_id,
                "stage": "offer",
                "stage_date": offer_date,
                "stage_outcome": "pass" if got_offer else "fail",
            }
        )

        if not got_offer:
            continue

        # hire stage
        accept_p = _sigmoid(0.2 + (0.15 if source_channel == "Referral" else 0.0) + rng.gauss(0.0, 0.25))
        hired = rng.random() < accept_p
        hire_date = _iso_date(dt.date.fromisoformat(offer_date) + dt.timedelta(days=rng.randint(7, 30)))

        pipeline_events.append(
            {
                "event_id": str(uuid.uuid4()),
                "candidate_id": candidate_id,
                "stage": "hire",
                "stage_date": hire_date,
                "stage_outcome": "pass" if hired else "withdrawn",
            }
        )

        if not hired:
            continue

        # outcomes for hires only
        retained_p = _sigmoid(0.6 + 0.4 * ability + rng.gauss(0.0, 0.35))
        retained = rng.random() < retained_p
        perf = _clamp(3.2 + 0.55 * ability + rng.gauss(0.0, 0.6), 1.0, 5.0)

        outcomes.append(
            {
                "candidate_id": candidate_id,
                "month3_retained_flag": 1 if retained else 0,
                "early_performance_rating": round(perf, 2),
            }
        )

    return {
        "candidates": [c.__dict__ for c in candidates],
        "assessments": assessments,
        "pipeline_events": pipeline_events,
        "outcomes": outcomes,
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path.name}")
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    base = Path(__file__).resolve().parent
    out_dir = base
    data = generate(seed=7, n_candidates=5000)

    _write_csv(out_dir / "candidates.csv", data["candidates"])
    _write_csv(out_dir / "assessments.csv", data["assessments"])
    _write_csv(out_dir / "pipeline_events.csv", data["pipeline_events"])
    _write_csv(out_dir / "outcomes.csv", data["outcomes"])

    print("Wrote synthetic data files to:", out_dir)


if __name__ == "__main__":
    main()

