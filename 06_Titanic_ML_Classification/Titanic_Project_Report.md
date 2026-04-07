# Titanic ML Classification — Project Report

**Author:** Mintay Misgano, PhD | **Year:** 2022 | **Tools:** Python, scikit-learn | **Best Kaggle Score:** 0.79186 (public leaderboard)

---

## Abstract

This project documents a machine-learning classification pipeline developed for the Kaggle Titanic competition, which challenges competitors to predict passenger survival using demographic and ticket-level features. The workflow proceeded through feature engineering, multi-model training, cross-validated evaluation, and ensemble construction via hard voting across five classifiers (Logistic Regression, Gaussian Naive Bayes, Decision Tree, Random Forest, and Gradient Boosting). The best submission achieved 79.19% accuracy on the Kaggle public leaderboard, improving on the initial single-model baseline. As a portfolio project, its value lies in demonstrating a complete supervised-learning workflow on structured tabular data rather than in the competition score alone.

---

## 1. Introduction

The Kaggle Titanic competition is one of the most widely used benchmarks in applied machine learning. It remains useful because it is a manageable binary-classification problem with a realistic mix of numeric and categorical variables, missing-data decisions, and clear evaluation through held-out competition scoring.

This project was completed as part of graduate coursework in data mining. The analysis iterated across four submission rounds, allowing the workflow to show how feature engineering, model comparison, and ensemble construction contributed to incremental performance gains.

---

## 2. Dataset

### 2.1 Training Data

The training dataset contains 891 passenger records with 12 raw features:

| Feature       | Type        | Description |
|:--------------|:------------|:------------|
| PassengerId   | Integer     | Unique identifier |
| Survived      | Binary      | Outcome variable (0 = No, 1 = Yes) |
| Pclass        | Ordinal     | Passenger class (1 = first, 2 = second, 3 = third) |
| Name          | String      | Full name including title |
| Sex           | Categorical | Male / Female |
| Age           | Continuous  | Age in years (177 missing values) |
| SibSp         | Integer     | Number of siblings/spouses aboard |
| Parch         | Integer     | Number of parents/children aboard |
| Ticket        | String      | Ticket number |
| Fare          | Continuous  | Passenger fare paid |
| Cabin         | String      | Cabin number (687 missing — ~77%) |
| Embarked      | Categorical | Port of embarkation (S/C/Q; 2 missing values) |

The overall survival rate in the training set is 38.4%.

### 2.2 Class Imbalance

The training set is moderately imbalanced: 549 passengers (61.6%) did not survive, versus 342 (38.4%) who survived. This imbalance is less severe than typical attrition datasets but was nonetheless addressed through stratified cross-validation, which preserves the class ratio in each fold and produces unbiased accuracy estimates.

### 2.3 Missing Data

Missing data is concentrated in two variables: Age (20% missing) and Cabin (77% missing). Embarked has two missing values. The missing data patterns required distinct strategies for each variable, described in Section 3.

---

## 3. Feature Engineering

Feature engineering produced larger performance gains than any single model choice or hyperparameter adjustment. The following features were constructed:

### 3.1 Title Extraction

Passenger names follow the format "Surname, Title. First Name(s)". Titles were extracted via regex and consolidated into five groups: Mr, Mrs, Miss, Master, and Rare (which includes Dr, Rev, Col, Major, Countess, Jonkheer, and other infrequent titles). Title is a strong proxy for the interaction of sex, age, and social class — variables that jointly determined evacuation priority.

### 3.2 Age Imputation

Rather than imputing age from the global median (which ignores the substantial variation in age by sex, class, and social role), missing ages were imputed from the median age within each Title × Pclass subgroup. For example, a "Miss" in third class was assigned a different median age than a "Mrs" in first class. This produces more contextually accurate imputations while remaining simple and non-leaky.

### 3.3 Family Size and Isolation Flag

SibSp (siblings/spouses) and Parch (parents/children) were combined into a single FamilySize variable (= SibSp + Parch + 1, counting the passenger). An IsAlone binary flag identifies passengers traveling without any family member. Both features capture the group coordination dynamic during evacuation: passengers traveling with a small family may have had better survival prospects than solo travelers, while very large families faced coordination challenges.

### 3.4 Fare Log-Transformation

Raw fares are right-skewed — a small number of passengers paid very high first-class fares. Log-transforming the fare variable (log1p) reduces skew and prevents high-fare outliers from disproportionately influencing linear and distance-based models.

### 3.5 Cabin Availability

Rather than attempting to impute 77% missing cabin values, a binary HasCabin flag was created (1 = cabin recorded, 0 = unknown). Cabin availability is a proxy for first-class booking confirmation and physical proximity to lifeboats — a meaningful signal despite being imprecise.

### 3.6 Age Bands

Continuous age was also discretized into five ordinal bands (child: 0–12, teen: 13–18, adult: 19–35, middle-aged: 36–60, elderly: 60+) to allow tree-based models to capture non-linear age effects without relying solely on the continuous variable.

---

## 4. Modeling

### 4.1 Classifier Descriptions

Five classifiers were trained and evaluated:

**Logistic Regression:** A linear classifier modeling the log-odds of survival as a linear function of features. Strong baseline for linearly separable problems; interpretable coefficients. Required feature scaling (StandardScaler) for stable convergence.

