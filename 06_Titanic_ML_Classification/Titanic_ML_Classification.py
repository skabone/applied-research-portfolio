"""
Titanic ML Classification
=========================
Author: Mintay Misgano, PhD
Course Context: Graduate coursework in data mining
Best Public Leaderboard Score: 0.79186

Description
-----------
Binary-classification benchmark project: predict passenger survival on the
Titanic using demographic and ticket-related features. This script implements
an end-to-end pipeline including data cleaning, feature engineering,
multi-model training, cross-validated evaluation, and a hard-voting ensemble.

Pipeline
--------
1. Load and inspect raw data
2. Feature engineering and imputation
3. Train individual classifiers (Logistic Regression, Naive Bayes, Decision Tree,
   Random Forest, Gradient Boosting)
4. Evaluate each classifier via cross-validation
5. Build a hard-voting ensemble from the 5 best models
6. Generate a Kaggle submission file
"""

# ── Imports ──────────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model   import LogisticRegression
from sklearn.naive_bayes    import GaussianNB
from sklearn.tree           import DecisionTreeClassifier
from sklearn.ensemble       import (RandomForestClassifier,
                                    GradientBoostingClassifier,
                                    VotingClassifier)
from sklearn.preprocessing  import LabelEncoder, StandardScaler
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics         import accuracy_score, classification_report


# ── 1. Load Data ─────────────────────────────────────────────────────────────
train = pd.read_csv("../data/train.csv")
test  = pd.read_csv("../data/test.csv")

print("Training shape:", train.shape)
print("Test shape:    ", test.shape)
print("\nSurvival rate: {:.1%}".format(train["Survived"].mean()))
print("\nMissing values (train):\n", train.isnull().sum()[train.isnull().sum() > 0])


# ── 2. Feature Engineering ───────────────────────────────────────────────────

def engineer_features(df):
    """
    Applies a complete feature engineering pipeline to a Titanic dataframe.
    Works on both train and test sets identically.
    """
    df = df.copy()

    # --- Title extraction from Name ---
    df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.", expand=False).str.strip()
    # Consolidate rare titles
    rare_titles = ["Lady", "Countess", "Capt", "Col", "Don", "Dr", "Major",
                   "Rev", "Sir", "Jonkheer", "Dona"]
    df["Title"] = df["Title"].replace(rare_titles, "Rare")
    df["Title"] = df["Title"].replace({"Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs"})

    # --- Age imputation: median by (Title, Pclass) ---
    age_medians = df.groupby(["Title", "Pclass"])["Age"].transform("median")
    df["Age"] = df["Age"].fillna(age_medians)
    df["Age"] = df["Age"].fillna(df["Age"].median())  # fallback for any remaining NAs

    # --- Family size and solo traveller flag ---
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    # --- Fare: impute test set missing value; log-transform to reduce skew ---
    df["Fare"] = df["Fare"].fillna(df.groupby("Pclass")["Fare"].transform("median"))
    df["FareLog"] = np.log1p(df["Fare"])

    # --- Cabin: known vs. unknown (most values missing) ---
    df["HasCabin"] = df["Cabin"].notna().astype(int)

    # --- Embarked: fill 2 missing values with mode ---
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # --- Encode categorical variables ---
    le = LabelEncoder()
    df["Sex_enc"]      = le.fit_transform(df["Sex"])
    df["Embarked_enc"] = le.fit_transform(df["Embarked"])
    df["Title_enc"]    = le.fit_transform(df["Title"])

    # --- Age bands (ordinal) ---
    df["AgeBand"] = pd.cut(df["Age"],
                           bins=[0, 12, 18, 35, 60, 100],
                           labels=[0, 1, 2, 3, 4]).astype(int)

    return df


train = engineer_features(train)
test  = engineer_features(test)

# Feature set used for modeling
FEATURES = [
    "Pclass", "Sex_enc", "Age", "AgeBand", "FamilySize", "IsAlone",
    "FareLog", "HasCabin", "Embarked_enc", "Title_enc"
]

X      = train[FEATURES]
y      = train["Survived"]
X_test = test[FEATURES]

print("\nFeatures:", FEATURES)
print("X shape:", X.shape, "| X_test shape:", X_test.shape)


# ── 3. Define Individual Classifiers ─────────────────────────────────────────
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

models = {
    "Logistic Regression": LogisticRegression(max_iter=500, C=0.5, random_state=42),
    "Naive Bayes":         GaussianNB(),
    "Decision Tree":       DecisionTreeClassifier(max_depth=5, min_samples_split=10, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=200, max_depth=6,
                                                   min_samples_split=10, random_state=42),
    "Gradient Boosting":   GradientBoostingClassifier(n_estimators=200, max_depth=4,
                                                        learning_rate=0.05, random_state=42),
}


# ── 4. Cross-Validated Model Evaluation ──────────────────────────────────────
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("\n" + "="*55)
print("  Cross-Validated Accuracy (5-Fold Stratified CV)")
print("="*55)

cv_results = {}
for name, model in models.items():
    X_input = X_scaled if name == "Logistic Regression" else X
    scores  = cross_val_score(model, X_input, y, cv=cv, scoring="accuracy")
    cv_results[name] = scores
    print(f"  {name:<25}  {scores.mean():.4f} ± {scores.std():.4f}")


# ── 5. Voting Ensemble ────────────────────────────────────────────────────────
# Hard voting: each model casts one vote; majority wins.
# All 5 classifiers are included. For Logistic Regression we pass
# pre-scaled X inside a Pipeline for cleanliness in the ensemble.

from sklearn.pipeline import Pipeline

lr_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("lr",     LogisticRegression(max_iter=500, C=0.5, random_state=42))
])

ensemble = VotingClassifier(
    estimators=[
        ("lr",  lr_pipeline),
        ("nb",  GaussianNB()),
        ("dt",  DecisionTreeClassifier(max_depth=5, min_samples_split=10, random_state=42)),
        ("rf",  RandomForestClassifier(n_estimators=200, max_depth=6,
                                        min_samples_split=10, random_state=42)),
        ("gb",  GradientBoostingClassifier(n_estimators=200, max_depth=4,
                                             learning_rate=0.05, random_state=42)),
    ],
    voting="hard"
)

ensemble_scores = cross_val_score(ensemble, X, y, cv=cv, scoring="accuracy")
print(f"\n  {'Voting Ensemble (5×)':<25}  {ensemble_scores.mean():.4f} ± {ensemble_scores.std():.4f}")
print("="*55)


# ── 6. Fit Final Model and Generate Submission ────────────────────────────────
ensemble.fit(X, y)
predictions = ensemble.predict(X_test)

submission = pd.DataFrame({
    "PassengerId": test["PassengerId"],
    "Survived":    predictions
})
submission.to_csv("titanic_submission.csv", index=False)

print("\nSubmission saved to: titanic_submission.csv")
print("Predicted survival rate (test): {:.1%}".format(predictions.mean()))
print("\nKaggle Best Score (public leaderboard): 0.79186")


# ── 7. Feature Importance (Random Forest) ────────────────────────────────────
rf_model = RandomForestClassifier(n_estimators=200, max_depth=6,
                                   min_samples_split=10, random_state=42)
rf_model.fit(X, y)

importance_df = pd.DataFrame({
    "Feature":   FEATURES,
    "Importance": rf_model.feature_importances_
}).sort_values("Importance", ascending=False)

print("\nRandom Forest Feature Importance:")
print(importance_df.to_string(index=False))
