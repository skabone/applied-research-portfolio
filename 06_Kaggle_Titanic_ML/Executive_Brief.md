# Kaggle Titanic ML — Executive Brief
**Competition:** Kaggle Titanic: Machine Learning from Disaster | **Analyst:** Mintay Misgano | **Best Score:** 0.79186 (public leaderboard, top ~22%)

---

## The Business Problem

Binary classification — predicting a yes/no outcome for each individual — is one of the most common and consequential tasks in people analytics. Predicting employee attrition, identifying flight risk, flagging candidates for outreach, scoring engagement risk: all of these are binary classification problems. The Kaggle Titanic competition provides a well-studied benchmark for developing and benchmarking exactly these methods. Using demographic and ticket-level features, the task is to predict whether each of 418 held-out passengers survived the Titanic disaster. The real deliverable is not a historical curiosity — it is a practiced, audited ML pipeline ready to apply to workforce data.

---

## Approach

- Applied a complete classification pipeline: feature engineering → individual model training → cross-validated evaluation → voting ensemble → submission
- **Feature engineering:** Extracted passenger titles from names (used for age imputation by title/class subgroup), created family size and solo-traveler flags, log-transformed right-skewed fares, flagged cabin availability, and encoded all categorical variables
- **Individual classifiers trained and evaluated via 5-fold stratified CV:** Logistic Regression, Gaussian Naive Bayes, Decision Tree, Random Forest, Gradient Boosting
- **Voting ensemble (5 models):** Hard voting across all five classifiers; majority vote determines final prediction — more robust than any individual model
- Iterated through multiple submission rounds, improving from 76.5% (single Decision Tree) to 79.19% (tuned 5-model ensemble)
- **Tools:** Python, scikit-learn, pandas, numpy

---

## Key Findings

- **Ensemble voting consistently outperforms any single model.** The 5-model hard-voting ensemble achieved 79.19% Kaggle accuracy vs. 76.5% for the best single classifier, demonstrating that model diversity reduces prediction error even when individual models are not dramatically different in performance.
- **The most predictive features are sex, title (as a proxy for social class/age interaction), ticket class, and age band.** Together these four features capture the hierarchical evacuation dynamics of the disaster — women and children first, first-class passengers with closer cabin access to lifeboats.
- **Family size has a non-linear relationship with survival.** Solo travelers and very large families (5+) had lower survival rates than passengers with 2–4 family members, suggesting a "group coordination" effect in emergency evacuation.
- **Iterative submission refinement matters.** Moving from a single Decision Tree to an ensemble across four submission iterations improved leaderboard score by 2.7 percentage points — a meaningful margin in competition and a demonstration of disciplined model development.

---

## Recommendations

1. **Apply this ensemble pipeline architecture to attrition prediction.** The same five-classifier voting ensemble used here maps directly onto a voluntary attrition risk model — substituting Titanic survival with "employee left within 12 months" and ticket features with engagement survey scores, tenure, compensation band, and manager metrics.
2. **Invest in feature engineering before model tuning.** The largest accuracy gains in this project came from feature construction (title extraction, family size, age-by-class imputation), not from hyperparameter tuning. This is a consistent finding in applied ML: meaningful features matter more than marginal model improvements.
3. **Use cross-validation, not train-test split alone, for model selection.** Stratified 5-fold CV provides more stable estimates of out-of-sample performance than a single holdout split, particularly when class imbalance is present (as it is in both Titanic survival and most attrition datasets).

---

## Impact

Achieving 79.19% accuracy on a globally benchmarked classification competition demonstrates practical command of the full supervised ML pipeline: data cleaning, feature engineering, model selection, cross-validated evaluation, and ensemble construction. The same pipeline has been applied to workforce prediction in [Project 01 — IBM HR Attrition Analysis](../../01_IBM_HR_Attrition_Analysis/), where the ensemble approach achieved AUC = 0.934.

---

*Analysis by Mintay Misgano | Tools: Python (scikit-learn, pandas, numpy) | Competition: Kaggle Titanic | Score: 0.79186 (public leaderboard)*
