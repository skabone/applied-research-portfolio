# Project 09 — HR Analytics: Job Change Prediction (Data Mining)

**CRISP-DM pipeline** | Predicting data scientist job-seeking intent | N = 19,158 | Python, scikit-learn

---

## Overview

A company that trains data scientists wants to identify which trainees are actively seeking new employment — enabling optimized placement resources and proactive retention. This project applies the **CRISP-DM framework** to the Kaggle HR Analytics: Job Change of Data Scientists dataset, covering the full arc from business understanding through deployment logic.

The problem is structurally identical to **voluntary attrition prediction** in corporate people analytics:

| Dataset Variable | People Analytics Equivalent |
|:----------------|:---------------------------|
| `target` (1=looking for new job) | Voluntary departure flag |
| `city_development_index` | Regional labor market competitiveness |
| `experience` | Tenure / years in current role |
| `company_size` / `company_type` | Current employer profile |
| `training_hours` | Recent L&D investment received |

---

## Results

| Model | CV Accuracy | CV AUC |
|:------|:-----------:|:------:|
| Logistic Regression | ~77% | ~0.75 |
| Decision Tree | ~76% | ~0.72 |
| Random Forest | ~78% | ~0.77 |
| **Gradient Boosting (best)** | **~79%** | **~0.79** |

- **ROC-AUC > 0.75** achieved → deployment threshold met
- Top predictors: city development index, relevant experience flag, experience years, company size

---

## CRISP-DM Stages Covered

```
1. Business Understanding  → Define success: ROC-AUC > 0.75, Precision > 0.60
2. Data Understanding      → EDA: 19,158 obs, 25% positive class, 6 vars with missingness
3. Data Preparation        → Mode imputation, ordinal encoding, log-transform, binary flags
4. Modeling                → LR, Decision Tree, Random Forest, Gradient Boosting + 5-fold CV
5. Evaluation              → Accuracy, AUC, confusion matrix, classification report
6. Deployment              → Score at mid-program; flag P(job-change) > 0.50 for recruiter
```

---

## Files

| File | Description |
|:-----|:------------|
| `HR_JobChange_DataMining.py` | Complete CRISP-DM pipeline script |
| `Executive_Brief.md` | 1-page practitioner summary |
| `README.md` | This file |

**Note:** Data files (`aug_train.csv`, `aug_test.csv`) are in `../DM Project/HR Anylytics Project/archive/`. Script uses relative paths.

---

## Tools

- **Language:** Python
- **Libraries:** scikit-learn, pandas, numpy
- **Framework:** CRISP-DM
- **Methods:** Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, stratified 5-fold CV, ROC-AUC, SimpleImputer, LabelEncoder

---

*Part of the [People Analytics Portfolio](../README.md) | Analyst: Mintay Misgano | Data: Kaggle HR Analytics (N=19,158) | Course: ISM 6359 Data Mining, SPU (Winter 2022)*
