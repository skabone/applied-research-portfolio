# Python Machine Learning Methods Showcase

**Author:** Mintay Misgano, PhD
**Year:** 2022
**Tools:** Python, scikit-learn, pandas, numpy, matplotlib
**Dataset:** ISLR College Data (N = 777)

---

## Abstract

This project presents a comparative demonstration of eight core machine learning methods applied to the ISLR College dataset. The goal is not to solve a single business problem, but to show how a consistent workflow can be used to compare supervised and unsupervised methods on the same structured dataset. The collection includes linear regression, logistic regression, decision trees, support vector machines, random forest, k-means clustering, Gaussian mixture modeling, and principal components analysis. Classification models were compared with 5-fold stratified cross-validation, while clustering and PCA were used to examine structure in the feature space.

---

## 1. Project Context

This project was developed from graduate-level coursework in Python and machine learning. Rather than leaving the work distributed across weekly labs, the methods were consolidated into one script and one report so the collection could function as a compact technical showcase.

The project addresses four practical questions:

1. Which classification methods perform best on this binary tabular prediction problem?
2. What do the major tradeoffs look like across interpretability and predictive performance?
3. Can unsupervised clustering recover meaningful structure without using the target label?
4. How much dimensionality reduction is possible before most of the variance is lost?

---

## 2. Dataset

The ISLR College dataset contains data on 777 U.S. colleges and universities. It includes institutional features such as enrollment, tuition, expenditures, faculty credentials, and graduation rate, alongside a binary institutional type outcome: private versus public.

This is a useful teaching dataset for comparative machine learning because it is structured, moderately imbalanced, and rich enough to support both predictive and exploratory methods.

---

## 3. Methods

### 3.1 Supervised Methods

- Linear regression for graduation-rate prediction
- Logistic regression for binary classification
- Decision tree classification
- Support vector machine with RBF kernel
- Random forest ensemble

### 3.2 Unsupervised Methods

- k-means clustering
- Gaussian mixture modeling
- Principal components analysis

### 3.3 Evaluation Approach

All classification models were compared using 5-fold stratified cross-validation so that method-to-method performance estimates were based on the same class balance and evaluation procedure.

---

## 4. Main Results

### 4.1 Classification

Random forest produced the strongest classification accuracy in this workflow. Logistic regression remained competitive while offering much more straightforward interpretation. Decision trees were the easiest to explain visually, though they gave up some predictive performance relative to ensemble methods.

### 4.2 Clustering

k-means and Gaussian mixture modeling both recovered meaningful structure in the dataset without relying on the target label directly. This makes them useful examples of how unsupervised methods can complement classification work.

### 4.3 Dimensionality Reduction

PCA showed that a smaller number of components could retain most of the variance in the selected features. This section functions mainly as a demonstration of how dimensionality reduction can simplify a feature set before later modeling or interpretation.

---

## 5. Interpretation

The main takeaway is not that one algorithm is universally best, but that different methods answer different analytical needs. Random forest offered the best accuracy in this comparison, while logistic regression and decision trees remained more interpretable. The unsupervised methods added value by revealing dataset structure that would not be visible from classification alone.

Because this is a comparative methods collection built on a teaching dataset, the project is most useful as evidence of technical breadth, evaluation discipline, and implementation fluency across core Python ML workflows.

---

## 6. Limitations

**Teaching dataset:** The ISLR College data is well suited for demonstration, but it is not a real production case.

**Single dataset:** Results reflect one structured classification problem and should not be generalized too broadly across domains.

**Approximate reporting:** The emphasis is on comparative patterns and workflow rather than on exhaustive hyperparameter tuning or benchmark optimization.

---

## 7. Conclusion

This project demonstrates a broad but organized command of foundational Python machine learning methods. By applying multiple techniques to the same dataset under a shared evaluation framework, it shows not just how to run individual models, but how to compare, interpret, and position them within a larger analytical workflow.
