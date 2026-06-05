"""Titanic passenger survival classification workflow.

The script rebuilds the public Kaggle Titanic analysis from project-local data,
creates diagnostic figures, evaluates several supervised classifiers with
stratified cross-validation, and writes a competition-style submission file.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
    VotingClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    balanced_accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_predict, cross_validate
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"
FIGURE_DIR = DOCS_DIR / "figures"
OUTPUT_DIR = BASE_DIR / "outputs"

RANDOM_STATE = 42
TARGET = "Survived"

NUMERIC_FEATURES = ["Age", "FareLog", "FamilySize", "IsAlone", "HasCabin"]
CATEGORICAL_FEATURES = [
    "Pclass",
    "Sex",
    "Embarked",
    "Title",
    "AgeBand",
    "FamilyCategory",
    "Deck",
]
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES

SUBMISSION_HISTORY = pd.DataFrame(
    [
        {
            "Attempt": 1,
            "Method": "Single decision tree baseline",
            "PublicScore": 0.76555,
        },
        {
            "Attempt": 2,
            "Method": "Three-model voting ensemble",
            "PublicScore": 0.77511,
        },
        {
            "Attempt": 3,
            "Method": "Five-model voting ensemble, first tuning pass",
            "PublicScore": 0.78947,
        },
        {
            "Attempt": 4,
            "Method": "Tuned five-model voting ensemble",
            "PublicScore": 0.79186,
        },
    ]
)


@dataclass(frozen=True)
class FeatureContext:
    """Training-set statistics used to transform train and test consistently."""

    age_by_title_class: pd.Series
    age_by_title: pd.Series
    global_age_median: float
    fare_by_class: pd.Series
    global_fare_median: float
    embarked_mode: str


def ensure_output_dirs() -> None:
    """Create deterministic project output locations before any files are saved."""

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Read the public Kaggle training and test files from project-local paths."""

    train = pd.read_csv(DATA_DIR / "train.csv")
    test = pd.read_csv(DATA_DIR / "test.csv")
    return train, test


def clean_title(title: str) -> str:
    """Collapse sparse honorifics into stable groups before one-hot encoding."""

    title = title.strip()
    title = {"Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs"}.get(title, title)
    common_titles = {"Mr", "Mrs", "Miss", "Master"}
    return title if title in common_titles else "Rare"


def extract_title(name: str) -> str:
    """Extract the honorific between the comma and period in the passenger name."""

    match = re.search(r",\s*([^.]*)\.", name)
    if not match:
        return "Rare"
    return clean_title(match.group(1))


def fit_feature_context(train: pd.DataFrame) -> FeatureContext:
    """Learn imputation values from the labeled training set only."""

    working = train.copy()
    working["Title"] = working["Name"].map(extract_title)
    age_by_title_class = working.groupby(["Title", "Pclass"])["Age"].median()
    age_by_title = working.groupby("Title")["Age"].median()
    fare_by_class = working.groupby("Pclass")["Fare"].median()

    return FeatureContext(
        age_by_title_class=age_by_title_class,
        age_by_title=age_by_title,
        global_age_median=float(working["Age"].median()),
        fare_by_class=fare_by_class,
        global_fare_median=float(working["Fare"].median()),
        embarked_mode=str(working["Embarked"].mode(dropna=True).iloc[0]),
    )


def age_imputation_value(row: pd.Series, context: FeatureContext) -> float:
    """Choose a contextual age median while retaining a global fallback."""

    title_class_key = (row["Title"], row["Pclass"])
    if title_class_key in context.age_by_title_class.index:
        value = context.age_by_title_class.loc[title_class_key]
        if not pd.isna(value):
            return float(value)

    if row["Title"] in context.age_by_title.index:
        value = context.age_by_title.loc[row["Title"]]
        if not pd.isna(value):
            return float(value)

    return context.global_age_median


