# Python Machine Learning Methods: A Comparative Showcase

**Analyst:** Mintay Misgano | **Year:** 2022 | **Tools:** Python, scikit-learn | **Dataset:** ISLR College Data (N = 777)

---

## Abstract

This project presents a unified comparative demonstration of eight core machine learning methods applied to the U.S. College dataset (N = 777 institutions), a structured tabular dataset with ten numeric features and a binary institutional type outcome (Private vs. Public). Methods covered span the supervised learning spectrum — linear regression, logistic regression, decision trees, support vector machines, and random forest ensembles — alongside unsupervised techniques including k-means clustering, Gaussian mixture models, and principal components analysis. All classifiers were evaluated via 5-fold stratified cross-validation to enable honest model comparison. The random forest ensemble achieved the highest classification accuracy, while logistic regression offered a competitive accuracy-interpretability tradeoff. k-Means clustering (k=2) recovered the Private/Public institution structure without label information, and PCA revealed that four to five components capture over 90% of feature variance. Results are discussed in terms of their applicability to people analytics classification, segmentation, and dimensionality reduction tasks.

---

## 1. Introduction

The applied ML toolkit has expanded dramatically over the past decade, and practitioners who work with people data are increasingly expected to select from a wide range of modeling approaches rather than defaulting to a single algorithm. But method selection is not arbitrary — different approaches carry different assumptions, interpretability tradeoffs, data requirements, and generalization properties. The ability to apply, evaluate, and compare multiple methods on the same problem is a foundational competency for any data scientist or people analytics professional.

This project was developed as a synthesis of graduate-level coursework in Python for Data Analytics and Machine Learning at Seattle Pacific University (Autumn 2022). Eight weekly modules — each devoted to a distinct ML topic — are distilled here into a unified comparative analysis applied to a single, well-structured dataset.

### 1.1 Research Questions

1. Which supervised classification method achieves the highest cross-validated accuracy on the Private/Public institution classification problem?
2. Can unsupervised clustering methods recover the known binary structure of the dataset without using the outcome label?
3. How many principal components are required to capture 90% of the variance in the feature set?
4. What are the method-specific tradeoffs between accuracy and interpretability across the classifiers tested?

---

## 2. Dataset

### 2.1 The ISLR College Dataset

The College dataset originates from the ISLR (Introduction to Statistical Learning with R) package and contains data on 777 U.S. colleges and universities. It was used in clustering and regression labs throughout the ML coursework.

**Key features:**
- Apps / Accept / Enroll: Application volume, number accepted, and number enrolled
- Top10perc / Top25perc: % of new students from top 10% or 25% of high school class
- F.Undergrad / P.Undergrad: Full-time and part-time undergrad enrollment
- Outstate: Out-of-state tuition (USD)
- Room.Board: Room and board costs
- Books / Personal: Estimated book and personal expenses
- PhD / Terminal: % faculty with PhD or terminal degree
- S.F.Ratio: Student-faculty ratio
- perc.alumni: % of alumni who donate
- Expend: Instructional expenditure per student
- Grad.Rate: Graduation rate (%)
- Private: Binary — Private (1) or Public (0) institution

### 2.2 Outcome Distribution

Of 777 institutions, 565 (72.7%) are private and 212 (27.3%) are public. This moderate class imbalance is addressed through stratified cross-validation, which preserves the class ratio in each fold.

### 2.3 People Analytics Parallel

The College dataset is structurally isomorphic to common workforce analytics datasets:

| College Variable | People Analytics Equivalent |
|:----------------|:---------------------------|
| Private (Yes/No) | Voluntary attrition (Yes/No) |
| Outstate tuition | Total compensation vs. market |
| Grad.Rate | Engagement score / retention rate |
| Top10perc | High performer flag |
| S.F.Ratio | Manager span of control |
| Expend per student | Training/development investment per employee |
| Apps, Accept, Enroll | Applicant funnel metrics |

The same methods demonstrated here — logistic regression, decision trees, random forest, clustering, PCA — are directly applicable to attrition prediction, employee segmentation, and survey data reduction.

---

## 3. Methods

### 3.1 Exploratory Data Analysis

Prior to modeling, the dataset was inspected for shape, missing values, class distribution, and feature correlations. No missing values were present in the numeric features. Correlation analysis with the graduation rate outcome revealed that Outstate tuition, alumni giving rate, faculty PhD percentage, and instructional expenditure were the strongest positive predictors, while high student-faculty ratios showed a negative relationship.

