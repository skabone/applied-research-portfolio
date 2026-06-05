# Project 11 - Confirmatory Factor Analysis

Author: Mintay Misgano, PhD

This project applies confirmatory factor analysis to evaluate the dimensional structure of the Gendered Racial Microaggressions Scale for Asian American Women (GRMSAAW). The analysis compares a unidimensional model with a four-factor correlated model using simulated data based on published parameters, and replicates the CFA workflow in both R and Python.

## Practical Value

- Formal comparison of competing CFA measurement models
- Interpretation of common fit indices including CFI, RMSEA, SRMR, AIC, and chi-square difference tests
- Cross-platform replication using `lavaan` in R and `semopy` in Python
- Psychometric reasoning about when subscales should be scored separately rather than collapsed

## Main Finding

The four-factor model fit the data substantially better than the unidimensional model across every major fit index. The results support treating the GRMSAAW as a multidimensional instrument with distinguishable subscales.

## Project Files

- [CFA_Project_Summary.md](./CFA_Project_Summary.md) provides the short overview.
- Use [CFA_Project_Report.md](./CFA_Project_Report.md) for the full write-up.
- See [02_CFA_Analysis_R.md](./02_CFA_Analysis_R.md) and [03_CFA_Analysis_Python.ipynb](./03_CFA_Analysis_Python.ipynb) for the platform-specific analyses.

## Data Note

The dataset in this project is simulated from published factor loadings and item-level descriptives. The project is therefore best interpreted as a psychometric methods demonstration and replication exercise rather than as a new empirical validation sample.
