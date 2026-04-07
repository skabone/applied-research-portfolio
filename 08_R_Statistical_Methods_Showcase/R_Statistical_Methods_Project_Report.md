# R Statistical Methods Showcase

**Author:** Mintay Misgano, PhD
**Year:** 2023
**Tools:** R, tidyverse, survival, survminer, car, broom, ggplot2
**Dataset:** Lung disease survival data (N = 228)

---

## Abstract

This project presents a comparative showcase of core statistical methods implemented in R. The collection includes descriptive analysis, t-tests, ANOVA, linear regression, logistic regression, Kaplan-Meier estimation, and Cox proportional hazards modeling. All methods are applied to the same time-to-event dataset so they can be interpreted within a shared analytical context. The project is designed as a reproducible methods demonstration rather than a single applied domain study.

---

## 1. Project Context

This project was developed from graduate coursework in R-based statistical analysis. The goal of consolidating the work into one report was to show how several commonly taught methods relate to one another when applied to the same dataset rather than presented as isolated assignments.

The sequence moves from simpler group comparisons through regression-based modeling and ends with survival analysis, which is especially useful when the timing of an event matters and some observations are censored.

---

## 2. Dataset

The project uses a public lung disease survival dataset with 228 observations. It contains a survival-time variable, an event-status indicator, and several patient-level predictors such as age, sex, performance ratings, and health-related measures.

This dataset works well for a methods collection because it supports multiple styles of analysis:

- mean comparisons across groups
- continuous-outcome regression
- binary event modeling
- time-to-event modeling with censoring

---

## 3. Methods

### 3.1 Foundational Statistical Methods

- Descriptive summaries and grouped exploration
- Welch's t-test
- One-way ANOVA with Tukey HSD follow-up comparisons
- Linear regression with diagnostic plots
- Logistic regression with odds ratios

### 3.2 Survival Analysis

- Kaplan-Meier survival curves
- Log-rank tests
- Cox proportional hazards regression
- Proportional hazards assumption checks

### 3.3 Source Workflow

The analysis is maintained in [R_Statistical_Methods_Project_Report.Rmd](/Users/Taco/Library/CloudStorage/ProtonDrive-Skabone@pm.me-folder/2!!Career/GitHub_Portfolio/08_R_Statistical_Methods_Collection/GitHub_Ready/R_Statistical_Methods_Project_Report.Rmd), which serves as the source document for the long-form report.

---

## 4. Main Results

The project demonstrates that the same dataset can support multiple layers of statistical interpretation depending on the question being asked.

- Group-comparison methods identify whether survival-related differences are visible across categories.
- Regression methods show how individual predictors relate to continuous or binary outcomes.
- Survival analysis adds a more appropriate framework when the timing of an event and censoring both matter.

Within this workflow, survival analysis is the most distinctive component because it moves beyond whether an event happened and focuses on when it happened.

---

## 5. Interpretation

The main value of the collection is methodological range. It demonstrates not only familiarity with individual statistical procedures, but also the ability to choose among them based on the structure of the outcome variable.

The project also shows the advantages of R Markdown as an analysis format: code, output, interpretation, and model diagnostics can live together in one reproducible document.

---

## 6. Limitations

**Teaching dataset:** This is a public instructional dataset and should be interpreted as a methods demonstration.

**Single data context:** Results come from one medical survival dataset and are not intended as broad domain conclusions.

**Comparative emphasis:** The project prioritizes range and workflow over deep optimization of any single model.

---

## 7. Conclusion

This project demonstrates a broad R-based statistical toolkit in a single, coherent workflow. By combining classical inference, regression, and survival analysis in one reproducible package, it functions as both a methods collection and a compact demonstration of analytical judgment across different kinds of outcomes.
