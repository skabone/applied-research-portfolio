# Hiring & Selection Pipeline — Results Snapshot (Synthetic Data)

This snapshot is generated from the synthetic datasets in `data/` and SQL queries in `sql/`.

## Funnel counts by stage

| stage_order | stage | candidates |
|---|---|---|
| 1 | applied | 5000 |
| 2 | screen | 5000 |
| 3 | assessment | 2363 |
| 4 | interview | 1070 |
| 5 | offer | 678 |
| 6 | hire | 434 |

## Adverse impact screen (4/5ths rule) — flagged rows

| dimension | stage | group_name | n_total | n_passed | pass_rate | impact_ratio | flagged_under_4_5ths |
|---|---|---|---|---|---|---|---|
| gender_group | hire | Nonbinary/Other | 17 | 6 | 0.3529 | 0.6265 | 1 |
| race_ethnicity_group | assessment | Black | 174 | 62 | 0.3563 | 0.7047 | 1 |
| race_ethnicity_group | hire | Black | 25 | 10 | 0.4 | 0.6947 | 1 |
| race_ethnicity_group | hire | Two+ | 19 | 7 | 0.3684 | 0.6399 | 1 |

## Notes / limitations

- This is a **screening** workflow for interpretation and documentation practice, not a legal conclusion.
- The synthetic generator intentionally introduces small subgroup shifts to demonstrate how to detect and discuss potential impact.
- In real work, you would add minimum-n thresholds, job-relatedness evidence, and a validation plan before changing selection decisions.