def engineer_features(df: pd.DataFrame, context: FeatureContext) -> pd.DataFrame:
    """Turn raw Titanic records into a stable modeling table."""

    working = df.copy()

    # Titles encode age, gender norms, and social role more compactly than name text.
    working["Title"] = working["Name"].map(extract_title)

    missing_age = working["Age"].isna()
    if missing_age.any():
        working.loc[missing_age, "Age"] = working.loc[missing_age].apply(
            age_imputation_value, axis=1, context=context
        )

    working["Fare"] = working["Fare"].fillna(working["Pclass"].map(context.fare_by_class))
    working["Fare"] = working["Fare"].fillna(context.global_fare_median)
    working["FareLog"] = np.log1p(working["Fare"])

    working["Embarked"] = working["Embarked"].fillna(context.embarked_mode)
    working["FamilySize"] = working["SibSp"] + working["Parch"] + 1
    working["IsAlone"] = (working["FamilySize"] == 1).astype(int)
    working["HasCabin"] = working["Cabin"].notna().astype(int)
    working["Deck"] = working["Cabin"].str[0].fillna("Unknown")

    working["AgeBand"] = pd.cut(
        working["Age"],
        bins=[0, 12, 18, 35, 60, np.inf],
        labels=["Child", "Teen", "Adult", "Midlife", "Older"],
        include_lowest=True,
    ).astype(str)

    working["FamilyCategory"] = pd.cut(
        working["FamilySize"],
        bins=[0, 1, 4, np.inf],
        labels=["Solo", "Small family", "Large family"],
        include_lowest=True,
    ).astype(str)

    working["Pclass"] = working["Pclass"].astype(str)
    return working


def make_one_hot_encoder() -> OneHotEncoder:
    """Build a dense encoder while staying compatible across scikit-learn versions."""

    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        return OneHotEncoder(handle_unknown="ignore", sparse=False)


def make_preprocessor(scale_numeric: bool) -> ColumnTransformer:
    """Create a column transformer for numeric and categorical predictors."""

    numeric_transformer: str | StandardScaler
    numeric_transformer = StandardScaler() if scale_numeric else "passthrough"

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_transformer, NUMERIC_FEATURES),
            ("categorical", make_one_hot_encoder(), CATEGORICAL_FEATURES),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )


def make_pipeline(model: BaseEstimator, scale_numeric: bool = False) -> Pipeline:
    """Attach shared preprocessing to a classifier."""

    return Pipeline(
        steps=[
            ("preprocess", make_preprocessor(scale_numeric=scale_numeric)),
            ("model", model),
        ]
    )


def build_models() -> dict[str, Pipeline]:
    """Define model families that make different assumptions about the same data."""

    return {
        "Logistic Regression": make_pipeline(
            LogisticRegression(max_iter=1000, C=0.8, random_state=RANDOM_STATE),
            scale_numeric=True,
        ),
        "Gaussian Naive Bayes": make_pipeline(GaussianNB()),
        "Decision Tree": make_pipeline(
            DecisionTreeClassifier(
                max_depth=5,
                min_samples_leaf=8,
                random_state=RANDOM_STATE,
            )
        ),
        "Random Forest": make_pipeline(
            RandomForestClassifier(
                n_estimators=400,
                max_depth=6,
                min_samples_leaf=6,
                random_state=RANDOM_STATE,
                n_jobs=-1,
            )
        ),
        "Gradient Boosting": make_pipeline(
            GradientBoostingClassifier(
                n_estimators=140,
                max_depth=3,
                learning_rate=0.05,
                random_state=RANDOM_STATE,
            )
        ),
    }


def build_ensemble() -> VotingClassifier:
    """Construct a hard-voting ensemble from independent model instances."""

    models = build_models()
    return VotingClassifier(
        estimators=[
            ("lr", models["Logistic Regression"]),
            ("nb", models["Gaussian Naive Bayes"]),
            ("dt", models["Decision Tree"]),
            ("rf", models["Random Forest"]),
            ("gb", models["Gradient Boosting"]),
        ],
        voting="hard",
    )


