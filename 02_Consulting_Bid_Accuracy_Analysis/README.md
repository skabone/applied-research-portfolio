# Consulting Bid Accuracy Analysis

- **Author:** Mintay Misgano, PhD
- **Engagement Type:** Real consulting project completed under NDA; public dataset is synthetic and anonymized for presentation
- **Tools:** R, RStudio, dplyr, ggplot2, OLS regression
- **Dataset:** 279 synthetic public records modeled from the protected project structure, FY2020–2021

---

## Overview

A regional assessment services firm had two years of internal project records and a concrete operational problem: project bids were not consistently landing close to final invoiced amounts. Some projects came in significantly over estimate, others under, and the firm had no systematic way to identify what was driving the gap. This project was completed as part of a graduate consulting engagement to answer that question.

The analysis examines project-level, personnel, and client-level factors across 279 records using eight OLS regression model specifications, compares their explanatory value, and translates the findings into actionable process recommendations. The engagement was real; the public data file is synthetic and anonymized so the analytical structure can be reviewed without exposing protected records.

![Estimated bill compared with final invoice](docs/figures/eda-bill-vs-invoice-1.png)

The diagonal line marks perfect estimate accuracy. Points above the line were underestimated, and points below it were overestimated; the spread around that line is the operational problem this project investigates.

---

## Key Findings

- Consultant identity and specific client accounts explained more estimation variance than broad categories like service area.
- The estimation problem appeared relational rather than structural — a signal that targeted review by account and project lead is likely more useful than an across-the-board pricing overhaul.
- Travel estimates showed a consistent pattern of overestimation, pointing to a specific calibration opportunity.
- Missing department or intake data co-occurred with worse bid accuracy, suggesting that process discipline and data quality are connected.
- Four of five OLS assumptions were violated; results are interpreted conservatively (p < .01) and framed as exploratory guidance rather than definitive findings.

---

## Read This Project

| File | Purpose |
|---|---|
| `01_Project_Summary.md` | Short narrative overview: problem, approach, and takeaways |
| `02_Project_Report.md` | Full methods and results write-up |
| `03_Analysis_Workflow.md` | GitHub-viewable analysis workflow with figures |
| `04_Source_Report.Rmd` | R Markdown source file for the report |
| `data.csv` | Synthetic, anonymized public dataset used in the analysis |
| `docs/Results_Snapshot.md` | Quick-reference model results table |
| `docs/figures/` | Stable figure exports referenced by the README, summary, and report |

---

## Confidentiality Note

This project was completed under a Non-Disclosure Agreement. The client organization is not named. All personnel identifiers, client organization names, invoice numbers, and operationally identifying details have been removed or replaced with anonymized labels. The published dataset is synthetic and generalized from the protected workflow so the project remains reviewable without exposing any protected records.
