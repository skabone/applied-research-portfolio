"""
Job Change Prediction with CRISP-DM
===================================
Author: Mintay Misgano, PhD
Context: Graduate coursework in data mining (2022)

Description
-----------
This script applies the CRISP-DM framework to a public Kaggle dataset on
job-change intent among data science trainees. The goal is to demonstrate
an end-to-end data-mining workflow spanning business framing, preparation,
model comparison, and evaluation.

Dataset: Kaggle HR Analytics — Job Change of Data Scientists
  - N = 19,158 training records
  - Target: 1 = candidate looking for new job; 0 = not looking
  - Class imbalance: 25% positive (job-seekers), 75% negative

This project follows the CRISP-DM framework:
  1. Business Understanding
  2. Data Understanding (EDA)
  3. Data Preparation (cleaning, encoding, feature engineering)
  4. Modeling (Logistic Regression, Decision Tree, Random Forest)
  5. Evaluation (CV accuracy, ROC-AUC, confusion matrix)
  6. Deployment notes
"""

# ── Imports ──────────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model     import LogisticRegression
from sklearn.tree             import DecisionTreeClassifier
from sklearn.ensemble         import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing    import LabelEncoder, StandardScaler
from sklearn.model_selection  import cross_val_score, StratifiedKFold, train_test_split
from sklearn.metrics          import (accuracy_score, roc_auc_score,
                                      classification_report, confusion_matrix)
from sklearn.impute           import SimpleImputer


# ── 1. CRISP-DM: Business Understanding ──────────────────────────────────────
"""
Business question: Which data science trainees are likely to seek new employment
after completing our training program?

Success criteria:
  - ROC-AUC > 0.75 (sufficient for talent pipeline prioritization)
  - Precision on positive class (job-seekers) > 0.60 (limit false positives)

Deployment context: Predictions would feed into a recruiter dashboard showing
  probability-of-departure for each trainee cohort.
"""


# ── 2. Data Understanding ─────────────────────────────────────────────────────
train = pd.read_csv(
    "../DM Project/HR Anylytics Project/archive/aug_train.csv"
)
test  = pd.read_csv(
    "../DM Project/HR Anylytics Project/archive/aug_test.csv"
)

print("="*60)
print("  DATA UNDERSTANDING")
print("="*60)
print(f"\n  Training: {train.shape[0]:,} rows × {train.shape[1]} columns")
print(f"  Test:     {test.shape[0]:,} rows × {test.shape[1]} columns")
print(f"\n  Target distribution:")
print(f"    Not looking (0): {(train['target']==0).sum():,} ({(train['target']==0).mean():.1%})")
print(f"    Looking (1):     {(train['target']==1).sum():,} ({(train['target']==1).mean():.1%})")
print(f"\n  Missing values (training):")
print(train.isnull().sum()[train.isnull().sum() > 0].to_string())


# ── 3. Data Preparation ───────────────────────────────────────────────────────

def prep_features(df):
    """
    CRISP-DM: Data Preparation
    Clean, encode, and engineer features for ML modeling.
    Applied identically to train and test sets.
    """
    df = df.copy()

    # ── Missing value imputation ──────────────────────────────────────────────
    # Categorical: fill with mode (most frequent category)
    cat_cols = ["gender", "enrolled_university", "education_level",
                "major_discipline", "experience", "company_size",
                "company_type", "last_new_job"]
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].mode()[0])

    # ── Feature engineering ───────────────────────────────────────────────────

    # Ordinal: experience years → integer (">20" → 21, "<1" → 0)
    exp_map = {">20": 21, "<1": 0}
    df["experience_num"] = df["experience"].replace(exp_map)
    df["experience_num"] = pd.to_numeric(df["experience_num"], errors="coerce").fillna(10)

    # Ordinal: company size → midpoint integer
    size_map = {
        "<10": 5, "10/49": 30, "50-99": 75,
        "100-500": 300, "500-999": 750,
        "1000-4999": 2500, "5000-9999": 7500, "10000+": 12500
    }
    df["company_size_num"] = df["company_size"].replace(size_map)
    df["company_size_num"] = pd.to_numeric(df["company_size_num"], errors="coerce").fillna(
        df["company_size"].map(size_map).median()
    )

    # Ordinal: last_new_job → integer (">4" → 5, "never" → 0)
    lnj_map = {">4": 5, "never": 0}
    df["last_new_job_num"] = df["last_new_job"].replace(lnj_map)
    df["last_new_job_num"] = pd.to_numeric(df["last_new_job_num"], errors="coerce").fillna(2)

    # Binary flags
    df["has_relevant_exp"] = (df["relevent_experience"] == "Has relevent experience").astype(int)
    df["is_in_university"]  = (df["enrolled_university"] != "no_enrollment").astype(int)
    df["is_STEM"]           = (df["major_discipline"] == "STEM").astype(int)
    df["is_private"]        = (df["company_type"] == "Pvt Ltd").astype(int)
    df["log_training_hrs"]  = np.log1p(df["training_hours"])

    # Encode remaining categorical variables
    le = LabelEncoder()
    df["gender_enc"]    = le.fit_transform(df["gender"].astype(str))
    df["edu_enc"]       = le.fit_transform(df["education_level"].astype(str))

    return df