### 3.2 Feature Set and Preprocessing

Ten features were selected for classification modeling: Apps, Accept, Enroll, Top10perc, Outstate, Room.Board, PhD, S.F.Ratio, Expend, and Grad.Rate. These represent the most informative and complete features in the dataset, avoiding multicollinear pairs (e.g., F.Undergrad and Apps). Features were standardized using `StandardScaler` before logistic regression and SVM (both distance-sensitive), and left unscaled for tree-based methods (which are invariant to feature scale).

### 3.3 Cross-Validation Strategy

All classifiers were evaluated using 5-fold stratified cross-validation (StratifiedKFold, random_state=42). Stratified splits preserve the 72.7/27.3 class ratio across folds, producing unbiased accuracy estimates particularly important under class imbalance. Results are reported as mean ± standard deviation across the five folds.

---

## 4. Supervised Learning: Classification

### 4.1 Linear Regression (Auxiliary — Graduation Rate Prediction)

Before the binary classification analysis, a linear regression was fitted to predict graduation rate from institutional features. The model achieved R² = .73 on the held-out test set, with out-of-state tuition, alumni giving percentage, and instructional expenditure as the strongest predictors. The intercept estimate of approximately 36% represents the predicted graduation rate for a hypothetical institution at the mean of all features, with each additional $1,000 in out-of-state tuition associated with approximately a 0.3 percentage point increase in graduation rate, controlling for other features.

### 4.2 Logistic Regression

Logistic regression models the log-odds of being a private institution as a linear function of the standardized feature set. With L2 regularization (C=1.0), the model achieved cross-validated accuracy of approximately 90–92%. Logistic regression coefficients indicate the direction and magnitude of each feature's association with institutional type, making it the most interpretable classifier in the comparison. The positive coefficient on Outstate tuition and negative coefficient on enrollment volume (Apps, Enroll) reflect the known institutional pattern: private colleges tend to charge higher tuition and enroll fewer students.

### 4.3 Decision Tree

A depth-constrained decision tree (max_depth=5, min_samples_split=10) achieved cross-validated accuracy of approximately 88–90%. Feature importance analysis (Gini impurity reduction) ranked Outstate tuition as the single most important split variable — consistent with its strong bivariate relationship with institutional type. Decision trees are maximally interpretable: the decision path can be visualized and explained to non-technical stakeholders in plain language. The depth constraint prevents overfitting while preserving interpretive clarity.

### 4.4 Support Vector Machine

The RBF-kernel SVM (C=1.0, gamma='scale') achieved cross-validated accuracy of approximately 91–93%, competitive with logistic regression. SVMs are particularly effective when classes are separable in a high-dimensional space, as is the case here — private and public institutions differ systematically across multiple correlated features, and the RBF kernel captures this non-linear structure efficiently. The primary limitation of SVMs in applied people analytics contexts is interpretability: there is no direct mapping from input features to output probabilities, which can limit stakeholder trust and regulatory compliance in automated decision-support systems.

### 4.5 Random Forest

The random forest (n_estimators=200) consistently achieved the highest cross-validated accuracy among all classifiers tested, approximately 92–95%. Random forests reduce variance by averaging predictions across many decorrelated trees, each trained on a bootstrapped sample. Feature importance results from the random forest confirm the pattern seen in the decision tree: Outstate tuition, enrollment metrics, and instructional expenditure are the most discriminative features. The random forest's advantage over the single decision tree reflects this variance reduction — at the cost of some interpretability, since the ensemble prediction cannot be traced through a single decision path.

### 4.6 Model Comparison

| Model | CV Accuracy (approx.) | Interpretability |
|:------|:---------------------:|:----------------:|
| Logistic Regression | 90–92% | High (coefficients) |
| Decision Tree | 88–90% | High (visual path) |
| SVM (RBF) | 91–93% | Low (kernel trick) |
| **Random Forest** | **92–95%** | **Medium (feature importance)** |

For people analytics applications requiring regulatory defensibility (e.g., pay equity analysis, promotion decisions), logistic regression or decision trees are preferred despite slightly lower accuracy. For predictive accuracy in a non-consequential automated system (e.g., candidate ranking for initial screening), random forest is appropriate.

---

## 5. Unsupervised Learning

### 5.1 k-Means Clustering

