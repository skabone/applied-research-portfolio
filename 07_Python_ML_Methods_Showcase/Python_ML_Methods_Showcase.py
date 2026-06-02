"""
Python Machine Learning Methods Showcase
=========================================
Author: Mintay Misgano, PhD
Context: Graduate coursework in Python and machine learning (2022)

Description
-----------
This script consolidates core supervised and unsupervised machine learning
methods into a single comparative workflow. All methods are applied to the
ISLR College dataset so their behavior, evaluation, and tradeoffs can be
compared on the same structured problem.

The showcase covers:
  1. Exploratory Data Analysis (EDA)
  2. Linear Regression (OLS) with feature engineering
  3. Logistic Regression (binary classification)
  4. Decision Tree classification
  5. Support Vector Machine (SVM)
  6. k-Means Clustering + Gaussian Mixture Models (GMM)
  7. Principal Components Analysis (PCA)
  8. Random Forest Ensemble

Dataset: College_Data.csv (ISLR College dataset)
  - 777 U.S. colleges and universities
  - Features: application volume, acceptance rate, enrollment, tuition,
    faculty qualifications, graduation rates, and more
  - Binary outcome: Private (1) vs. Public (0)
"""

# ── Imports ──────────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

import matplotlib
matplotlib.use("Agg")  # non-interactive backend for script mode
import matplotlib.pyplot as plt

from sklearn.model_selection  import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing    import StandardScaler, LabelEncoder
from sklearn.linear_model     import LinearRegression, LogisticRegression
from sklearn.tree             import DecisionTreeClassifier
from sklearn.svm              import SVC
from sklearn.ensemble         import RandomForestClassifier, GradientBoostingClassifier
from sklearn.cluster          import KMeans
from sklearn.mixture          import GaussianMixture
from sklearn.decomposition    import PCA
from sklearn.metrics          import (accuracy_score, classification_report,
                                      confusion_matrix, mean_squared_error, r2_score)


# ── 0. Load and Inspect Data ─────────────────────────────────────────────────
df = pd.read_csv("../Week 6 - Clustering and GMM/College_Data.csv")

# Encode target variable: Private (Yes/No) → 1/0
df["Private_bin"] = (df["Private"] == 1).astype(int)

print("="*60)
print("  DATASET OVERVIEW")
print("="*60)
print(f"  Shape: {df.shape}")
print(f"  Columns: {list(df.columns)}")
print(f"  Private institutions: {df['Private_bin'].sum()} "
      f"({df['Private_bin'].mean():.1%})")
print(f"  Public institutions:  {(1 - df['Private_bin']).sum()} "
      f"({(1 - df['Private_bin']).mean():.1%})")
print(f"\n  Missing values: {df.isnull().sum().sum()}")


# ── 1. Exploratory Data Analysis ─────────────────────────────────────────────
print("\n" + "="*60)
print("  1. EXPLORATORY DATA ANALYSIS")
print("="*60)

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"\n  Numeric features: {len(numeric_cols)}")
print(df[numeric_cols].describe().round(1).to_string())

# Correlation with Graduation Rate
grad_corr = (df[numeric_cols]
             .corr()["Grad.Rate"]
             .drop("Grad.Rate")
             .sort_values(ascending=False))
print("\n  Top correlates of Graduation Rate:")
print(grad_corr.head(6).round(3).to_string())


# ── 2. Linear Regression: Predicting Graduation Rate ─────────────────────────
print("\n" + "="*60)
print("  2. LINEAR REGRESSION — Predicting Graduation Rate")
print("="*60)

features_lr = ["Outstate", "Top10perc", "Expend", "PhD", "S.F.Ratio",
               "perc.alumni", "Private_bin"]
target_lr   = "Grad.Rate"

df_lr = df[features_lr + [target_lr]].dropna()
X_lr  = df_lr[features_lr]
y_lr  = df_lr[target_lr]

X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(
    X_lr, y_lr, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train_lr, y_train_lr)
