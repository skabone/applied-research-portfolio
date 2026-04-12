# Career Fair Program Analytics (Program Evaluation + Survey Insights)

**Author:** Mintay Misgano, PhD  
**Project Type:** Program evaluation case study (career fair planning + execution + feedback)  
**Tools:** Python/R (analysis), spreadsheet-style ops tracking, markdown reporting

---

## Objective

Demonstrate an end-to-end stakeholder analytics workflow:

- define program success metrics
- summarize registration + attendance signals
- analyze student + employer survey feedback
- translate results into actionable recommendations for the next event cycle

This project shows practical strength in **people analytics**, **program evaluation**, and **stakeholder-facing reporting** (problem framing → analysis → stakeholder-ready findings).

---

## Key Findings

- Student ratings were strongest for employer approachability and overall layout/value.
- Employer ratings were strongest for atmosphere and registration process.
- Several employer items point to opportunities around candidate volume, candidate fit, and event ergonomics.

## Data Note

Raw exports for this project may include contact information (emails/names) and other operational details.

For GitHub publication:

- only **sanitized** or **aggregated** datasets will be included in `data/`
- any potentially identifying information will be removed

## Repository Guide

| Path | Purpose |
|---|---|
| `analysis/` | Supporting scripts that regenerate the public-safe tables |
| `data/` | Sanitized/aggregated datasets used in the public analysis |
| `docs/` | Public-safe results snapshot, leader brief, and metrics definitions |

## Key Deliverables

- `01_Project_Summary.md`
- `02_Project_Report.md`
- `03_Analysis_Notebook.ipynb`
- `docs/Leader_Brief.md`
- `docs/Metrics_Spec.md`
- `docs/Results_Snapshot.md`

## Repro (optional)

On GitHub, start with `03_Analysis_Notebook.ipynb` and `docs/Results_Snapshot.md`. If you have access to the original exports locally, you can regenerate the public tables:

```bash
python3 analysis/build_public_data.py --source-base "/path/to/Career_Fair_Analytics_2023"
```

## Limitations

- The public package is intentionally aggregated, which limits granular diagnostic detail.
- The package is strongest for surfacing next-cycle decisions rather than longitudinal evaluation.
