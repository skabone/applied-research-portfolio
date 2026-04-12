from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
OUT_DATA_DIR = ROOT / "GitHub_Ready" / "data"
OUT_DOCS_DIR = ROOT / "GitHub_Ready" / "docs"

DEFAULT_SOURCE_BASE = (
    ROOT.parent / "GitHub Potential Projects" / "Career_Fair_Analytics_2023"
).resolve()

LIKERT_ORDER = [
    "Strongly disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly agree",
]


def _redact_text(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = re.sub(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}", "[REDACTED_EMAIL]", s, flags=re.I)
    s = re.sub(r"\\b\\d{3}[-.\\s]?\\d{3}[-.\\s]?\\d{4}\\b", "[REDACTED_PHONE]", s)
    return s.strip()


def _save_csv(df: pd.DataFrame, filename: str) -> None:
    OUT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_DATA_DIR / filename, index=False)


def _coerce_bool_like(series: pd.Series) -> pd.Series:
    s = series.astype(str).str.strip().str.lower()
    mapping = {"true": True, "false": False, "yes": True, "no": False, "nan": None, "": None}
    return s.map(mapping).astype("boolean")


def _split_multi(s: str) -> list[str]:
    if not isinstance(s, str) or not s.strip():
        return []
    # Handshake exports commonly use comma-separated lists in a single cell.
    return [p.strip() for p in s.split(",") if p.strip()]


