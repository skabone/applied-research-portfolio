# IBM Employee Attrition Analysis — Project Report
### Predictive Modeling, Exploratory Analysis, and Workforce Interpretation

**Author:** Mintay Misgano, PhD  
**Tools:** Python, scikit-learn, pandas, SMOTE/ADASYN, Logistic Regression, Random Forest, Decision Tree, PCA  
**Dataset:** IBM HR Analytics Employee Attrition benchmark dataset, N = 1,470 employees, 35 variables

---

## Abstract

This project analyzes the IBM HR Analytics Employee Attrition benchmark dataset to examine which workforce factors are associated with attrition and how well standard supervised learning models classify higher-risk versus lower-risk cases. The workflow combines exploratory data analysis, preprocessing, class-imbalance correction, model comparison, and PCA. Logistic Regression produced the strongest overall performance in this project setup (AUC = 0.934), followed by Random Forest and Decision Tree models. Across exploratory analysis and model outputs, overtime, compensation-related variables, job role, age, and tenure patterns emerged as meaningful signals. Completed as graduate coursework in people analytics and machine learning, the project is best interpreted as a demonstration of analytical workflow and model interpretation rather than as directly deployable organizational guidance.

**Keywords:** employee attrition, people analytics, machine learning, logistic regression, random forest, SMOTE

---

## 1. Introduction

Employee attrition is one of the most common applications of people analytics because it affects workforce continuity, replacement cost, and planning stability. A well-framed attrition project typically needs to do two things at once: identify interpretable workforce patterns and evaluate whether a predictive model adds useful signal beyond descriptive reporting.

This project applies that workflow to the IBM HR Analytics Employee Attrition dataset, a widely used public benchmark, as part of graduate coursework in people analytics and machine learning. The central question is straightforward:

> Which employee and job factors are most associated with attrition in this dataset, and how well can common classification models distinguish attrition from non-attrition cases?

The analysis proceeds from exploratory data analysis to preprocessing, class-imbalance handling, model comparison, and interpretation of practical implications.

---

## 2. Dataset Description

The dataset was retrieved from Kaggle and contains 1,470 de-identified employee records with 35 variables. These variables span several broad domains:

| Domain | Example variables |
|--------|-------------------|
| Demographic | Age, Gender, MaritalStatus, EducationField |
| Job characteristics | JobRole, Department, JobLevel, BusinessTravel, OverTime |
| Compensation | MonthlyIncome, MonthlyRate, HourlyRate, PercentSalaryHike, StockOptionLevel |
| Satisfaction and engagement | JobSatisfaction, EnvironmentSatisfaction, JobInvolvement, WorkLifeBalance |
| Tenure | YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager |
| Outcome | Attrition (Yes/No) |

The outcome is imbalanced: 1,233 employees are coded as non-attrition (83.9%) and 237 as attrition (16.1%). This imbalance matters because a naive classifier can appear accurate while doing a poor job identifying the minority class.

The dataset is also a curated public benchmark. That makes it useful for demonstrating analysis design and model comparison, but it limits how confidently findings should be generalized to any real employer.

---

## 3. Data Preparation

Preparation focused on keeping the feature set usable for both exploration and modeling.

### 3.1 Feature Removal

Four variables were removed before modeling because they did not add useful information:

- `Over18`
- `StandardHours`
- `EmployeeCount`
- `EmployeeNumber`

The first three had no meaningful variance, and `EmployeeNumber` functioned only as an identifier.

### 3.2 Encoding and Scaling

Binary variables such as `OverTime`, `Gender`, and `Attrition` were converted to numeric indicators. Multi-category predictors such as `JobRole`, `Department`, `MaritalStatus`, `BusinessTravel`, and `EducationField` were retained for exploratory analysis and one-hot encoded for modeling as needed.

Continuous variables were standardized before PCA so that large-scale variables such as income would not dominate the component structure simply because of measurement scale.

### 3.3 Class Imbalance Handling

Because attrition is the minority class, the analysis used SMOTE and ADASYN to rebalance the training data. This step was important because an imbalanced model can achieve superficially high accuracy by predicting non-attrition almost all the time, which is not useful for the actual business question.

---

## 4. Exploratory Findings

Exploratory analysis was used to identify the variables with the clearest attrition patterns before comparing models.

### 4.1 Overtime

Overtime emerged as one of the clearest attrition signals in the dataset. Employees working overtime showed notably higher attrition rates than employees not working overtime.

### 4.2 Marital Status

Single employees showed higher attrition rates than married or divorced employees. In practical terms, this suggests that attrition risk may not be distributed evenly across employee groups with different personal and career-stage contexts.

### 4.3 Job Role

Attrition rates varied across job roles. Sales Representatives and Laboratory Technicians were among the higher-attrition roles, while some senior roles showed lower attrition. This supports looking at role-specific patterns rather than treating attrition as uniform across the workforce.

### 4.4 Age and Tenure

Younger employees and employees earlier in tenure showed higher attrition patterns than later-career groups. In this dataset, attrition appears concentrated in an earlier-career window rather than being evenly distributed over time.

### 4.5 Additional Signals

Monthly income, stock option level, job involvement, and work-life balance also showed meaningful differences between attrition and non-attrition groups. These did not operate as isolated explanations, but they consistently appeared among the more informative signals in the project.

---

## 5. Modeling Approach

