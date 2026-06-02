# Hiring & Selection Pipeline Analytics — Project Report (First Pass)

## 1) Questions this workflow supports

1. Where do candidates drop out of the funnel (stage counts)?
2. Do pass rates differ meaningfully by subgroup at each stage?
3. Do any subgroup differences trigger a preliminary 4/5ths adverse impact flag?

## 2) Data model

Tables:

- `candidates`: requisition + demographic grouping fields (synthetic)
- `pipeline_events`: stage events with pass/fail/withdrawn outcomes
- `assessments`: a simple work-sample-like score and pass flag
- `outcomes`: post-hire early outcomes (retention and early performance), for demonstration only

## 3) Methods

- Funnel counts: distinct candidates per stage.
- Subgroup pass rates: pass / total at each stage by gender and race/ethnicity group.
- Adverse impact screen: compare each subgroup’s pass rate to the maximum pass rate within that stage (4/5ths rule threshold).

## 4) Governance + interpretation notes

- This screen is **not** a legal conclusion or validation study.
- Any flagged stage should trigger deeper review: minimum-n rules, job-relatedness evidence, alternative cut scores, and validation planning.

## 5) Outputs

- SQL queries in `sql/`
- Public-facing snapshot in `docs/Results_Snapshot.md`
- Repro script in `analysis/run_analysis.py` (writes tables to `analysis/outputs/`)