def _summarize_likert(df: pd.DataFrame, question_cols: list[str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for col in question_cols:
        if col not in df.columns:
            continue
        s = df[col].dropna().astype(str).str.strip()
        if s.empty:
            continue
        counts = s.value_counts(dropna=False).reindex(LIKERT_ORDER, fill_value=0)
        n = int(counts.sum())
        score_map = {k: i + 1 for i, k in enumerate(LIKERT_ORDER)}
        mean_score = (s.map(score_map).dropna().mean()) if n else None
        rows.append(
            {
                "question": col.strip(),
                "n": n,
                "strongly_disagree": int(counts["Strongly disagree"]),
                "disagree": int(counts["Disagree"]),
                "neutral": int(counts["Neutral"]),
                "agree": int(counts["Agree"]),
                "strongly_agree": int(counts["Strongly agree"]),
                "agree_or_strongly_agree_pct": float(
                    (counts["Agree"] + counts["Strongly agree"]) / n
                ),
                "mean_score_1_to_5": float(mean_score) if mean_score == mean_score else None,
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["agree_or_strongly_agree_pct", "n"], ascending=[False, False]
    )


def _summarize_yesno(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for col in cols:
        if col not in df.columns:
            continue
        s = df[col].dropna().astype(str).str.strip().str.lower()
        if s.empty:
            continue
        yes = int((s == "yes").sum())
        no = int((s == "no").sum())
        n = yes + no
        if n == 0:
            continue
        rows.append(
            {
                "question": col.strip(),
                "n": n,
                "yes": yes,
                "no": no,
                "yes_pct": float(yes / n),
            }
        )
    return pd.DataFrame(rows).sort_values(["yes_pct", "n"], ascending=[False, False])


def _summarize_single_choice(df: pd.DataFrame, col: str, top_n: int = 20) -> pd.DataFrame:
    if col not in df.columns:
        return pd.DataFrame(columns=[col, "n", "pct"])
    s = df[col].dropna().astype(str).str.strip()
    counts = s.value_counts().head(top_n)
    n = int(counts.sum())
    out = counts.reset_index()
    out.columns = [col, "n"]
    out["pct"] = out["n"] / n if n else 0.0
    return out


def _summarize_multivalue(df: pd.DataFrame, col: str, top_n: int = 30) -> pd.DataFrame:
    if col not in df.columns:
        return pd.DataFrame(columns=["value", "n", "pct"])
    values: list[str] = []
    for v in df[col].dropna().astype(str):
        values.extend(_split_multi(v))
    if not values:
        return pd.DataFrame(columns=["value", "n", "pct"])
    s = pd.Series(values, name="value")
    counts = s.value_counts().head(top_n)
    n = int(counts.sum())
    out = counts.reset_index()
    out.columns = ["value", "n"]
    out["pct"] = out["n"] / n if n else 0.0
    return out


def build_public_tables(source_base: Path) -> dict[str, pd.DataFrame]:
    surveys_dir = source_base / "surveys"
    data_dir = source_base / "data"

    student_path = surveys_dir / "SPU Spring 23 CF Student Survey.csv"
    employer_path = surveys_dir / "SPU Spring 23 CF Employers Survey.csv"
    registration_path = data_dir / "registration_download20230403-1-8r9w6k.csv"

    student = pd.read_csv(student_path)
    employer = pd.read_csv(employer_path)
    reg = pd.read_csv(registration_path, low_memory=False)

    # --- Surveys (aggregate only; do not publish row-level responses) ---
    student_cols = [c for c in student.columns if c.strip().lower() != "timestamp"]
    student_likert_cols = [
        c
        for c in student_cols
        if student[c].astype(str).str.strip().isin(LIKERT_ORDER).any()
    ]
    # Heuristic: yes/no questions tend to start with "Did you"
    student_yesno_cols = [c for c in student_cols if c.strip().lower().startswith("did you")]

    employer_cols = [c for c in employer.columns if c.strip().lower() != "timestamp"]
    employer_likert_cols = [
        c
        for c in employer_cols
        if employer[c].astype(str).str.strip().isin(LIKERT_ORDER).any()
    ]

    out: dict[str, pd.DataFrame] = {}
    out["student_likert_summary"] = _summarize_likert(student, student_likert_cols)
    out["employer_likert_summary"] = _summarize_likert(employer, employer_likert_cols)
    out["student_yesno_summary"] = _summarize_yesno(student, student_yesno_cols)
    out["student_hear_about_summary"] = _summarize_single_choice(student, "How did you hear about the Career Fair")

    # --- Registration / employer participation (aggregate only) ---
    safe_cols = [
        "Career Fair",
        "Employer Industry",
        "Status",
        "Payment Status",
        "Representatives Count",
        "Student Check-ins",
        "Accept All Majors?",
        "Employment Types",
        "Job Types",
        "School Years",
        "Located in US?",
        "Accepts OPT/CPT candidates?",
        "Willing to sponsor candidate?",
    ]
    reg_slim = reg[[c for c in safe_cols if c in reg.columns]].copy()

    for numeric_col in ["Representatives Count", "Student Check-ins"]:
        if numeric_col in reg_slim.columns:
            reg_slim[numeric_col] = pd.to_numeric(reg_slim[numeric_col], errors="coerce")

    for bool_col in [
        "Accept All Majors?",
        "Located in US?",
        "Accepts OPT/CPT candidates?",
        "Willing to sponsor candidate?",
    ]:
        if bool_col in reg_slim.columns:
            reg_slim[bool_col] = _coerce_bool_like(reg_slim[bool_col])

    if "Employer Industry" in reg_slim.columns:
        vc = (
            reg_slim["Employer Industry"]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .value_counts()
        )
        out["employers_by_industry"] = vc.rename_axis("employer_industry").reset_index(name="n_employers")

    if "Status" in reg_slim.columns:
        vc = (
            reg_slim["Status"]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .value_counts()
        )
        out["registration_status_counts"] = vc.rename_axis("status").reset_index(name="n")

    for multi_col, out_name in [
        ("Employment Types", "employment_types_counts"),
        ("Job Types", "job_types_counts"),
        ("School Years", "target_school_year_counts"),
    ]:
        out[out_name] = _summarize_multivalue(reg_slim, multi_col)

    if "Career Fair" in reg_slim.columns:
        # one-row, public-safe totals for the event
        totals = {
            "career_fair": reg_slim["Career Fair"].dropna().astype(str).unique()[:1].tolist(),
            "n_employer_registrations_rows": int(len(reg_slim)),
            "total_representatives": float(reg_slim.get("Representatives Count", pd.Series(dtype=float)).sum(skipna=True)),
            "total_student_checkins": float(reg_slim.get("Student Check-ins", pd.Series(dtype=float)).sum(skipna=True)),
        }
        out["event_totals"] = pd.DataFrame(
            [
                {
                    "career_fair": totals["career_fair"][0] if totals["career_fair"] else "",
                    "n_employer_registrations_rows": totals["n_employer_registrations_rows"],
                    "total_representatives": int(totals["total_representatives"]),
                    "total_student_checkins": int(totals["total_student_checkins"]),
                }
            ]
        )

    return out


def write_results_snapshot(tables: dict[str, pd.DataFrame]) -> None:
    OUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)

    student_top = tables.get("student_likert_summary", pd.DataFrame()).head(8)
    employer_top = tables.get("employer_likert_summary", pd.DataFrame()).head(8)
    totals = tables.get("event_totals", pd.DataFrame())
    industry = tables.get("employers_by_industry", pd.DataFrame()).head(12)

    lines: list[str] = [
        "# Career Fair Program Analytics — Results Snapshot (Public-Safe, First Pass)",
        "",
        "This snapshot is generated from **aggregated** survey and registration tables (no row-level survey responses and no contact fields).",
        "",
    ]

    if not totals.empty:
        lines += ["## Event Totals (from registration export)", "", totals.to_markdown(index=False), ""]

    if not industry.empty:
        lines += ["## Employers by Industry (top)", "", industry.to_markdown(index=False), ""]

    if not student_top.empty:
        lines += [
            "## Student Survey — Top Items by % Agree/Strongly Agree",
            "",
            student_top[["question", "n", "agree_or_strongly_agree_pct", "mean_score_1_to_5"]].to_markdown(
                index=False
            ),
            "",
        ]

    if not employer_top.empty:
        lines += [
            "## Employer Survey — Top Items by % Agree/Strongly Agree",
            "",
            employer_top[["question", "n", "agree_or_strongly_agree_pct", "mean_score_1_to_5"]].to_markdown(
                index=False
            ),
            "",
        ]

    lines += [
        "## Limitations",
        "",
        "- Survey results are descriptive and represent only respondents.",
        "- Registration export fields vary across events; tables are built from available columns only.",
        "- Open-ended feedback was intentionally excluded from the public dataset in this first pass.",
        "",
    ]

    (OUT_DOCS_DIR / "Results_Snapshot.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build aggregated, public-safe tables for the Career Fair Analytics project."
    )
    parser.add_argument(
        "--source-base",
        type=Path,
        default=DEFAULT_SOURCE_BASE,
        help="Path to the private source folder (exports + surveys).",
    )
    args = parser.parse_args()

    tables = build_public_tables(args.source_base.resolve())

    _save_csv(tables["student_likert_summary"], "student_likert_summary.csv")
    _save_csv(tables["employer_likert_summary"], "employer_likert_summary.csv")
    _save_csv(tables["student_yesno_summary"], "student_yesno_summary.csv")
    _save_csv(tables["student_hear_about_summary"], "student_hear_about_summary.csv")

    for k, out_name in [
        ("event_totals", "event_totals.csv"),
        ("employers_by_industry", "employers_by_industry.csv"),
        ("registration_status_counts", "registration_status_counts.csv"),
        ("employment_types_counts", "employment_types_counts.csv"),
        ("job_types_counts", "job_types_counts.csv"),
        ("target_school_year_counts", "target_school_year_counts.csv"),
    ]:
        if k in tables and not tables[k].empty:
            _save_csv(tables[k], out_name)

    write_results_snapshot(tables)

    print("Wrote public-safe datasets to:", OUT_DATA_DIR)
    print("Wrote snapshot to:", OUT_DOCS_DIR / "Results_Snapshot.md")


if __name__ == "__main__":
    main()
