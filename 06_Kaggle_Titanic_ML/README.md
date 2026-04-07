# Titanic ML Classification

**Author:** Mintay Misgano, PhD  
**Competition:** Kaggle Titanic: Machine Learning from Disaster  
**Best Public Leaderboard Score:** 0.79186

---

## Overview

This project uses the Kaggle Titanic competition as a benchmark binary-classification problem. The workflow includes feature engineering, multi-model comparison, cross-validated evaluation, and a hard-voting ensemble.

Completed as graduate coursework in data mining, the project is intended to demonstrate an applied machine-learning pipeline on a well-known public dataset.

---

## Key Results

| Submission | Method | Public Score |
|:-----------|:-------|:------------:|
| 1 | Single Decision Tree baseline | 0.76555 |
| 2 | 3-model voting ensemble | 0.77511 |
| 3 | 5-model voting ensemble | 0.78947 |
| **4** | **Tuned 5-model voting ensemble** | **0.79186** |

- Ensemble voting improved performance over the single-model baseline.
- Feature engineering contributed more to performance gains than minor model adjustments.
- The final workflow combined Logistic Regression, Naive Bayes, Decision Tree, Random Forest, and Gradient Boosting.

---

## Read This Project

- Start here for the project overview and file map
- Read `Titanic_Project_Summary.md` for the short narrative interpretation
- Read `Titanic_Project_Report.md` for methods, results, and limitations in full
- Open `Titanic_ML_Classification.ipynb` for a GitHub-rendered notebook view of the workflow
- Use `Titanic_ML_Classification.py` for the script version

---

## Project Files

| File | Purpose |
|:-----|:--------|
| `Titanic_ML_Classification.ipynb` | GitHub-rendered notebook companion for the modeling workflow |
| `Titanic_ML_Classification.py` | End-to-end classification pipeline and submission workflow |
| `Titanic_Project_Summary.md` | Short narrative summary of the project and what it demonstrates |
| `Titanic_Project_Report.md` | Full project report with methods, results, and limitations |

**Note:** Data files (`train.csv`, `test.csv`) are stored in `../data/` and the script uses relative paths.

---

## Benchmark Note

This is a public competition benchmark. The leaderboard score is useful as a point of comparison, but the main value of the project is the demonstrated workflow: feature engineering, model comparison, cross-validation, and ensemble construction on structured tabular data.
