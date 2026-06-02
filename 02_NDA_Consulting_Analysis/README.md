# Public-Safe Consulting Bid Accuracy Analysis

**Author:** Mintay Misgano, PhD
**Project Type:** Consulting analytics case study using synthetic public data
**Tools:** R, dplyr, ggplot2, OLS regression

---

## Overview

This project demonstrates how a consulting operations question can be translated into a structured analytics workflow: which project, client, staffing, and process factors are associated with the gap between estimated bids and final invoice amounts?

The public portfolio version uses a fully synthetic dataset that preserves the analytical structure of a consulting bid-accuracy problem without exposing real client records, personnel names, customer IDs, invoice numbers, dates, contact fields, or operational notes.

---

## Key Findings From The Synthetic Demo

- Consultant and client identifiers are useful diagnostic grouping variables when bid variance is concentrated in repeated patterns.
- Project type and department ownership can explain some discrepancy, but model interpretation should stay cautious.
- Travel and shipping flags are operational variables worth checking because they affect cost estimation assumptions.
- Missing or unlisted ownership fields can be treated as process-quality signals rather than ignored as simple blanks.
- The best use of this workflow is targeted review and calibration, not automated pricing decisions.

---

## Read This Project

- Start here for the project overview and file map.
- Read `NDA_Organization_Project_Summary.md` for the short consulting-case narrative.
- Read `NDA_Organization_Project_Report.md` for methods, results, and limitations in full.
- Use `NDA_Organization_Project_Report.Rmd` as the source file for the long-form report.

---

## Project Files

| File | Purpose |
|---|---|
| `NDA_Organization_Project_Summary.md` | Short narrative summary of the project and what it demonstrates |
| `NDA_Organization_Project_Report.md` | Full public-facing report |
| `NDA_Organization_Project_Report.Rmd` | R Markdown source file for the report |
| `data.csv` | Synthetic public dataset used in the analysis |

---

## Data And Confidentiality Note

No protected client data is published in this project. The dataset is synthetic and was generated for portfolio demonstration only. It does not contain real organization names, personnel names, client names, contacts, invoice numbers, customer IDs, exact dates, or original row-level records.
