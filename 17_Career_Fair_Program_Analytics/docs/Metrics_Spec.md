# Metrics Spec

## Purpose

Define the public-safe program metrics used in this career fair package.

## Core metrics

| Metric | Definition | Grain | Why it matters |
|---|---|---|---|
| `total_representatives` | Sum of employer representatives across registrations | Event | Approximates employer-side staffing |
| `total_student_checkins` | Count of student event check-ins | Event | Core turnout indicator |
| `agree_or_strongly_agree_pct` | Share of respondents selecting favorable response options | Survey item | Simple stakeholder-friendly experience metric |
| `mean_score_1_to_5` | Average Likert score for an item | Survey item | Complements favorable-rate interpretation |
| `n_employers_by_industry` | Count of employer registrations in each industry category | Industry | Indicates market mix and outreach breadth |

## Guardrails

- Public package uses aggregated tables only.
- Survey metrics are descriptive of respondents, not all attendees.
- Event-to-event comparisons should use the same field definitions and survey wording.