train_prep = prep_features(train)
test_prep  = prep_features(test)

FEATURES = [
    "city_development_index", "gender_enc", "has_relevant_exp",
    "is_in_university", "edu_enc", "experience_num",
    "company_size_num", "last_new_job_num", "log_training_hrs",
    "is_STEM", "is_private"
]

X = train_prep[FEATURES]
y = train_prep["target"]
X_test = test_prep[FEATURES]

# Impute any residual NaN from numeric conversion
imputer = SimpleImputer(strategy="median")
X       = pd.DataFrame(imputer.fit_transform(X),    columns=FEATURES)
X_test  = pd.DataFrame(imputer.transform(X_test),   columns=FEATURES)

print(f"\n  Feature matrix: {X.shape}")
print(f"  Features: {FEATURES}")


# ── 4. Modeling ───────────────────────────────────────────────────────────────
scaler   = StandardScaler()
X_scaled = scaler.fit_transform(X)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

models = {
    "Logistic Regression":  LogisticRegression(C=0.5, max_iter=500, random_state=42),
    "Decision Tree":        DecisionTreeClassifier(max_depth=6, min_samples_split=20, random_state=42),
    "Random Forest":        RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42),
    "Gradient Boosting":    GradientBoostingClassifier(n_estimators=150, max_depth=4,
                                                        learning_rate=0.08, random_state=42),
}


# ── 5. Evaluation ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("  CRISP-DM: EVALUATION")
print("="*60)
print(f"\n  {'Model':<25} {'CV Acc':>8}  {'CV AUC':>8}")
print("  " + "-"*45)

cv_results = {}
for name, model in models.items():
    X_input = X_scaled if name == "Logistic Regression" else X
    acc  = cross_val_score(model, X_input, y, cv=cv, scoring="accuracy").mean()
    auc  = cross_val_score(model, X_input, y, cv=cv, scoring="roc_auc").mean()
    cv_results[name] = {"accuracy": acc, "auc": auc}
    print(f"  {name:<25} {acc:>8.4f}  {auc:>8.4f}")

# Best model: Gradient Boosting (or whichever is highest)
best_name = max(cv_results, key=lambda k: cv_results[k]["auc"])
print(f"\n  Best model (by AUC): {best_name}")

# Fit best model for detailed evaluation
best_model = models[best_name]
X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2,
                                              stratify=y, random_state=42)
best_model.fit(X_tr, y_tr)
y_pred      = best_model.predict(X_val)
y_pred_prob = best_model.predict_proba(X_val)[:, 1]

print(f"\n  Holdout accuracy: {accuracy_score(y_val, y_pred):.4f}")
print(f"  Holdout AUC:      {roc_auc_score(y_val, y_pred_prob):.4f}")
print(f"\n  Classification Report:\n{classification_report(y_val, y_pred)}")

cm = confusion_matrix(y_val, y_pred)
print(f"\n  Confusion Matrix:")
print(f"    TN={cm[0,0]:4d}  FP={cm[0,1]:4d}")
print(f"    FN={cm[1,0]:4d}  TP={cm[1,1]:4d}")


# ── Feature Importance ─────────────────────────────────────────────────────────
print("\n  Feature Importance (best model):")
if hasattr(best_model, "feature_importances_"):
    imp_df = pd.DataFrame({
        "Feature":    FEATURES,
        "Importance": best_model.feature_importances_
    }).sort_values("Importance", ascending=False)
    print(imp_df.round(4).to_string(index=False))


# ── 6. Deployment Notes ────────────────────────────────────────────────────────
print("\n" + "="*60)
print("  CRISP-DM: DEPLOYMENT")
print("="*60)
print("""
  Deployment recommendation:
  ------------------------------------------------------------------
  1. Apply the best model to each new trainee cohort at mid-program
  2. Score each trainee with job-change probability (predict_proba[:, 1])
  3. Flag trainees with P(job-change) > 0.5 for recruiter follow-up
  4. Trainees with P > 0.7: offer accelerated internal placement
     to retain them before external search escalates
  5. Re-train the model quarterly on updated enrollment data
  6. Monitor AUC drift — if AUC falls below 0.72, trigger retraining

  Key predictor interpretation:
  - city_development_index: High CDI → strong local job market →
    higher intent to seek new employment
  - has_relevant_exp: Experienced candidates have more alternatives →
    higher departure intent
  - experience_num: Mid-career professionals (5–10 years) show peak
    job-seeking behavior; very senior candidates are more stable
  - company_size_num: Candidates from very large/very small firms
    show different stability profiles
  ------------------------------------------------------------------
""")

# Generate submission file for Kaggle
best_model_full = models[best_name]
best_model_full.fit(X, y)
test_preds = best_model_full.predict(X_test)
submission = pd.DataFrame({
    "enrollee_id": test["enrollee_id"],
    "target":      test_preds
})
submission.to_csv("hr_jobchange_submission.csv", index=False)
print("  Submission saved: hr_jobchange_submission.csv")
print("  Done.")
