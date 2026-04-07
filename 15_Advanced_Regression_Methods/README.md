# Project 15 - Advanced Regression Methods

Author: Mintay Misgano, PhD

This project collects several regression models used when ordinary linear regression is not appropriate. The methods are demonstrated in R across count outcomes, ordered categories, truncated samples, and censored outcomes so the collection functions as a practical reference for choosing the right model when the dependent variable violates standard OLS assumptions.

## What This Project Demonstrates

- Model selection based on outcome structure rather than defaulting to OLS
- Comparison of Poisson and negative binomial regression for count data
- Use of ordinal logistic regression for ranked response categories
- Use of truncated and Tobit regression when data are restricted by sampling or censoring
- Reproducible R Markdown workflow for a methods collection

## Methods Included

| Method | Outcome Type |
|--------|--------------|
| Poisson regression | Count |
| Negative binomial regression | Overdispersed count |
| Ordinal logistic regression | Ordered categorical |
| Truncated regression | Continuous, sampled range only |
| Tobit regression | Censored continuous outcome |

## Read This Project

- Start with [Advanced_Regression_Methods_Project_Summary.md](/Users/Taco/Library/CloudStorage/ProtonDrive-Skabone@pm.me-folder/2!!Career/GitHub_Portfolio/15_Advanced_Regression_Collection/GitHub_Ready/Advanced_Regression_Methods_Project_Summary.md) for the short overview.
- Use [Advanced_Regression_Methods_Project_Report.md](/Users/Taco/Library/CloudStorage/ProtonDrive-Skabone@pm.me-folder/2!!Career/GitHub_Portfolio/15_Advanced_Regression_Collection/GitHub_Ready/Advanced_Regression_Methods_Project_Report.md) for the long-form write-up.
- See [Advanced_Regression_Methods_Project_Report.Rmd](/Users/Taco/Library/CloudStorage/ProtonDrive-Skabone@pm.me-folder/2!!Career/GitHub_Portfolio/15_Advanced_Regression_Collection/GitHub_Ready/Advanced_Regression_Methods_Project_Report.Rmd) for the source document.

## Context Note

This is a methods collection rather than a single applied study. It is designed to show how different regression models fit different data-generating situations.
