# Job Change Prediction with CRISP-DM

**Author:** Mintay Misgano, PhD
**Year:** 2022
**Tools:** Python, pandas, numpy, scikit-learn
**Dataset:** Kaggle HR Analytics: Job Change of Data Scientists (N = 19,158)

---

## Abstract

This project applies the CRISP-DM framework to a public classification problem involving job-change intent among data science trainees. The workflow covers business understanding, data preparation, feature engineering, model comparison, and evaluation. Logistic regression, decision tree, random forest, and gradient boosting models were compared using stratified cross-validation. Gradient boosting produced the strongest overall performance, and ROC-AUC served as the main evaluation metric because the target outcome was imbalanced.

---

## 1. Project Context

The goal of the project was to build a compact but complete data-mining workflow around a realistic binary classification problem. Rather than focusing only on final model performance, the project was structured to show how CRISP-DM can guide the full progression from problem framing to model evaluation and deployment-style interpretation.

This makes the project especially useful as a coursework portfolio piece: it demonstrates process as well as results.

---

## 2. Dataset

The dataset comes from Kaggle's HR Analytics competition on job change among data scientists. It contains 19,158 observations with variables related to geography, education, experience, employer context, and training participation.

The target variable indicates whether a candidate is looking for a new job. The positive class is a minority class, which means that accuracy alone would not be a sufficient evaluation metric.

---

## 3. CRISP-DM Workflow

### 3.1 Business Understanding

The project defines a practical binary prediction problem and sets success criteria with ROC-AUC as a key metric.

### 3.2 Data Understanding

Exploration focused on class balance, missingness patterns, and variable structure across categorical and ordinal fields.

### 3.3 Data Preparation

Preparation steps included:

- mode imputation for categorical fields
- ordinal recoding for experience and company-size variables
- binary feature engineering
- limited transformation of skewed variables
- encoding for model-ready input

### 3.4 Modeling

Four models were compared:

- Logistic regression
- Decision tree
- Random forest
- Gradient boosting

### 3.5 Evaluation

Models were evaluated with stratified 5-fold cross-validation using accuracy and ROC-AUC, with ROC-AUC emphasized because of class imbalance.

---

## 4. Main Results

Gradient boosting performed best in this workflow, followed by random forest. The results reinforce a familiar pattern in tabular classification problems: ensemble methods often outperform simpler baselines when the feature space contains nonlinear structure and mixed categorical relationships.

The strongest predictors included city development index, experience-related variables, and company-context features. These variables suggest that mobility patterns in the dataset are shaped partly by labor-market context rather than by training participation alone.

---

## 5. Interpretation

The main contribution of this project is the structured use of CRISP-DM. The work shows not just model fitting, but a full applied workflow with explicit preparation, metric choice, and comparative evaluation. It also demonstrates why ROC-AUC is often more informative than raw accuracy for imbalanced classification tasks.

Because the dataset is public and benchmark-oriented, the project is best interpreted as a demonstration of data-mining workflow, feature preparation, and model comparison rather than as a claim about deployment readiness in a live organizational setting.

---

## 6. Limitations

**Public benchmark data:** The project uses a Kaggle dataset rather than a live operational dataset.

**Limited feature context:** Some predictors may function as proxies for broader labor-market conditions rather than directly interpretable causal drivers.

**Comparative scope:** The analysis emphasizes a clear CRISP-DM workflow and model comparison rather than exhaustive tuning.

---

## 7. Conclusion

This project demonstrates a full CRISP-DM data-mining workflow on a realistic classification problem. It shows practical skill in preprocessing, model comparison, metric selection, and interpretation, with enough structure to serve as a compact example of end-to-end applied machine learning.
