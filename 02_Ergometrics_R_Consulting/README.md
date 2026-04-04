# Project Bid Accuracy Analysis — NDA Org (Consulting Engagement)

**Type:** Real consulting project (anonymized per NDA)
**Tools:** R, R Markdown, ggplot2, lmtest, nortest, corrplot
**Domain:** Business analytics, consulting operations, organizational effectiveness

## Project Overview

A Pacific Northwest organizational survey and assessment firm — specializing in pre-employment testing for public safety agencies — needed to understand why their project cost estimates frequently diverged from actual invoiced amounts. Estimation errors created competitive risk (overbidding loses contracts) and financial risk (underbidding erodes margins).

This analysis used two years of internal project data (2020–2021, N = 279) to identify which factors most strongly predict the gap between estimated bids and actual invoices. Findings directly informed four operational recommendations adopted by the firm.

> All client names, personnel identifiers, and organizational details have been anonymized per a signed NDA.

## Methods Applied

- Data integration and cleaning across two annual workbooks (572 raw → 279 cleaned observations)
- Feature engineering: created target variable (DV = Invoice − Estimated Bid), calculated net profit, and reporting inconsistency metric
- OLS assumption testing: linearity, normality (Anderson-Darling, Shapiro-Wilk), homoscedasticity (Breusch-Pagan), multicollinearity, independence
- 10 multiple and simple linear regression models tested at p < 0.01 threshold (adjusted for assumption violations)
- Model evaluation: F-statistic, p-value, Adjusted R², MAE, RMSE, MSE

## Key Findings

- **Consultant identity** and **specific client organizations** — not industry sector or position rank — were the primary predictors of estimation error
- Four client organizations showed persistent, statistically significant underestimation (invoiced more than quoted)
- Projects with travel requirements were systematically overestimated
- 32% of projects had no department recorded — itself a significant predictor of overestimation

## Files

| File | Description |
|------|-------------|
| `NDA_Org_ProjectBidAccuracy_Analysis.Rmd` | Full polished R Markdown: EDA, assumption testing, 10 regression models, results |
| `Executive_Brief.md` | 1-page business case for HR/People Analytics leadership audience |
| `NDA_Org_Project_Report.docx` | PhD-quality written report with literature review, methods, results, and APA references |
| `data.csv` | Anonymized project dataset (279 observations × 15 variables) |

## Note on Confidentiality

This project was completed under a Non-Disclosure Agreement. All client organization names, consultant names, and identifying project details have been replaced with generic labels (Client A, Consultant B, etc.). The analytical methodology, data structure, and findings are authentic.

---
*Seattle Pacific University — Programming for Data Analytics: R (ISM 6354) — Winter 2023*
*Mintay Misgano · github.com/skabone/people-analytics-portfolio*
