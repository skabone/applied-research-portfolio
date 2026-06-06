# Results Snapshot

Metric summary for Project 01: IBM HR Employee Attrition Analysis.

## Dataset

- `N = 1,470` employee records
- Attrition cases: `237` (`16.1%`)
- Non-attrition cases: `1,233` (`83.9%`)
- Variables: `35` (4 removed before modeling; 31 used)

## Classification Performance (held-out test set, SMOTE-balanced training)

| Model | Accuracy | Precision | Recall | F1-Score | AUC |
|---|---|---|---|---|---|
| Logistic Regression | 93.4% | 96.0% | 90.5% | 93.2% | 0.934 |
| Random Forest | 90.1% | 91.3% | 86.4% | 88.8% | 0.901 |
| Decision Tree | 83.7% | 79.0% | 83.2% | 81.2% | 0.837 |

Logistic Regression produced the strongest overall performance. All models improved after class-imbalance correction via SMOTE and ADASYN.

## Top Feature Signals (consistent across exploratory analysis and tree-based models)

| Signal | Pattern |
|---|---|
| Overtime | Employees working overtime show substantially higher attrition rates |
| Monthly income | Lower income strongly associated with higher attrition |
| Stock option level | Higher stock option level associated with lower attrition |
| Age | Younger employees show higher attrition patterns |
| Job involvement | Lower involvement associated with higher attrition |
| Job satisfaction | Lower satisfaction associated with higher attrition |

## PCA

- Standardized PCA produced interpretable components reflecting tenure, compensation, and engagement dimensions.
- Unstandardized PCA was dominated by high-magnitude income-related variables.
- PCA added descriptive insight but was not central to classification performance.
