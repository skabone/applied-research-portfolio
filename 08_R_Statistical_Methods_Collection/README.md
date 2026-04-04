# Project 08 — R Statistical Methods Showcase

**5-method statistical cascade with survival analysis highlight** | From ANOVA to Cox PH regression | R, survival, ggplot2

---

## Overview

A unified R Markdown showcase demonstrating five statistical modeling methods applied to a common time-to-event dataset (lung disease patient survival, N=228). The dataset is structurally equivalent to employee tenure/attrition data — making every analysis directly applicable to workforce research. Survival analysis (Kaplan-Meier + Cox PH) is highlighted as a rare and high-value capability in the people analytics toolkit.

---

## Methods Demonstrated

| # | Method | Output | PA Equivalent |
|:--|:-------|:-------|:--------------|
| 1 | EDA + descriptives | Group means, distributions | HR dashboard metrics |
| 2 | t-Test + one-way ANOVA (Tukey HSD) | Group differences in survival time | Compensation equity by group |
| 3 | Linear Regression (OLS) | R², coefficients, diagnostic plots | Predict engagement score from predictors |
| 4 | Logistic Regression | Odds ratios with 95% CIs | Attrition within 90 days (binary) |
| **5** | **Survival Analysis (KM + Cox PH)** | **KM curves, log-rank test, hazard ratios, forest plot** | **Time-to-departure modeling** |

---

## Why Survival Analysis?

Standard logistic regression treats "still employed" as missing data. Survival analysis treats it as a **censored observation** — using the full tenure-to-date rather than discarding it. This produces:

- Less biased estimates (no information wasted)
- Time-varying hazard curves (when is risk highest?)
- Hazard ratios (how much does each predictor shift departure risk?)
- KM curves (visual tenure survival by subgroup, with log-rank p-values)

---

## Key Results

- Female patients: significantly longer survival (log-rank p < .05); KM curves separate early and persist
- ECOG performance (0=best, 3=worst): strongest independent predictor in Cox model; HR > 1.5 per unit increase
- Cox concordance (C-index) ≈ .64; proportional hazards assumption tested via Schoenfeld residuals
- Odds ratios (logistic) and hazard ratios (Cox) directionally consistent — Cox provides fuller picture by incorporating censored observations

---

## Files

| File | Description |
|:-----|:------------|
| `R_Statistical_Methods_Showcase.Rmd` | Full Rmd — EDA, t-test, ANOVA, OLS, logistic, KM, Cox PH; knits to GitHub-renderable `.md` |
| `Executive_Brief.md` | 1-page practitioner summary with PA transfer |
| `README.md` | This file |

**Note:** Data file (`lung_disease.csv`) is in `../Week 6 - Survival Analysis .../`. Script uses relative path.

---

## Tools

- **Language:** R
- **Libraries:** `survival`, `survminer` (KM plots, forest plots), `car` (Levene's test), `broom` (tidy model output), `ggplot2`, `tidyverse`
- **Methods:** Welch's t-test, one-way ANOVA, Tukey HSD, OLS, binary logistic regression, Kaplan-Meier, log-rank test, Cox proportional hazards, Schoenfeld residuals

---

*Part of the [People Analytics Portfolio](../README.md) | Analyst: Mintay Misgano | Course: Programming for Data Analytics: R (ISM 6354), SPU (Winter 2023)*
