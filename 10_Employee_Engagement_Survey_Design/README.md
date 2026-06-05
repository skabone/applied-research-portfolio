# Employee Engagement Pulse Survey — Design & Reporting

Organizations usually detect engagement problems too late — as attrition, after the people are gone. This project builds the instrument that surfaces the signal earlier: a short quarterly survey designed to measure employee engagement reliably enough to trust and quickly enough to act on, grounded in the Utrecht Work Engagement Scale (UWES-15).

Engagement is measured as three distinct dimensions — **Vigor**, **Dedication**, and **Absorption** — so a low score points to *what* is wrong, not just *that* something is. The design covers the full lifecycle: construct definition, item selection, stratified sampling, anonymous administration, scoring, layered reporting, and a pre-specified validation plan (reliability ≥ 0.70 before any number is trusted).

![Quarterly engagement trend by subscale across four waves — the core monitoring view the design is built to produce](docs/figures/quarterly-trend-1.png)

*Above: the headline view leadership would receive each quarter. Tracking Vigor, Dedication, and Absorption separately over four waves makes a dip in any single dimension visible before it compounds into turnover.*

## Project Files

- **[01_Project_Summary.md](./01_Project_Summary.md)** — concise overview of the problem, the design, and what it produces.
- **[02_Project_Report.md](./02_Project_Report.md)** — full PhD-level design specification: theoretical framework, sampling, instrument, scoring, validation plan, and APA-cited methodology.
- **[03_Reporting_Demonstration.ipynb](./03_Reporting_Demonstration.ipynb)** — the scoring and reporting pipeline implemented end-to-end on clearly-labeled synthetic illustrative data ([source](./04_Reporting_Demonstration_Source.py)).

## Note on data

This is a measurement-**design** project — no employees were surveyed. To show how the designed instrument behaves once fielded, the notebook generates a synthetic illustrative dataset matching the instrument's structure (3 subscales × 5 items, 5-point Likert, quarterly waves, department strata) and runs the exact scoring/reporting logic from the specification. All figures are demonstrations, not findings about any organization.

*Originated as graduate coursework in survey design and development (2023).*