def evaluate_models(X: pd.DataFrame, y: pd.Series) -> tuple[pd.DataFrame, np.ndarray]:
    """Compare candidate classifiers under the same stratified folds."""

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    scoring = {
        "accuracy": "accuracy",
        "balanced_accuracy": "balanced_accuracy",
    }
    rows: list[dict[str, float | str]] = []

    for name, model in build_models().items():
        scores = cross_validate(model, X, y, cv=cv, scoring=scoring)
        rows.append(
            {
                "Model": name,
                "AccuracyMean": scores["test_accuracy"].mean(),
                "AccuracySD": scores["test_accuracy"].std(),
                "BalancedAccuracyMean": scores["test_balanced_accuracy"].mean(),
                "BalancedAccuracySD": scores["test_balanced_accuracy"].std(),
            }
        )

    ensemble = build_ensemble()
    ensemble_scores = cross_validate(ensemble, X, y, cv=cv, scoring=scoring)
    rows.append(
        {
            "Model": "Hard-Voting Ensemble",
            "AccuracyMean": ensemble_scores["test_accuracy"].mean(),
            "AccuracySD": ensemble_scores["test_accuracy"].std(),
            "BalancedAccuracyMean": ensemble_scores["test_balanced_accuracy"].mean(),
            "BalancedAccuracySD": ensemble_scores["test_balanced_accuracy"].std(),
        }
    )

    out_of_fold_predictions = cross_val_predict(ensemble, X, y, cv=cv)
    return pd.DataFrame(rows).sort_values("AccuracyMean", ascending=False), out_of_fold_predictions


def format_percentage(value: float) -> str:
    """Return a one-decimal percentage string for report-friendly output."""

    return f"{value * 100:.1f}%"


def plot_survival_by_sex_class(train: pd.DataFrame) -> None:
    """Show the strongest descriptive split in the labeled data."""

    survival = (
        train.groupby(["Sex", "Pclass"], observed=True)[TARGET]
        .mean()
        .reset_index()
        .pivot(index="Pclass", columns="Sex", values=TARGET)
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(survival.index))
    width = 0.34
    colors = {"female": "#2F80ED", "male": "#E07A5F"}

    for offset, sex in [(-width / 2, "female"), (width / 2, "male")]:
        values = survival[sex].values
        bars = ax.bar(x + offset, values, width, label=sex.title(), color=colors[sex])
        ax.bar_label(bars, labels=[format_percentage(v) for v in values], padding=3, fontsize=9)

    ax.set_title("Survival rates varied sharply by sex and passenger class")
    ax.set_xlabel("Passenger class")
    ax.set_ylabel("Training-set survival rate")
    ax.set_xticks(x)
    ax.set_xticklabels([f"Class {label}" for label in survival.index])
    ax.set_ylim(0, 1.1)
    ax.legend(title="Sex")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fig01-survival-by-sex-class.png", dpi=200)
    plt.close(fig)


def plot_missingness(train: pd.DataFrame) -> None:
    """Quantify missing raw fields so imputation choices are visible."""

    missing = train.isna().mean().sort_values(ascending=False)
    missing = missing[missing > 0]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(missing.index[::-1], missing.values[::-1], color="#6A994E")
    ax.bar_label(bars, labels=[format_percentage(v) for v in missing.values[::-1]], padding=4)
    ax.set_title("Missingness was concentrated in Cabin and Age")
    ax.set_xlabel("Share of training records missing")
    ax.set_xlim(0, 0.85)
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fig02-missingness-profile.png", dpi=200)
    plt.close(fig)


def plot_submission_history() -> None:
    """Place the final leaderboard score in the context of earlier attempts."""

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(
        SUBMISSION_HISTORY["Attempt"],
        SUBMISSION_HISTORY["PublicScore"],
        marker="o",
        color="#335C67",
        linewidth=2.5,
    )
    for _, row in SUBMISSION_HISTORY.iterrows():
        ax.annotate(
            f"{row['PublicScore']:.5f}",
            (row["Attempt"], row["PublicScore"]),
            textcoords="offset points",
            xytext=(0, 9),
            ha="center",
            fontsize=9,
        )
    ax.set_title("Public leaderboard accuracy improved across four submissions")
    ax.set_xlabel("Submission attempt")
    ax.set_ylabel("Kaggle public leaderboard score")
    ax.set_xticks(SUBMISSION_HISTORY["Attempt"])
    ax.set_ylim(0.755, 0.800)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fig03-submission-history.png", dpi=200)
    plt.close(fig)


