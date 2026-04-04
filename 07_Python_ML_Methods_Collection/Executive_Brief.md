# Python ML Methods Collection — Executive Brief
**Domain:** Supervised & Unsupervised Machine Learning | **Analyst:** Mintay Misgano | **Year:** 2022

---

## The Business Problem

People analytics teams are increasingly expected to apply machine learning — not just descriptive statistics — to workforce questions. But "using ML" encompasses a wide range of methods with different strengths, assumptions, and interpretability tradeoffs. This project demonstrates command of the full breadth of the core ML toolkit: from linear models and decision trees to clustering, dimensionality reduction, and ensemble methods. Understanding when to use each method — and how to evaluate and compare them honestly — is the foundational competency underlying any real-world analytics application.

---

## Approach

- Built a unified ML methods showcase applying 8 distinct techniques to the U.S. College Data dataset (N = 777 institutions) — a structured tabular dataset with mixed numeric features and a binary outcome (Private vs. Public institution), directly analogous to HR classification problems
- Each method is implemented cleanly, evaluated via 5-fold stratified cross-validation, and compared in a model summary table
- **Methods demonstrated:** EDA → Linear Regression (OLS) → Logistic Regression → Decision Tree → Support Vector Machine (RBF) → k-Means Clustering + GMM → PCA → Random Forest ensemble
- All methods sourced from graduate-level coursework (SPU ISM, Autumn 2022) and distilled into a single reproducible script
- **Tools:** Python, scikit-learn, pandas, numpy, matplotlib

---

## Key Findings

- **Random Forest consistently outperforms all single classifiers** on cross-validated accuracy for the Private/Public classification task — demonstrating that ensemble diversity reduces prediction error beyond any individual model's performance
- **Logistic Regression achieves competitive accuracy** (~90%+ CV) with full coefficient interpretability — the preferred choice when stakeholders need to understand *why* a prediction was made, not just what it is
- **k-Means clustering (k=2) recovers the Private/Public split** without using the label — validating that the institution profiles are naturally separated in feature space. The elbow plot confirms k=2 as the optimal solution
- **PCA reveals that 4–5 components capture >90% of variance** in 10 features — useful for compressing multi-item survey instruments into a manageable set of dimensions before supervised modeling
- **Decision Tree provides the most interpretable model** at the cost of some accuracy — the top split is almost universally on Outstate tuition, reflecting its status as the strongest single predictor of institution type

---

## Recommendations

1. **Match method to the decision context.** When the audience is an HR business partner or executive, logistic regression and decision trees are preferred — their outputs are explainable in plain language. When the goal is maximum predictive accuracy in an automated system, random forest or gradient boosting is appropriate.
2. **Use clustering before segmented modeling.** k-Means or GMM analysis of the employee population can reveal meaningful subgroups (high-performer clusters, flight-risk segments) that should be modeled separately rather than pooled — a step often skipped in people analytics workflows.
3. **Apply PCA when engagement surveys have many redundant items.** Survey instruments with 20+ items often have significant intercorrelation. PCA reduces these to 4–6 meaningful dimensions, simplifying downstream modeling without losing explanatory power.

---

## Impact

Demonstrated command of 8 distinct ML methods — supervised (regression, logistic regression, decision tree, SVM, random forest) and unsupervised (k-means, GMM, PCA) — on a real structured dataset. The unified showcase makes method tradeoffs directly comparable and establishes a reusable template for applying these techniques to workforce data including attrition prediction, employee segmentation, and survey dimension reduction.

---

*Analysis by Mintay Misgano | Tools: Python (scikit-learn, pandas, numpy) | Data: ISLR College dataset (N=777) | Course: Programming for Data Analytics: Python & ML, SPU (Autumn 2022)*
