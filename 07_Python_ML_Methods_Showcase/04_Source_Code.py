"""
College Institutional Profile Modeling
======================================

This workflow turns the ISLR College teaching dataset into a compact applied
machine-learning comparison. The goal is not to claim a production deployment
model for colleges; it is to show how supervised and unsupervised methods answer
different questions about the same institutional profile data.

The script is intentionally project-local:
- input data: data/College_Data.csv
- output figures: docs/figures/

Running `python3 04_Source_Code.py` regenerates every figure referenced in the
README, summary, and report.
"""

from pathlib import Path
import warnings

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import adjusted_rand_score, mean_squared_error, r2_score
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "College_Data.csv"
FIG_DIR = ROOT / "docs" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

PALETTE = {
    "blue": "#1f77b4",
    "green": "#2ca02c",
    "orange": "#ff7f0e",
    "red": "#d62728",
    "purple": "#9467bd",
    "gray": "#6b6b6b",
}

plt.rcParams.update({
    "figure.dpi": 120,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.axisbelow": True,
    "font.size": 10,
})


def load_college_data() -> pd.DataFrame:
    """Load and prepare the public College dataset.

    The published source stores `Private` as 1/0 in this repository. The binary
    label is kept explicit so readers can see which target every classification
    and clustering comparison uses.
    """
    df = pd.read_csv(DATA_PATH)
    df["Private_bin"] = df["Private"].astype(int)
    df["Institution_type"] = np.where(df["Private_bin"] == 1, "Private", "Public")
    df["Accept_rate"] = df["Accept"] / df["Apps"]
    df["Yield_rate"] = df["Enroll"] / df["Accept"]
    return df


def plot_private_balance(df: pd.DataFrame) -> None:
    counts = df["Institution_type"].value_counts().reindex(["Private", "Public"])
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    bars = ax.bar(counts.index, counts.values, color=[PALETTE["blue"], PALETTE["orange"]])
    ax.set_title("Institution Type Balance in the College Dataset")
    ax.set_ylabel("Number of institutions")
    ax.set_xlabel("Institution type")
    total = counts.sum()
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 8, f"{int(h)} ({h/total:.1%})",
                ha="center", va="bottom", fontweight="bold")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig01-institution-type-balance.png")
    plt.close(fig)


