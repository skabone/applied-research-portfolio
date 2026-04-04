# Project 07 — Python ML Methods Showcase

**8 methods, 1 dataset, honest model comparison** | Supervised + Unsupervised | Python, scikit-learn

---

## Overview

This project distills eight weekly lab modules from a graduate-level Python ML course into a unified, comparative demonstration applied to the U.S. College dataset (N = 777 institutions). Each method is implemented cleanly, evaluated via 5-fold stratified cross-validation, and compared on the same classification problem — Private vs. Public institution — to enable honest method-to-method comparison.

The dataset's structure mirrors common people analytics problems: a binary outcome, mixed numeric features, moderate class imbalance, and meaningful clustering structure in the feature space.

---

## Methods Covered

| # | Method | Task | CV Accuracy |
|:--|:-------|:-----|:-----------:|
| 1 | EDA + Linear Regression | Predict graduation rate | R² ≈ .73 |
| 2 | Logistic Regression | Classify Private/Public | ~91% |
| 3 | Decision Tree | Classify Private/Public | ~89% |
| 4 | Support Vector Machine (RBF) | Classify Private/Public | ~92% |
| 5 | **Random Forest (best)** | **Classify Private/Public** | **~93%** |
| 6 | k-Means (k=2) | Cluster institutions | Recovers P/P split |
| 7 | Gaussian Mixture Model | Soft cluster assignments | BIC-optimal at k=2 |
| 8 | PCA | Dimensionality reduction | 4–5 PCs → ≥90% variance |

---

## People Analytics Transfer

| ML Method | Workforce Application |
|:----------|:----------------------|
| Logistic Regression | Attrition risk scoring (interpretable for HR BPs) |
| Decision Tree | Explainable prediction paths for managers |
| Random Forest | Flight risk model for HRIS integration |
| k-Means | Employee segment identification for retention programs |
| GMM | Probabilistic segment membership for borderline cases |
| PCA | Engagement survey dimension reduction |

---

## Files

| File | Description |
|:-----|:------------|
| `ML_Methods_Showcase.py` | Complete pipeline: all 8 methods, CV evaluation, model comparison |
| `ML_Methods_Project_Report.md` | Full narrative report with method rationale and PA transfer |
| `Executive_Brief.md` | 1-page practitioner summary |

**Note:** Data file (`College_Data.csv`) is in `../Week 6 - Clustering and GMM/`. Script uses relative path.

---

## Tools

- **Language:** Python
- **Libraries:** scikit-learn, pandas, numpy, matplotlib
- **Methods:** OLS regression, Logistic Regression, Decision Tree, SVM (RBF), Random Forest, k-Means, GMM, PCA
- **Evaluation:** 5-fold stratified cross-validation (all classifiers)

---

*Part of the [People Analytics Portfolio](../README.md) | Analyst: Mintay Misgano | Course: Programming for Data Analytics: Python & ML, SPU (Autumn 2022)*