def plot_model_comparison(results: pd.DataFrame) -> None:
    """Compare cross-validated model accuracy with fold-to-fold uncertainty."""

    plot_df = results.sort_values("AccuracyMean", ascending=True)
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bars = ax.barh(
        plot_df["Model"],
        plot_df["AccuracyMean"],
        xerr=plot_df["AccuracySD"],
        color="#4D908E",
        error_kw={"elinewidth": 1.4, "capsize": 3},
    )
    ax.bar_label(
        bars,
        labels=[f"{value:.3f}" for value in plot_df["AccuracyMean"]],
        padding=5,
        fontsize=9,
    )
    ax.set_title("Tree ensembles led the cross-validated model comparison")
    ax.set_xlabel("Five-fold stratified cross-validated accuracy")
    ax.set_xlim(0.70, 0.89)
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fig04-cross-validated-model-comparison.png", dpi=200)
    plt.close(fig)


def plot_feature_importance(X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    """Fit a random forest and display the strongest engineered predictors."""

    model = build_models()["Random Forest"]
    model.fit(X, y)

    preprocessor = model.named_steps["preprocess"]
    feature_names = preprocessor.get_feature_names_out()
    forest = model.named_steps["model"]

    importance = (
        pd.DataFrame(
            {
                "Feature": feature_names,
                "Importance": forest.feature_importances_,
            }
        )
        .sort_values("Importance", ascending=False)
        .head(12)
    )

    fig, ax = plt.subplots(figsize=(8.5, 5.4))
    plot_df = importance.sort_values("Importance", ascending=True)
    bars = ax.barh(plot_df["Feature"], plot_df["Importance"], color="#9A031E")
    ax.bar_label(
        bars,
        labels=[f"{value:.3f}" for value in plot_df["Importance"]],
        padding=4,
        fontsize=8,
    )
    ax.set_title("Sex, title, class, and fare drove the random forest predictions")
    ax.set_xlabel("Gini importance")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fig05-feature-importance.png", dpi=200)
    plt.close(fig)
    return importance


def plot_confusion_matrix(y: pd.Series, predictions: Iterable[int]) -> np.ndarray:
    """Summarize out-of-fold ensemble errors in original class units."""

    matrix = confusion_matrix(y, predictions, labels=[0, 1])
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    image = ax.imshow(matrix, cmap="Blues")
    ax.set_title("Out-of-fold hard-voting ensemble confusion matrix")
    ax.set_xlabel("Predicted class")
    ax.set_ylabel("Observed class")
    ax.set_xticks([0, 1], labels=["Did not survive", "Survived"])
    ax.set_yticks([0, 1], labels=["Did not survive", "Survived"])

    threshold = matrix.max() / 2
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            color = "white" if matrix[i, j] > threshold else "black"
            ax.text(j, i, f"{matrix[i, j]}", ha="center", va="center", color=color, fontsize=12)

    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fig06-confusion-matrix.png", dpi=200)
    plt.close(fig)
    return matrix


def write_submission(model: VotingClassifier, X: pd.DataFrame, y: pd.Series, test_features: pd.DataFrame, test: pd.DataFrame) -> pd.DataFrame:
    """Fit the final ensemble on all labeled records and write test predictions."""

    model.fit(X, y)
    predictions = model.predict(test_features)
    submission = pd.DataFrame(
        {
            "PassengerId": test["PassengerId"],
            "Survived": predictions,
        }
    )
    submission.to_csv(OUTPUT_DIR / "titanic_submission.csv", index=False)
    return submission


def write_results_snapshot(
    train: pd.DataFrame,
    test: pd.DataFrame,
    results: pd.DataFrame,
    matrix: np.ndarray,
    feature_importance: pd.DataFrame,
    submission: pd.DataFrame,
    ensemble_predictions: np.ndarray,
) -> None:
    """Write a compact Markdown snapshot for the README and report to reference."""

    best_model = results.iloc[0]
    survival_count = int(train[TARGET].sum())
    nonsurvival_count = int((train[TARGET] == 0).sum())
    precision = precision_score(train[TARGET], ensemble_predictions)
    recall = recall_score(train[TARGET], ensemble_predictions)
    balanced_accuracy = balanced_accuracy_score(train[TARGET], ensemble_predictions)

    lines = [
        "# Results Snapshot",
        "",
        "This snapshot is produced by `04_Source_Code.py` from the public Kaggle Titanic files in `data/`.",
        "",
        "## Data Profile",
        "",
        f"- Training rows: {len(train):,}",
        f"- Test rows: {len(test):,}",
        f"- Observed survivors in training data: {survival_count:,} of {len(train):,} ({train[TARGET].mean():.1%})",
        f"- Observed non-survivors in training data: {nonsurvival_count:,} of {len(train):,} ({1 - train[TARGET].mean():.1%})",
        f"- Age missingness in training data: {train['Age'].isna().mean():.1%}",
        f"- Cabin missingness in training data: {train['Cabin'].isna().mean():.1%}",
        "",
        "## Model Comparison",
        "",
        "| Model | Accuracy mean | Accuracy SD | Balanced accuracy mean |",
        "|:--|--:|--:|--:|",
    ]

    for _, row in results.iterrows():
        lines.append(
            f"| {row['Model']} | {row['AccuracyMean']:.3f} | "
            f"{row['AccuracySD']:.3f} | {row['BalancedAccuracyMean']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## Ensemble Diagnostics",
            "",
            f"- Best cross-validated model by accuracy: {best_model['Model']} ({best_model['AccuracyMean']:.3f})",
            f"- Hard-voting ensemble out-of-fold precision for survived: {precision:.3f}",
            f"- Hard-voting ensemble out-of-fold recall for survived: {recall:.3f}",
            f"- Hard-voting ensemble out-of-fold balanced accuracy: {balanced_accuracy:.3f}",
            f"- Confusion matrix counts, observed rows by predicted columns [[0, 1], [0, 1]]: {matrix.tolist()}",
            f"- Final test-set predicted survival rate: {submission['Survived'].mean():.1%}",
            "- Best recorded Kaggle public leaderboard score: 0.79186",
            "",
            "## Top Random Forest Predictors",
            "",
            "| Rank | Feature | Importance |",
            "|--:|:--|--:|",
        ]
    )

    for rank, (_, row) in enumerate(feature_importance.head(10).iterrows(), start=1):
        lines.append(f"| {rank} | {row['Feature']} | {row['Importance']:.3f} |")

    lines.extend(
        [
            "",
            "## Figures",
            "",
            "- `docs/figures/fig01-survival-by-sex-class.png`",
            "- `docs/figures/fig02-missingness-profile.png`",
            "- `docs/figures/fig03-submission-history.png`",
            "- `docs/figures/fig04-cross-validated-model-comparison.png`",
            "- `docs/figures/fig05-feature-importance.png`",
            "- `docs/figures/fig06-confusion-matrix.png`",
        ]
    )

    (DOCS_DIR / "Results_Snapshot.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """Run the full analysis workflow and print the key results."""

    ensure_output_dirs()
    train_raw, test_raw = load_data()
    context = fit_feature_context(train_raw)
    train = engineer_features(train_raw, context)
    test = engineer_features(test_raw, context)

    X = train[FEATURES]
    y = train[TARGET]
    X_test = test[FEATURES]

    results, ensemble_predictions = evaluate_models(X, y)
    ensemble = build_ensemble()
    submission = write_submission(ensemble, X, y, X_test, test_raw)

    plot_survival_by_sex_class(train_raw)
    plot_missingness(train_raw)
    plot_submission_history()
    plot_model_comparison(results)
    feature_importance = plot_feature_importance(X, y)
    matrix = plot_confusion_matrix(y, ensemble_predictions)

    write_results_snapshot(
        train=train_raw,
        test=test_raw,
        results=results,
        matrix=matrix,
        feature_importance=feature_importance,
        submission=submission,
        ensemble_predictions=ensemble_predictions,
    )

    print("Titanic survival classification workflow")
    print(f"Training rows: {len(train_raw):,} | Test rows: {len(test_raw):,}")
    print(f"Training survival rate: {train_raw[TARGET].mean():.1%}")
    print("\nCross-validated model comparison:")
    print(
        results.to_string(
            index=False,
            formatters={
                "AccuracyMean": "{:.3f}".format,
                "AccuracySD": "{:.3f}".format,
                "BalancedAccuracyMean": "{:.3f}".format,
                "BalancedAccuracySD": "{:.3f}".format,
            },
        )
    )
    print(f"\nOut-of-fold ensemble confusion matrix: {matrix.tolist()}")
    print(f"Predicted survival rate in test file: {submission['Survived'].mean():.1%}")
    print("Best recorded Kaggle public leaderboard score: 0.79186")
    print(f"Figures written to: {FIGURE_DIR.relative_to(BASE_DIR)}")
    print(f"Submission written to: {(OUTPUT_DIR / 'titanic_submission.csv').relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
