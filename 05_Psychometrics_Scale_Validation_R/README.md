# Psychometric Scale Validation

**Author:** Mintay Misgano, PhD  
**Instrument:** Perceptions of the LGBTQ College Campus Climate Scale (Szymanski & Bissonette, 2020)  
**Tools:** R, psych, tidyverse, MASS

---

## Overview

This project demonstrates a psychometric scale-validation workflow using a published two-factor instrument and simulated item-level data derived from reported parameters. The analysis focuses on whether the scale is best interpreted as a single total score or as two distinct subscales: College Response and Stigma.

Completed as graduate psychometrics coursework, the project is intended to show measurement-focused analytical skill, including reliability analysis, item analysis, and exploratory factor analysis.

Because the item-level data are simulated from published parameters rather than collected directly, the project should be read as a transparent validation demonstration rather than as a new empirical study.

---

## Key Findings

- The total six-item scale showed weaker internal consistency than the two subscales.
- Both subscales produced acceptable reliability estimates (α = .79 each).
- Items showed strong within-subscale relationships and low cross-subscale relationships.
- PCA and PAF recovered the same two-factor structure.
- Parallel analysis supported retention of two factors rather than one.

---

## Read This Project

- Start here for the project overview and file map
- Read `Psychometrics_Project_Summary.md` for the short narrative interpretation
- Read `Psychometrics_Project_Report.md` for methods, results, and limitations in full
- Use `Psychometrics_Project_Report.Rmd` as the source file for the long-form report

---

## Project Files

| File | Purpose |
|---|---|
| `Psychometrics_Project_Summary.md` | Short narrative summary of the project and what it demonstrates |
| `Psychometrics_Project_Report.md` | Full project report with methods, results, and limitations |
| `Psychometrics_Project_Report.Rmd` | R Markdown source file for the report |

---

## Data Note

The project uses simulated item-level data generated from published loadings, means, and sample size information. This preserves transparency and reproducibility while avoiding use of proprietary raw data.