y_pred_lr = lr_model.predict(X_test_lr)

r2   = r2_score(y_test_lr, y_pred_lr)
rmse = np.sqrt(mean_squared_error(y_test_lr, y_pred_lr))

print(f"\n  R²:   {r2:.3f}")
print(f"  RMSE: {rmse:.2f} percentage points")
print("\n  Coefficients:")
coef_df = pd.DataFrame({"Feature": features_lr,
                         "Coefficient": lr_model.coef_.round(3)}).sort_values(
                             "Coefficient", key=abs, ascending=False)
print(coef_df.to_string(index=False))


# ── 3. Logistic Regression: Private vs. Public Classification ────────────────
print("\n" + "="*60)
print("  3. LOGISTIC REGRESSION — Private vs. Public")
print("="*60)

FEATURES_CLF = ["Apps", "Accept", "Enroll", "Top10perc", "Outstate",
                "Room.Board", "PhD", "S.F.Ratio", "Expend", "Grad.Rate"]
TARGET_CLF   = "Private_bin"

df_clf = df[FEATURES_CLF + [TARGET_CLF]].dropna()
X_clf  = df_clf[FEATURES_CLF]
y_clf  = df_clf[TARGET_CLF]

scaler    = StandardScaler()
X_scaled  = scaler.fit_transform(X_clf)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

logit = LogisticRegression(C=1.0, max_iter=500, random_state=42)
logit_cv = cross_val_score(logit, X_scaled, y_clf, cv=cv, scoring="accuracy")
print(f"\n  CV Accuracy: {logit_cv.mean():.4f} ± {logit_cv.std():.4f}")

logit.fit(X_scaled, y_clf)
print(f"\n  Full-data accuracy: {accuracy_score(y_clf, logit.predict(X_scaled)):.4f}")


# ── 4. Decision Tree ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("  4. DECISION TREE — Private vs. Public")
print("="*60)

dt = DecisionTreeClassifier(max_depth=5, min_samples_split=10, random_state=42)
dt_cv = cross_val_score(dt, X_clf, y_clf, cv=cv, scoring="accuracy")
print(f"\n  CV Accuracy: {dt_cv.mean():.4f} ± {dt_cv.std():.4f}")

dt.fit(X_clf, y_clf)
feat_imp = pd.DataFrame({"Feature": FEATURES_CLF,
                          "Importance": dt.feature_importances_}).sort_values(
                              "Importance", ascending=False)
print("\n  Top 5 features (Gini importance):")
print(feat_imp.head(5).round(4).to_string(index=False))


# ── 5. Support Vector Machine ─────────────────────────────────────────────────
print("\n" + "="*60)
print("  5. SUPPORT VECTOR MACHINE (RBF Kernel)")
print("="*60)

svm = SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)
svm_cv = cross_val_score(svm, X_scaled, y_clf, cv=cv, scoring="accuracy")
print(f"\n  CV Accuracy: {svm_cv.mean():.4f} ± {svm_cv.std():.4f}")


# ── 6. k-Means Clustering ────────────────────────────────────────────────────
print("\n" + "="*60)
print("  6. k-MEANS CLUSTERING (k=2)")
print("="*60)

X_cluster = scaler.fit_transform(X_clf)

kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X_cluster)

cluster_df = df_clf.copy()
cluster_df["Cluster"] = kmeans.labels_

# Compare cluster assignments to actual Private label
print("\n  Cluster vs. Private label:")
print(pd.crosstab(cluster_df["Cluster"], cluster_df["Private_bin"],
                   rownames=["Cluster"], colnames=["Private"]))

# Cluster profiles (key means)
print("\n  Cluster mean profiles (selected features):")
print(cluster_df.groupby("Cluster")[
    ["Outstate", "Expend", "Grad.Rate", "Top10perc"]
].mean().round(1).to_string())

# Elbow method — inertia for k = 1..8
inertias = []
for k in range(1, 9):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_cluster)
    inertias.append(km.inertia_)