def graduation_regression(df: pd.DataFrame) -> dict[str, object]:
    """Fit an interpretable OLS-style linear regression for graduation rate.

    This step answers a different question than classification: which public
    institutional features help explain graduation-rate differences? Keeping it
    separate prevents the portfolio from treating every model as a classifier.
    """
    features = [
        "Outstate", "Top10perc", "Expend", "PhD", "S.F.Ratio",
        "perc.alumni", "Private_bin",
    ]
    target = "Grad.Rate"
    data = df[features + [target]].dropna()
    x_train, x_test, y_train, y_test = train_test_split(
        data[features], data[target], test_size=0.20, random_state=42
    )
    model = LinearRegression()
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    r2 = r2_score(y_test, pred)
    rmse = float(np.sqrt(mean_squared_error(y_test, pred)))
    coef = pd.DataFrame({"feature": features, "coefficient": model.coef_})
    coef["abs_coefficient"] = coef["coefficient"].abs()
    coef = coef.sort_values("abs_coefficient", ascending=False)

    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    colors = [PALETTE["green"] if v > 0 else PALETTE["red"] for v in coef["coefficient"]]
    ax.barh(coef["feature"], coef["coefficient"], color=colors)
    ax.axvline(0, color="#333333", lw=1)
    ax.invert_yaxis()
    ax.set_title("Graduation-Rate Regression Coefficients")
    ax.set_xlabel("Coefficient in percentage-point graduation-rate units")
    ax.set_ylabel("Feature")
    for i, v in enumerate(coef["coefficient"]):
        ax.text(v + (0.15 if v >= 0 else -0.15), i, f"{v:.2f}",
                va="center", ha="left" if v >= 0 else "right", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig02-graduation-regression-coefficients.png")
    plt.close(fig)

    return {"r2": r2, "rmse": rmse, "coef": coef}


def classification_models(df: pd.DataFrame) -> dict[str, object]:
    """Compare four classification models with one consistent CV design.

    Stratified 5-fold cross-validation preserves the private/public class mix in
    every fold, making model-to-model accuracy comparisons fairer than one
    arbitrary train/test split.
    """
    features = [
        "Apps", "Accept", "Enroll", "Top10perc", "Outstate",
        "Room.Board", "PhD", "S.F.Ratio", "Expend", "Grad.Rate",
    ]
    x = df[features].copy()
    y = df["Private_bin"].copy()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    models = {
        "Logistic regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000, random_state=42)),
        ]),
        "Decision tree": DecisionTreeClassifier(
            max_depth=5, min_samples_split=10, random_state=42
        ),
        "SVM (RBF kernel)": Pipeline([
            ("scale", StandardScaler()),
            ("model", SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)),
        ]),
        "Random forest": RandomForestClassifier(
            n_estimators=300, min_samples_split=5, random_state=42
        ),
    }

    rows = []
    for name, model in models.items():
        scores = cross_val_score(model, x, y, cv=cv, scoring="accuracy")
        rows.append({"model": name, "cv_accuracy": scores.mean(), "cv_std": scores.std()})
    results = pd.DataFrame(rows).sort_values("cv_accuracy", ascending=False)

    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    ax.barh(results["model"], results["cv_accuracy"], xerr=results["cv_std"],
            color=PALETTE["blue"], alpha=0.9)
    ax.set_xlim(0.80, 0.98)
    ax.invert_yaxis()
    ax.set_title("Private/Public Classification Accuracy by Model")
    ax.set_xlabel("5-fold stratified cross-validated accuracy")
    ax.set_ylabel("Model")
    for i, row in enumerate(results.itertuples(index=False)):
        ax.text(row.cv_accuracy + 0.004, i, f"{row.cv_accuracy:.3f}",
                va="center", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig03-classification-model-comparison.png")
    plt.close(fig)

    rf = RandomForestClassifier(n_estimators=300, min_samples_split=5, random_state=42)
    rf.fit(x, y)
    importance = pd.DataFrame({
        "feature": features,
        "importance": rf.feature_importances_,
    }).sort_values("importance", ascending=False)

    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    top = importance.head(8).sort_values("importance")
    ax.barh(top["feature"], top["importance"], color=PALETTE["green"])
    ax.set_title("Random Forest Feature Importance")
    ax.set_xlabel("Mean decrease in impurity importance")
    ax.set_ylabel("Feature")
    for i, v in enumerate(top["importance"]):
        ax.text(v + 0.005, i, f"{v:.3f}", va="center", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig04-random-forest-feature-importance.png")
    plt.close(fig)

    return {"results": results, "importance": importance}


def clustering_and_pca(df: pd.DataFrame) -> dict[str, object]:
    """Use unsupervised methods to inspect structure without the label.

    k-means and Gaussian mixture modeling ask whether the numeric features split
    into meaningful groups before the private/public label is supplied. PCA then
    shows how much of the feature variation is captured by a smaller number of
    synthetic dimensions.
    """
    features = [
        "Apps", "Accept", "Enroll", "Top10perc", "Outstate",
        "Room.Board", "PhD", "S.F.Ratio", "Expend", "Grad.Rate",
    ]
    x = df[features].copy()
    y = df["Private_bin"].copy()
    x_scaled = StandardScaler().fit_transform(x)

    kmeans = KMeans(n_clusters=2, n_init=20, random_state=42)
    km_labels = kmeans.fit_predict(x_scaled)
    km_ari = adjusted_rand_score(y, km_labels)
    km_table = pd.crosstab(km_labels, y, rownames=["k-means cluster"],
                           colnames=["Private_bin"])

    gmm = GaussianMixture(n_components=2, covariance_type="full", n_init=10,
                          random_state=42)
    gmm_labels = gmm.fit_predict(x_scaled)
    gmm_ari = adjusted_rand_score(y, gmm_labels)

    pca = PCA()
    pca.fit(x_scaled)
    explained = pca.explained_variance_ratio_
    cumulative = np.cumsum(explained)
    n_90 = int(np.argmax(cumulative >= 0.90) + 1)

    pca2 = PCA(n_components=2, random_state=42)
    coords = pca2.fit_transform(x_scaled)
    plot_df = pd.DataFrame({
        "PC1": coords[:, 0],
        "PC2": coords[:, 1],
        "Institution_type": df["Institution_type"],
        "kmeans_cluster": km_labels,
    })

    fig, ax = plt.subplots(figsize=(7.4, 5.4))
    for label, color in [("Private", PALETTE["blue"]), ("Public", PALETTE["orange"])]:
        sub = plot_df[plot_df["Institution_type"] == label]
        ax.scatter(sub["PC1"], sub["PC2"], label=label, s=32, alpha=0.75,
                   color=color, edgecolor="white", linewidth=0.35)
    ax.set_title("PCA Map of College Profiles")
    ax.set_xlabel(f"PC1 ({pca2.explained_variance_ratio_[0]:.1%} variance)")
    ax.set_ylabel(f"PC2 ({pca2.explained_variance_ratio_[1]:.1%} variance)")
    ax.legend(title="Institution type")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig05-pca-profile-map.png")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    components = np.arange(1, len(explained) + 1)
    ax.bar(components, explained, color=PALETTE["purple"], alpha=0.85,
           label="Individual component")
    ax.plot(components, cumulative, marker="o", color=PALETTE["gray"],
            label="Cumulative")
    ax.axhline(0.90, color=PALETTE["red"], linestyle="--", linewidth=1)
    ax.axvline(n_90, color=PALETTE["red"], linestyle="--", linewidth=1)
    ax.set_title("PCA Variance Explained")
    ax.set_xlabel("Principal component")
    ax.set_ylabel("Variance explained")
    ax.set_xticks(components)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig06-pca-variance-explained.png")
    plt.close(fig)

    return {
        "km_ari": km_ari,
        "km_table": km_table,
        "gmm_ari": gmm_ari,
        "gmm_bic": gmm.bic(x_scaled),
        "gmm_aic": gmm.aic(x_scaled),
        "pca_cumulative": cumulative,
        "pca_n_90": n_90,
        "pca2_variance": pca2.explained_variance_ratio_.sum(),
    }


def main() -> None:
    df = load_college_data()
    plot_private_balance(df)
    regression = graduation_regression(df)
    classification = classification_models(df)
    unsup = clustering_and_pca(df)

    private_n = int(df["Private_bin"].sum())
    public_n = int((1 - df["Private_bin"]).sum())

    print("=" * 72)
    print("COLLEGE INSTITUTIONAL PROFILE MODELING - VERIFIED RESULTS")
    print("=" * 72)
    print(f"N institutions: {len(df)}")
    print(f"Private institutions: {private_n} ({private_n/len(df):.1%})")
    print(f"Public institutions:  {public_n} ({public_n/len(df):.1%})")
    print()
    print("Graduation-rate regression")
    print(f"  R-squared: {regression['r2']:.3f}")
    print(f"  RMSE: {regression['rmse']:.2f} graduation-rate points")
    print("  Top coefficients by absolute value:")
    for row in regression["coef"].head(4).itertuples(index=False):
        print(f"    {row.feature}: {row.coefficient:+.3f}")
    print()
    print("Classification model comparison")
    for row in classification["results"].itertuples(index=False):
        print(f"  {row.model}: accuracy={row.cv_accuracy:.3f}, sd={row.cv_std:.3f}")
    print("  Top random forest importances:")
    for row in classification["importance"].head(5).itertuples(index=False):
        print(f"    {row.feature}: {row.importance:.3f}")
    print()
    print("Unsupervised structure")
    print(f"  k-means adjusted Rand index vs Private/Public: {unsup['km_ari']:.3f}")
    print("  k-means cluster table:")
    print(unsup["km_table"].to_string())
    print(f"  GMM adjusted Rand index vs Private/Public: {unsup['gmm_ari']:.3f}")
    print(f"  GMM AIC={unsup['gmm_aic']:.1f}, BIC={unsup['gmm_bic']:.1f}")
    print(f"  PC1 + PC2 variance: {unsup['pca2_variance']:.3f}")
    print(f"  Components needed for >=90% variance: {unsup['pca_n_90']}")
    print()
    print("Figures written:")
    for path in sorted(FIG_DIR.glob("*.png")):
        print(f"  {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