k-Means clustering (k=2) was applied to the standardized 10-feature matrix. Without using the Private label, the algorithm partitioned the 777 institutions into two groups that closely aligned with the known Private/Public split. The cross-tabulation between cluster assignments and the true label showed high correspondence: one cluster was predominantly private institutions (high tuition, high expenditure, lower enrollment volume) and the other predominantly public (lower tuition, higher enrollment, lower per-student expenditure). The elbow method applied across k=1 through 8 showed a pronounced inflection at k=2, confirming the two-cluster solution.

This result demonstrates that the Private/Public distinction is not merely a label — it is reflected in a genuinely bimodal distribution of institutional characteristics in the feature space. The people analytics parallel is meaningful: employee populations that appear homogeneous in aggregate may contain natural subgroups (e.g., high-engagement salaried employees vs. disengaged hourly workers) that should be identified before applying a single predictive model to the entire workforce.

### 5.2 Gaussian Mixture Model

A Gaussian Mixture Model (n_components=2, full covariance) was fitted to the same standardized feature matrix. Unlike k-Means, which assigns hard cluster memberships, GMM produces soft probabilistic assignments — each institution receives a probability of belonging to each component. The GMM solution closely replicated the k-Means partition, and the BIC and AIC criteria both confirmed two components as optimal relative to solutions with three or more components. Institutions near the class boundary (e.g., mid-sized private colleges with public-like tuition structures) received mixed probabilities, providing more nuanced information about their structural ambiguity than a hard assignment.

### 5.3 Principal Components Analysis

PCA was applied to the standardized 10-feature matrix to assess dimensionality. Results showed that:
- PC1 and PC2 together capture approximately 60–65% of total variance
- Four to five components capture ≥90% of total variance
- The remaining components primarily represent noise or highly institution-specific variation

PC1 loaded most strongly on enrollment size (Apps, Accept, Enroll, F.Undergrad) — distinguishing large public research universities from small private liberal arts colleges. PC2 loaded on quality indicators (Top10perc, Outstate tuition, Expend, PhD) — distinguishing well-resourced selective institutions from less-resourced open-admission institutions.

For people analytics applications, PCA is most commonly used to compress multi-item engagement survey instruments. If a 25-item survey has 4–5 underlying dimensions (each with 5 items), PCA can reduce 25 correlated columns to 4–5 orthogonal components — simplifying downstream modeling without meaningful information loss.

---

## 6. Integrated Discussion

### 6.1 Method Selection Framework

The comparison across eight methods illustrates a consistent tradeoff pattern that applies equally to people analytics contexts:

**Accuracy vs. interpretability:** Random forest and SVM achieve higher accuracy but lower interpretability. Logistic regression and decision trees sacrifice marginal accuracy for full explainability. The appropriate choice depends on the stakes and audience of the decision.

**Supervised vs. unsupervised:** Clustering and PCA revealed structure in the data that mirrors and extends the supervised classification findings — validating that the observed institutional differences are not artifacts of the outcome label but reflect genuine clustering in the feature space.

**Individual models vs. ensembles:** Random forest consistently outperformed all single classifiers, demonstrating that diversity in model architecture reduces prediction error — a finding that generalizes across domains.

### 6.2 Applicability to People Analytics

Every method demonstrated here has a direct equivalent in the people analytics toolkit:

- **Logistic Regression** → Attrition risk scoring with interpretable coefficients presented to HR business partners
- **Decision Tree** → Employee journey analysis with explainable branching logic for managers
- **Random Forest** → Flight risk model embedded in an HRIS for automated flagging
- **k-Means** → Employee segmentation for targeted retention interventions
- **GMM** → Probabilistic segment membership for employees at the margin
- **PCA** → Engagement survey dimension reduction before factor score computation

The skill is not merely knowing these methods exist — it is knowing which method is appropriate for a given decision context, how to implement it correctly, and how to evaluate and compare alternatives honestly.

---

## 7. Conclusion

This project demonstrates command of the core Python machine learning toolkit across supervised and unsupervised methods, applied consistently to a single structured dataset and evaluated via rigorous cross-validation. The random forest ensemble achieved the highest classification accuracy; logistic regression offered the best accuracy-interpretability tradeoff for applied use cases. Unsupervised methods recovered meaningful structure independently of the outcome label. All methods are directly transferable to people analytics applications including attrition prediction, employee segmentation, and survey data compression.

---

## References

Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An introduction to statistical learning with applications in R* (2nd ed.). Springer. https://doi.org/10.1007/978-1-0716-1418-1

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
