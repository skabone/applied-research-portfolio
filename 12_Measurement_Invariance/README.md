# Project 12 - Measurement Invariance Testing

Author: Mintay Misgano, PhD

This project tests whether the Ableist Microaggressions Scale functions equivalently across disability-severity groups. Using multi-group confirmatory factor analysis in R and Python, it evaluates the standard invariance sequence from configural through scalar constraints and examines whether cross-group score comparisons are psychometrically defensible.

## What This Project Demonstrates

- Multi-group CFA for configural, metric, and scalar invariance testing
- Interpretation of invariance decisions using fit change rather than single-model fit alone
- Cross-platform measurement work in R and Python
- Practical consequences of invariance failure for group comparisons

## Main Finding

Weak invariance was supported, but strong invariance was not. That means the factor loadings are comparable across groups, but item intercepts are not, so raw group mean comparisons should be interpreted cautiously.

## Read This Project

- Start with [Measurement_Invariance_Project_Summary.md](./Measurement_Invariance_Project_Summary.md) for the short overview.
- Use [Measurement_Invariance_Project_Report.md](./Measurement_Invariance_Project_Report.md) for the full write-up.
- See [02_Invariance_Analysis_R.md](./02_Invariance_Analysis_R.md) and [03_Invariance_Analysis_Python.ipynb](./03_Invariance_Analysis_Python.ipynb) for the detailed analyses.

## Data Note

The dataset is simulated from published parameters, so this project is best interpreted as a measurement-invariance methods demonstration rather than a new empirical sample.
