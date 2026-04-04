# R Statistical Methods Showcase — Executive Brief
**Domain:** Statistical Modeling & Survival Analysis | **Analyst:** Mintay Misgano | **Year:** 2023

---

## The Business Problem

Employee retention is one of the most costly and consequential challenges in people management. Yet most organizations measure it poorly — counting attrition rates as snapshots, failing to account for tenure patterns, and ignoring the time-dependent nature of departure risk. A 20% attrition rate tells you nothing about whether people leave in month 3 or year 3, which makes intervention design guesswork. This project demonstrates the statistical toolkit required to model attrition properly: from foundational hypothesis testing and regression through survival analysis — the gold-standard method for time-to-event workforce data. Applied to lung disease patient survival data (a structural twin of employee tenure/attrition data), the showcase covers the complete arc from descriptive inference to Cox proportional hazards regression.

---

## Approach

- Applied a complete statistical modeling cascade — EDA → hypothesis testing (t-test, ANOVA) → linear regression (OLS with diagnostics) → logistic regression (odds ratios) → survival analysis (Kaplan-Meier + Cox PH) — to a 228-observation time-to-event dataset
- Demonstrated the full survival analysis pipeline: Kaplan-Meier curves stratified by key predictors, log-rank test for group differences, Cox proportional hazards regression with hazard ratios and 95% CIs, and proportional hazards assumption testing (Schoenfeld residuals)
- Every analysis includes an explicit **people analytics parallel** — mapping patient-level variables (ECOG performance, Karnofsky physician rating) to workforce equivalents (engagement score, manager rating)
- **Tools:** R, survival, survminer, car, broom, ggplot2

---

## Key Findings

- **Female patients show significantly longer survival than males (log-rank p < .05)** — the KM curves diverge early and maintain separation throughout the observation period, suggesting a sex-based differential in disease trajectory with direct analogs in workforce gender equity analysis
- **ECOG performance score is the strongest predictor of both survival time and early event hazard** — patients with higher (worse) ECOG scores die sooner, with HR consistently above 1.5 in the Cox model; in workforce terms, this maps to the finding that declining engagement scores predict attrition before traditional performance flags appear
- **Cox model concordance (C-index) ≈ .64** — moderate discriminative ability from a parsimonious set of clinical predictors, consistent with the typical range of predictive models built from administrative HR data (engagement surveys, HRIS records) without behavioral or attitudinal measures
- **Survival analysis outperforms logistic regression for tenure modeling** — by accounting for censored observations (employees still employed at data extraction), Cox regression uses all available information rather than discarding partial tenure records, producing less biased and more complete hazard estimates

---

## Recommendations

1. **Replace attrition rate tracking with survival analysis.** Quarterly attrition snapshots conceal the timing and shape of departure risk. KM curves reveal when in the employee lifecycle retention risk peaks — enabling targeted onboarding interventions (month 3), career development conversations (year 2), and competitive compensation reviews (post-performance cycle).
2. **Apply Cox regression to identify the independent predictors of early attrition.** Controlling for tenure cohort, role, and demographics, which predictors — engagement score, manager rating, internal mobility, pay equity — independently predict the hazard of voluntary departure? The answer, expressed as hazard ratios, directly prioritizes retention interventions.
3. **Use t-tests and ANOVA for workforce equity audits.** Are promotion rates, compensation levels, or performance ratings statistically different across demographic groups? The ANOVA → Tukey HSD framework identifies both whether differences exist and which specific group pairs account for the difference.

---

## Impact

Survival analysis is rare in people analytics practice and represents a genuine differentiator in portfolio and professional capability. The ability to model time-to-event outcomes — accounting for censoring, visualizing differential hazard by subgroup, and estimating covariate-adjusted hazard ratios — produces workforce intelligence that snapshot attrition rates cannot. This project demonstrates that capability alongside the full statistical toolkit required to build toward it.

---

*Analysis by Mintay Misgano | Tools: R (survival, survminer, ggplot2, broom) | Data: Lung disease dataset (N=228) | Course: Programming for Data Analytics: R, SPU (Winter 2023)*
