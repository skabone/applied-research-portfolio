# Consulting Bid Accuracy Analysis

**Author:** Mintay Misgano, PhD  
**Engagement Type:** Real consulting project completed under NDA — data anonymized for public presentation  
**Tools:** R, RStudio, dplyr, ggplot2, OLS regression  
**Dataset:** 279 anonymized project records, FY2020–2021

---

## Overview

A regional assessment services firm had two years of internal project records and a concrete operational problem: project bids were not consistently landing close to final invoiced amounts. Some projects came in significantly over estimate, others under, and the firm had no systematic way to identify what was driving the gap. This project was completed as part of a graduate consulting engagement to answer that question.

The analysis examines project-level, personnel, and client-level factors across 279 records using ten OLS regression model specifications, compares their explanatory value, and translates the findings into actionable process recommendations. All organization, client, and personnel identifiers have been anonymized for public presentation.

---

## Key Findings

- Consultant identity and specific client accounts explained far more estimation variance than broad project categories like industry sector or position rank.
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
| `04_Source_Report.Rmd` | R Markdown source file for the report |
| `data.csv` | Anonymized project records used in the analysis |
| `docs/Results_Snapshot.md` | Quick-reference model results table |

---

## Confidentiality Note

This project was completed under a Non-Disclosure Agreement. The client organization is not named. All personnel identifiers, client organization names, invoice numbers, and operationally identifying details have been removed or replaced with anonymized labels. The published dataset reflects the analytical structure of the original data without exposing any protected records.