print(f"\n  Inertia by k: {[round(i, 0) for i in inertias]}")
print("  Elbow appears at k=2 or k=3 — consistent with Private/Public split")


# ── 7. Gaussian Mixture Model ────────────────────────────────────────────────
print("\n" + "="*60)
print("  7. GAUSSIAN MIXTURE MODEL (n_components=2)")
print("="*60)

gmm = GaussianMixture(n_components=2, covariance_type="full",
                       random_state=42, n_init=5)
gmm.fit(X_cluster)
gmm_labels = gmm.predict(X_cluster)

cluster_df["GMM"] = gmm_labels
print("\n  GMM vs. Private label:")
print(pd.crosstab(cluster_df["GMM"], cluster_df["Private_bin"],
                   rownames=["GMM Cluster"], colnames=["Private"]))

bic = gmm.bic(X_cluster)
aic = gmm.aic(X_cluster)
print(f"\n  BIC: {bic:.1f} | AIC: {aic:.1f}")


# ── 8. Principal Components Analysis ─────────────────────────────────────────
print("\n" + "="*60)
print("  8. PRINCIPAL COMPONENTS ANALYSIS")
print("="*60)

pca = PCA()
pca.fit(X_cluster)

explained = pca.explained_variance_ratio_
cumulative = np.cumsum(explained)

print("\n  Variance explained per component:")
for i, (e, c) in enumerate(zip(explained, cumulative), 1):
    bar = "█" * int(e * 100)
    print(f"  PC{i:2d}: {e:.3f}  ({c:.3f} cumulative) {bar}")
    if c > 0.90:
        print(f"\n  → {i} components explain ≥90% of variance")
        break

# PCA with 2 components for visualization
pca2 = PCA(n_components=2)
X_pca2 = pca2.fit_transform(X_cluster)
print(f"\n  Variance captured by PC1 + PC2: {pca2.explained_variance_ratio_.sum():.3f}")

# Top loadings for PC1
loadings_pc1 = pd.Series(
    np.abs(pca2.components_[0]),
    index=FEATURES_CLF
).sort_values(ascending=False)
print("\n  Top PC1 loadings (|loading|):")
print(loadings_pc1.head(5).round(3).to_string())


# ── 9. Random Forest Ensemble ─────────────────────────────────────────────────
print("\n" + "="*60)
print("  9. RANDOM FOREST ENSEMBLE — Private vs. Public")
print("="*60)

rf = RandomForestClassifier(n_estimators=200, max_depth=None,
                              min_samples_split=5, random_state=42)
rf_cv = cross_val_score(rf, X_clf, y_clf, cv=cv, scoring="accuracy")
print(f"\n  CV Accuracy: {rf_cv.mean():.4f} ± {rf_cv.std():.4f}")

rf.fit(X_clf, y_clf)
rf_importance = pd.DataFrame({"Feature": FEATURES_CLF,
                                "Importance": rf.feature_importances_}).sort_values(
                                    "Importance", ascending=False)
print("\n  Feature importance (Random Forest):")
print(rf_importance.round(4).to_string(index=False))


# ── 10. Model Comparison Summary ─────────────────────────────────────────────
print("\n" + "="*60)
print("  10. MODEL COMPARISON SUMMARY — Private vs. Public Classification")
print("="*60)
print(f"\n  {'Model':<28} {'CV Accuracy':>12}  {'CV Std':>8}")
print("  " + "-"*52)
results = [
    ("Logistic Regression",  logit_cv.mean(), logit_cv.std()),
    ("Decision Tree",        dt_cv.mean(),    dt_cv.std()),
    ("SVM (RBF)",            svm_cv.mean(),   svm_cv.std()),
    ("Random Forest",        rf_cv.mean(),    rf_cv.std()),
]
for name, mean, std in sorted(results, key=lambda x: x[1], reverse=True):
    print(f"  {name:<28} {mean:>12.4f}  {std:>8.4f}")

print("\nDone.")
