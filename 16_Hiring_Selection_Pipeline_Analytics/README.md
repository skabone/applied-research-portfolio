# Hiring & Selection Pipeline Analytics (SQL + Validation + Adverse Impact)

**Author:** Mintay Misgano, PhD  
**Project Type:** Portfolio case study using **synthetic** candidate and assessment data  
**Tools:** SQL + Python/R (analysis), markdown reporting

---

## Objective

Demonstrate an end-to-end hiring/selection analytics workflow:

1) business question → 2) data model → 3) SQL extraction → 4) statistical analysis → 5) decision-ready reporting

This project is designed to show crossover strength across **people analytics**, **talent assessment**, and **selection-system governance**, including **adverse impact** checks and documentation discipline.

---

## Key Findings

- SQL-first funnel and subgroup analytics show how selection process metrics can be structured for review.
- The synthetic run illustrates a full pipeline of 5,000 applied to 434 hired.
- Example 4/5ths rule flags appear at select stages to demonstrate review posture, not to imply an operational conclusion.
- The decision posture is explicitly conservative: flags trigger deeper review, minimum-n checks, and job-relatedness evidence gathering.

---

## Repository Guide

| Path | Purpose |
|---|---|
| `sql/` | Schema + queries (funnel metrics, subgroup selection ratios, adverse impact screens) |
| `analysis/` | Supporting scripts that regenerate the public outputs |
| `data/` | Synthetic dataset + data dictionary (no real candidate data) |
| `docs/` | Leader brief, technical memo, and governance notes |

## Key Deliverables

- `01_Project_Summary.md`
- `02_Project_Report.md`
- `03_Analysis_Notebook.ipynb`
- `docs/Leader_Brief.md`
- `docs/Metrics_Spec.md`
- `docs/AIERS_Governance_Note.md`
- `docs/Technical_Memo.md`
- `docs/Results_Snapshot.md` (generated)

## Repro

On GitHub, start with `03_Analysis_Notebook.ipynb` and `docs/Results_Snapshot.md`. To rerun the workflow locally:

```bash
python3 analysis/run_analysis.py
```

## Data Note

All datasets in `data/` are **synthetic** and created for portfolio demonstration. This project does **not** use proprietary hiring data or any organization’s real selection outcomes.

## Limitations

- The package is intentionally synthetic, so the main value is workflow and governance structure rather than empirical generalization.
- Adverse impact flags shown here are review triggers, not stand-alone decision rules.
