# HR Employee Attrition Analysis — IBM Benchmark Dataset

**Author:** Mintay Misgano, PhD  
**Dataset:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
**Question:** Which employee and job factors are most associated with attrition, and how well can standard classification models separate higher-risk from lower-risk cases?

---

## Overview

This project uses the IBM HR Analytics benchmark dataset (1,470 employees; 35 variables) to examine attrition patterns and compare several supervised learning approaches. The work moves from exploratory analysis to classification modeling, with PCA included as a supplementary exploratory step.

Completed as part of graduate coursework in people analytics and machine learning, the project is intended to demonstrate applied workflow, interpretation, and communication using public benchmark data.

Because this is a public benchmark dataset, the findings should be read as an analytical demonstration rather than as recommendations for deployment in a live organization without revalidation.

---

## Key Findings

- Attrition is a minority outcome in the dataset at about 16%, making class imbalance an important modeling issue.
- Overtime, compensation-related variables, job role, marital status, age, and tenure patterns all show meaningful relationships with attrition.
- Logistic Regression, Decision Tree, and Random Forest models all improved after balancing the training data.
- Logistic Regression produced the strongest overall test performance in this project, with AUC = 0.934 on the balanced evaluation setup.
- PCA was useful for exploring structure in the feature space, but it was not the main driver of predictive performance.

---

## Read This Project

- Start here for the project overview and file map
- Read `IBM_Project_Summary.md` for a short narrative interpretation of the project
- Read `IBM_Project_Report.md` for methods, results, and limitations in full
- Open the notebooks to inspect the analytic workflow step by step

---

## Project Files

| File | Purpose |
|---|---|
| `01_Data_Preparation_and_EDA.ipynb` | Data exploration, feature preparation, and class imbalance handling |
| `02_Classification_Modeling.ipynb` | Classification modeling and feature importance analysis |
| `03_PCA_Exploration.ipynb` | Dimensionality reduction and feature-space exploration |
| `IBM_Project_Summary.md` | Short narrative summary of the project and what it demonstrates |
| `IBM_Project_Report.md` | Full project report with methods, results, and limitations |

---

## Tools

- Python
- pandas, numpy, scikit-learn
- seaborn, matplotlib
- SMOTE, ADASYN
- Decision Tree, Random Forest, Logistic Regression, PCA

---

## Data Note

`HR_Attrition_IBM.csv` is a clean benchmark dataset with no missing values. It is useful for demonstrating workflow design, model comparison, and interpretation, but it should not be treated as evidence about IBM's current workforce or as a substitute for organization-specific validation.