The project compared three supervised classification models and used PCA as a supplementary exploratory tool.

### 5.1 Logistic Regression

Logistic Regression was included as an interpretable baseline model. Its main advantage in this context is transparency: coefficients and predicted probabilities are easier to explain to non-technical stakeholders than many black-box approaches.

### 5.2 Decision Tree

Decision Trees were used because they can capture non-linear splits and are easy to translate into rule-based logic. That interpretability can be useful in business settings even when they do not produce the strongest predictive performance.

### 5.3 Random Forest

Random Forest was used to test whether an ensemble tree approach would improve performance and provide more stable feature importance rankings than a single tree.

### 5.4 Principal Component Analysis

PCA was used to examine structure in the feature space rather than as the core predictive engine. Comparing standardized and unstandardized PCA also highlighted how strongly scaling choices affect component interpretation.

---

## 6. Results

### 6.1 Classification Performance

All models were evaluated on a held-out test set.

| Model | Accuracy | Precision | Recall | F1-Score | AUC |
|-------|----------|-----------|--------|----------|-----|
| Logistic Regression | 93.4% | 96.0% | 90.5% | 93.2% | 0.934 |
| Random Forest | 90.1% | 91.3% | 86.4% | 88.8% | 0.901 |
| Decision Tree | 83.7% | 79.0% | 83.2% | 81.2% | 0.837 |

Logistic Regression performed best in this project setup across the reported metrics. Random Forest also performed strongly, while Decision Tree offered lower overall performance but remained interpretable.

Balancing the training data materially improved minority-class detection compared with the imbalanced baseline setup. This was one of the clearest methodological lessons from the project.

### 6.2 Feature Importance

Feature importance rankings from the tree-based models were broadly consistent. The most informative variables included:

- Monthly income
- Stock option level
- Age
- Job involvement
- Job satisfaction
- Overtime

This alignment between exploratory analysis and model outputs increases confidence that the main signals are not artifacts of a single modeling approach.

### 6.3 PCA Interpretation

Unstandardized PCA was dominated by high-magnitude variables such as income-related measures. Standardized PCA produced a more interpretable structure, with components that roughly reflected tenure, compensation, and engagement-related dimensions. PCA added descriptive insight, but it was not central to model performance.

---

## 7. Discussion

Three themes stand out from the combined exploratory and modeling results.

First, compensation-related variables consistently matter. Monthly income and stock option level ranked near the top of the feature importance outputs, suggesting that pay structure and financial incentives are important parts of the attrition picture in this benchmark dataset.

Second, overtime appears as a strong operational signal. In a real organizational setting, that would justify closer attention to workload design, staffing patterns, and manager-level team demands rather than treating attrition primarily as a compensation problem.

Third, attrition patterns appear concentrated in earlier-career employees, shorter-tenure employees, and selected job roles. That points toward segment-specific analysis rather than generic retention messaging.

These are best understood as illustrative implications. They show the kinds of questions an internal people analytics team could test with its own data, not universal conclusions that should be applied unchanged across organizations.

---

## 8. Limitations

This project has several important constraints.

**Benchmark dataset limitations.** The IBM dataset is a public benchmark with limited provenance detail, so it should not be treated as a basis for claims about IBM's actual workforce or any other employer's current attrition dynamics.

**Outcome definition.** The attrition variable is binary and does not clearly separate voluntary from involuntary exits, which reduces interpretive precision.

**Cross-sectional structure.** The dataset is a static snapshot rather than a longitudinal panel, so it cannot model change over time or identify leading indicators with temporal precision.

**Predictive, not causal.** Variable importance and model performance indicate association, not causation. A strong predictor is not automatically an intervention lever.

**Operational readiness.** Strong benchmark performance does not by itself justify deployment. Real-world use would require organization-specific validation, monitoring, fairness review, and governance.

---

## 9. Conclusion

This project demonstrates a practical attrition-analysis workflow using a widely known people analytics benchmark dataset. The analysis combined exploratory data analysis, preprocessing, class-imbalance correction, model comparison, and business interpretation in a way that mirrors a realistic analytics process.

Within this project setup, Logistic Regression produced the strongest overall classification results, while overtime, compensation-related variables, role, age, and tenure emerged as recurring signals across methods. The most durable takeaway is not that a benchmark model should be deployed as-is. It is that attrition work is strongest when descriptive analysis, modeling discipline, and careful interpretation are kept tightly connected.

---

## References

Adams, J. S. (1965). Inequity in social exchange. In L. Berkowitz (Ed.), *Advances in Experimental Social Psychology* (Vol. 2, pp. 267–299). Academic Press.

Bakker, A. B., & Demerouti, E. (2007). The job demands-resources model: State of the art. *Journal of Managerial Psychology, 22*(3), 309–328. https://doi.org/10.1108/02683940710733115

Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research, 16*, 321–357.

He, H., Bai, Y., Garcia, E. A., & Li, S. (2008). ADASYN: Adaptive synthetic sampling approach for imbalanced learning. In *Proceedings of the 2008 IEEE International Joint Conference on Neural Networks* (pp. 1322–1328). IEEE. https://doi.org/10.1109/IJCNN.2008.4633969

Mitchell, T. R., Holtom, B. C., Lee, T. W., Sablynski, C. J., & Erez, M. (2001). Why people stay: Using job embeddedness to predict voluntary turnover. *Academy of Management Journal, 44*(6), 1102–1121.
