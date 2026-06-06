# Project 01 — IBM HR Employee Attrition Analysis

**Author:** Mintay Misgano, PhD  
**Dataset:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
**Question:** Which employee and job factors are most associated with attrition, and how well can standard classification models separate higher-risk from lower-risk cases?

---

## Overview

This project uses the IBM HR Analytics benchmark dataset (1,470 employees; 35 variables) to examine attrition patterns and compare several supervised learning approaches. The work moves from exploratory analysis to classification modeling, with PCA included as a supplementary exploratory step.

Completed as part of graduate coursework in people analytics and machine learning, the analysis emphasizes applied workflow, interpretation, and communication using public benchmark data.

Because this is a public benchmark dataset, the findings should be read as an analytical demonstration rather than as recommendations for deployment in a live organization without revalidation.

---

## Key Findings

- Attrition is a minority outcome at about 16%, making class imbalance an important modeling issue.
- Overtime, compensation-related variables, job role, marital status, age, and tenure all show meaningful relationships with attrition.
- All three models improved after balancing the training data via SMOTE and ADASYN.
- Logistic Regression produced the strongest overall test performance: AUC = 0.934.
- PCA was useful for exploring feature-space structure but was not central to predictive performance.

---

## File Map

| File | Purpose |
|---|---|
| `01_Project_Summary.md` | Short narrative summary of the project and practical value |
| `02_Project_Report.md` | Full project report with methods, results, and limitations |
| `01_Data_Preparation_and_EDA.ipynb` | Data exploration, feature preparation, and class imbalance handling |
| `02_Classification_Modeling.ipynb` | Classification modeling and feature importance analysis |
| `03_PCA_Exploration.ipynb` | Dimensionality reduction and feature-space exploration |
| `docs/Results_Snapshot.md` | Verified metrics table and top feature signals |

---

## Tools

Python · pandas · numpy · scikit-learn · seaborn · matplotlib · SMOTE · ADASYN · Logistic Regression · Random Forest · Decision Tree · PCA

---

## Data Note

`HR_Attrition_IBM.csv` is a clean public benchmark dataset with no missing values. It is useful for demonstrating workflow design, model comparison, and interpretation, but should not be treated as evidence about IBM's current workforce or as a substitute for organization-specific validation.