**Gaussian Naive Bayes:** Probabilistic classifier assuming feature independence and Gaussian-distributed continuous variables. Fast and effective with small samples; performs surprisingly well despite its independence assumption.

**Decision Tree:** Non-linear classifier partitioning the feature space into rectangular regions. Prone to overfitting without constraints; depth and minimum sample size were regularized (max_depth=5, min_samples_split=10).

**Random Forest:** Ensemble of decorrelated decision trees trained on bootstrapped samples. Reduces Decision Tree variance through averaging; less sensitive to hyperparameter choices than single trees. n_estimators=200, max_depth=6.

**Gradient Boosting:** Sequential ensemble where each tree is fit to the residuals of the previous ensemble. Typically the highest-performing individual model on tabular data. n_estimators=200, max_depth=4, learning_rate=0.05.

### 4.2 Cross-Validated Evaluation

All models were evaluated using 5-fold stratified cross-validation, which partitions the training data into five folds while preserving the survival class ratio in each fold. Results:

| Model                | CV Accuracy |
|:---------------------|:-----------:|
| Logistic Regression  | ~78.0%      |
| Naive Bayes          | ~76.5%      |
| Decision Tree        | ~76.5%      |
| Random Forest        | ~78.5%      |
| Gradient Boosting    | ~79.0%      |
| **Voting Ensemble**  | **~79.5%**  |

### 4.3 Voting Ensemble

A hard-voting ensemble aggregated predictions from all five classifiers. In hard voting, each model casts a single vote for each passenger; the class receiving the majority of votes (≥3 of 5) is the final prediction. Hard voting is more robust than any individual model when classifiers make independent errors — a condition that approximately holds here, as the five classifiers span different model families (linear, probabilistic, tree-based, and boosted).

The ensemble was fitted on the full 891-observation training set after cross-validation confirmed its advantage over individual models.

---

## 5. Results

### 5.1 Submission History

| Attempt | Method | Kaggle Score |
|:--------|:-------|:------------:|
| 1 | Single Decision Tree (baseline) | 0.76555 |
| 2 | Voting: Random Forest + Naive Bayes + Logistic Regression | 0.77511 |
| 3 | Voting × 5 (first tuning pass) | 0.78947 |
| **4** | **Voting × 5 (tuned feature set)** | **0.79186** |

The progression from 0.765 to 0.792 across four iterations demonstrates the compounding benefit of (1) ensemble construction and (2) feature engineering refinement. The largest single gain — from 0.765 to 0.775 — came from moving from a single Decision Tree to a three-model ensemble. Subsequent gains came from adding more diverse classifiers and refining the feature engineering pipeline.

### 5.2 Feature Importance

Random Forest feature importance scores (Gini impurity reduction) ranked the top predictors as:

1. **Title_enc** — captures sex, age, and social class simultaneously
2. **Sex_enc** — women had dramatically higher survival rates across all classes
3. **Pclass** — first-class passengers had better lifeboat access and shorter evacuation paths
4. **FareLog** — correlated with class; also captures fine-grained within-class variation
5. **Age** / **AgeBand** — children were prioritized in evacuation
6. **FamilySize** / **IsAlone** — group coordination effects

Cabin, Embarked, and SibSp/Parch in isolation ranked lower, though SibSp and Parch contribute meaningfully through the derived FamilySize variable.

---

## 6. Discussion

### 6.1 Ensemble Methods in Applied ML

The performance advantage of the voting ensemble reflects a common principle in applied machine learning: when models make partially different errors, aggregating their predictions can reduce variance and improve stability. The five classifiers used here span different model families — linear, probabilistic, tree-based, and boosted — which helps explain why the ensemble outperformed the initial single-model baseline.

### 6.2 Feature Engineering vs. Model Tuning

The analysis also reinforces a familiar pattern in applied ML: feature engineering can matter more than fine-grained algorithm tuning. The transition from raw variables to engineered features such as titles, family size, transformed fares, and subgroup-based age imputation produced clearer gains than minor hyperparameter adjustments.

---

## 7. Limitations

**External validity:** Titanic survival reflects a single historical event under extraordinary circumstances. The patterns identified (sex, class, age as primary predictors) are historically specific and should not be generalized as universal laws of emergency behavior.

**Public vs. private leaderboard:** The Kaggle public leaderboard score (0.79186) is computed on approximately 50% of the test set. The private leaderboard score — computed on the remaining 50% — may differ due to overfitting to the public test set through repeated submission. Production ML systems require held-out test sets that are not exposed to the analyst during development.

**Feature leakage check:** The Title feature extraction was performed identically on train and test sets using the same label encoder fitted on train, preventing target leakage.

---

## 8. Conclusion

This project demonstrates a complete supervised-learning workflow: raw data preparation, iterative feature engineering, multi-model training, stratified cross-validated evaluation, and ensemble construction. The final five-model hard-voting ensemble achieved 79.19% accuracy on the Kaggle Titanic public leaderboard, improving on the original single-model baseline. The clearest gains came from feature engineering and iterative refinement rather than from any single model alone.

As a portfolio project, its main value is showing a structured and reproducible approach to benchmark tabular classification. It demonstrates practical judgment about feature construction, model comparison, and how to interpret competition results with appropriate modesty.

---

## References

Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. *Annals of Statistics, 29*(5), 1189–1232. https://doi.org/10.1214/aos/1013203451

Kaggle. (2012). *Titanic: Machine learning from disaster*. https://www.kaggle.com/c/titanic

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
