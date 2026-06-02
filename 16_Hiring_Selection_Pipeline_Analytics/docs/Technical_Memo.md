# Technical Memo — Hiring & Selection Pipeline Analytics

This memo documents the analytic approach used in this synthetic hiring pipeline case study.

## What’s included

- Schema and queries: `sql/`
- Synthetic dataset + dictionary: `data/`
- Repro script (SQLite loader + query runner): `analysis/run_analysis.py`
- Public-facing output: `docs/Results_Snapshot.md`

## Adverse impact screen (4/5ths rule)

- Computed by stage, separately for gender and race/ethnicity dimensions.
- Each subgroup is compared to the **maximum** observed pass rate at that stage.
- Flagging indicates “review needed,” not a validation conclusion.

## Privacy / data handling

- No PII or proprietary hiring data is used.
- The generator creates plausible-but-fake candidate pipelines to demonstrate documentation and QA posture.
