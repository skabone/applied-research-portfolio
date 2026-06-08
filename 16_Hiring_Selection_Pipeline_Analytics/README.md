# Hiring & Selection Pipeline Analytics

Every hiring pipeline is a series of gates that remove candidates, and two questions follow from that: where does the process lose the most people, and do different demographic groups clear those gates at similar rates? This project builds the full workflow to answer both — a relational schema, SQL funnel and subgroup metrics, and an adverse-impact (4/5ths rule) fairness screen — on a synthetic candidate pipeline.

![The 4/5ths rule raised four flags; adding 95% confidence intervals shows only the assessment-stage gap for Black candidates (red, p = 0.020) is distinguishable from parity — the other three rest on samples under 30.](docs/figures/impact_ratio_ci.png)

## What it found

Of 5,000 applicants, 434 are hired (8.7% yield), and two early gates — assessment (47% pass-through) and interview (45%) — do almost all the filtering. The fairness screen points at the same place. The 4/5ths rule raised four flags, but pairing each with a two-proportion z-test and a confidence interval shows that only one holds up: at the **assessment** stage, Black candidates pass at 35.6% versus 50.6% for the top group — an impact ratio of **0.70**, 95% CI [0.53, 0.94], *p* = 0.020, the only flag whose interval excludes parity. It also sits on the heaviest-filtering gate, making it the clear priority. The three hire-stage flags rest on fewer than 30 candidates, span parity, and are logged as provisional.

## Where to go

- **[`01_Project_Summary.md`](01_Project_Summary.md)** — findings-first overview, plain language, ~3-minute read.
- **[`02_Project_Report.md`](02_Project_Report.md)** — full method and metric definitions, the complete adverse-impact screen, figure walkthroughs, and references.
- **[`03_Analysis_Notebook.ipynb`](03_Analysis_Notebook.ipynb)** — the executed, narrated workflow.

## Repository guide

| Path | Purpose |
|---|---|
| `sql/` | Schema and queries: funnel metrics, subgroup selection ratios, adverse-impact screen |
| `analysis/` | `run_analysis.py` (SQLite loader + query runner), `make_figures.py` (figures), and `inferential_tests.py` (z-tests + impact-ratio CIs) |
| `data/` | Synthetic dataset, generator, and data dictionary |
| `docs/` | Figures, generated results snapshot, leader brief, technical memo, metrics spec, governance note |

## Reproduce

```bash
python3 analysis/run_analysis.py       # writes analysis/outputs/ and docs/Results_Snapshot.md
python3 analysis/make_figures.py       # writes the funnel, subgroup, and adverse-impact figures to docs/figures/
python3 analysis/inferential_tests.py  # writes impact_inference.csv and the confidence-interval figure
```

## Data note

All data in `data/` is **synthetic**, generated with a fixed seed for this case study. The project uses no proprietary hiring data and no organization's real selection outcomes. The demographic fields exist only to demonstrate fairness-screening logic.

## Scope note

The 4/5ths screen is a review trigger, not a legal conclusion or a validation study. A flag means a stage warrants deeper review — job-relatedness evidence, cut-score sensitivity, and minimum-sample guardrails — as detailed in the report.
