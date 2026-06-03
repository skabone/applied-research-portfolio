# Job Change Prediction with CRISP-DM

**Author:** Mintay Misgano, PhD
**Year:** 2022
**Tools:** Python, pandas, numpy, scikit-learn
**Dataset:** Kaggle HR Analytics: Job Change of Data Scientists (N = 19,158 training records)

---

## Abstract

This project applies the CRISP-DM framework to a public HR analytics classification problem: estimating which data science trainees are likely to look for a new job after training. The project was originally completed in graduate data-mining coursework, but the public version is framed as an applied prediction workflow rather than a methods exercise.

Gradient boosting produced the strongest model in this workflow, with cross-validated ROC-AUC = 0.784 and holdout ROC-AUC = 0.802. The holdout confusion matrix showed 431 true positives, 524 false negatives, 302 false positives, and 2,575 true negatives. Those values support a cautious interpretation: the model is useful as a ranked prioritization layer, but the default threshold misses too many job-change cases to justify automated decision-making.

---

## 1. Project Context

The business question is whether a training provider could use candidate background, education, experience, employer context, and training activity to prioritize follow-up for trainees who may be looking for a new job. In a real talent-pipeline setting, the value of such a model would not come from labeling candidates as "leaving" or "staying." The value would come from ranking cases so recruiters or program staff can decide where limited follow-up time is most useful.

CRISP-DM, or Cross-Industry Standard Process for Data Mining, is a six-phase framework for applied analytics: business understanding, data understanding, data preparation, modeling, evaluation, and deployment planning (Chapman et al., 2000). The framework matters here because the prediction task has operational consequences. A model with acceptable aggregate accuracy can still be weak if it misses too many positive cases, uses unstable features, or is interpreted as causal when the data only support prediction.

---

## 2. Data Understanding

The dataset contains 19,158 training records and 2,129 unlabeled test records. The target variable is binary: `1` indicates that a trainee is looking for a job change, while `0` indicates that the trainee is not looking.

The first descriptive issue is class imbalance. Of the 19,158 training records, 14,381 cases are labeled `0` and 4,777 cases are labeled `1`. In percentage terms, 75.1% of trainees are not looking for a job change and 24.9% are looking. This imbalance shapes the analysis because a model can appear accurate by favoring the majority class.

The second descriptive issue is missingness. Employer-context fields have the heaviest missingness: `company_type` is missing in 6,140 records and `company_size` is missing in 5,938 records. Demographic and education fields also have missingness, including `gender` (4,508), `major_discipline` (2,813), `education_level` (460), `last_new_job` (423), `enrolled_university` (386), and `experience` (65). At this stage, the missingness pattern is not yet a recommendation. It is an analytic constraint: the model needs an imputation strategy, and any deployment interpretation should treat employer-context predictors with caution.

---

## 3. Data Preparation

Categorical missing values were imputed with the modal category within each field. This is a simple, transparent choice for a benchmark workflow, but it has tradeoffs. Mode imputation preserves sample size and keeps the preprocessing pipeline compact, but it can understate uncertainty when missingness is meaningful. A production workflow would compare mode imputation with missingness indicators, model-based imputation, or separate "unknown" categories depending on stakeholder needs and data governance constraints.

Ordinal fields were recoded into numeric approximations. Experience values such as `>20` and `<1` were converted into interpretable numeric values, company-size ranges were converted into midpoint estimates, and `last_new_job` was recoded into a numeric tenure-change feature. These transformations preserve ordering information that would be lost if all categories were treated as unrelated labels.

Binary features were engineered for relevant experience, university enrollment, STEM major, and private-sector employer type. Training hours were log-transformed using `log1p()` because the raw variable is right-skewed: many trainees have moderate hours, while a smaller number have very high values. The log transformation compresses extreme values so they do not dominate distance- or split-based model behavior.

---

## 4. Modeling Strategy

Four models were compared under the same stratified 5-fold cross-validation design:

| Model | Role in the comparison |
|---|---|
| Logistic regression | Linear baseline for interpretable classification |
| Decision tree | Simple nonlinear model with rule-based splits |
| Random forest | Bagged tree ensemble that reduces single-tree instability |
| Gradient boosting | Sequential tree ensemble that improves by focusing on prior errors |

Stratified cross-validation preserves the class distribution inside each fold. That choice matters because the positive class represents only 24.9% of the training sample; non-stratified folds could create unstable or misleading model estimates.

---

## 5. Evaluation Metrics

Accuracy is the proportion of cases classified correctly. It is easy to interpret, but it can be misleading with imbalanced outcomes because predicting the majority class can produce a superficially high score.

ROC-AUC, or area under the receiver operating characteristic curve, measures how well the model ranks positive cases above negative cases across possible thresholds (Fawcett, 2006). A value of 0.50 is no better than random ranking; values closer to 1.00 indicate stronger discrimination. ROC-AUC is useful here because the operational question is partly about prioritization: who should be reviewed first?

Precision is the proportion of predicted positive cases that are truly positive. In this project, positive-class precision answers: among trainees flagged as looking for a job change, how many actually have the positive label?

Recall is the proportion of actual positive cases that the model identifies. In this project, recall answers: among trainees who are looking for a job change, how many did the model catch? Recall is especially important if the stakeholder cares about not missing people who may need follow-up.

---

## 6. Results

### 6.1 Cross-Validated Model Comparison

| Model | CV Accuracy | CV ROC-AUC |
|---|---:|---:|
| Logistic regression | 0.764 | 0.732 |
| Decision tree | 0.778 | 0.761 |
| Random forest | 0.779 | 0.781 |
| Gradient boosting | 0.780 | 0.784 |

Gradient boosting had the strongest ROC-AUC at 0.784, but random forest was very close at 0.781. The small AUC gap matters for interpretation: gradient boosting is the selected model, but the evidence does not suggest a dramatic performance separation between the two ensemble approaches. The larger contrast is between the ensemble models and logistic regression, where the AUC difference is roughly 0.052 to 0.052 points depending on the ensemble used. That pattern suggests nonlinear relationships or interaction-like structure in the predictors.

### 6.2 Holdout Performance

| Metric | Value |
|---|---:|
| Holdout accuracy | 0.784 |
| Holdout ROC-AUC | 0.802 |
| Positive-class precision | 0.588 |
| Positive-class recall | 0.451 |
| Positive-class F1 | 0.511 |

The holdout ROC-AUC of 0.802 is the strongest evidence that the model can rank cases meaningfully. However, the threshold-specific classification metrics show the operational tradeoff. At the default 0.50 threshold, positive-class precision is 0.588 and recall is 0.451. In plain terms, the model's positive flags are moderately precise, but it catches fewer than half of the true job-change cases.

### 6.3 Confusion Matrix

| Holdout result | Count |
|---|---:|
| True negatives | 2,575 |
| False positives | 302 |
| False negatives | 524 |
| True positives | 431 |

The confusion matrix explains why accuracy alone is not enough. The model correctly classified 2,575 negative cases and 431 positive cases, but it missed 524 positive cases. If the purpose were broad early outreach, those false negatives would be a serious limitation. If the purpose were narrower prioritization for a limited follow-up queue, the model could still be useful because the ranked probabilities help staff decide where to look first.

### 6.4 Feature Importance

| Feature | Importance |
|---|---:|
| City development index | 0.604 |
| Company size | 0.132 |
| Log training hours | 0.060 |
| Education level | 0.047 |
| Relevant experience | 0.044 |
| Experience | 0.043 |

City development index dominates the fitted gradient boosting model, with importance = 0.604. That is more than four times the importance of company size (0.132), the second-ranked predictor. The key interpretation is that local labor-market context appears to carry more predictive signal than individual training activity alone. Log training hours ranks third at 0.060, which means training engagement contributes to the model but is not the primary driver.

---

## 7. Synthesis

Three results matter most when read together.

First, the class imbalance means that the model must be evaluated beyond accuracy. A naive majority-class prediction strategy would already be correct for 75.1% of records, so the holdout accuracy of 0.784 is not sufficient by itself.

Second, the AUC evidence is stronger than the default-threshold evidence. Gradient boosting reaches holdout ROC-AUC = 0.802, which supports using the model for ranking or prioritization. But the same model catches only 431 of 955 positive holdout cases at the 0.50 threshold, which argues against using the default threshold as a final decision rule.

Third, the feature-importance pattern points toward structural context. City development index has importance = 0.604, while company size and training hours are much lower. That does not prove a causal relationship, but it does suggest that job-change intent in this dataset is heavily shaped by market context.

---

## 8. Recommendations

**Use the model as a ranked screening layer, not an automated decision rule.** This recommendation follows from the mismatch between AUC and recall: the model ranks cases reasonably well (holdout ROC-AUC = 0.802), but at the default threshold it misses 524 of 955 positive cases.

**Tune the decision threshold to the stakeholder's risk tolerance.** If the priority is to avoid missing likely job-change cases, the threshold should be lowered and evaluated against recall, precision, and follow-up capacity. If the priority is to avoid false alarms, the threshold can remain higher, but the stakeholder should accept that more true job-change cases will be missed.

**Treat city development index as a context signal, not an individual diagnosis.** Because city development index is the dominant feature (importance = 0.604), the model is partly detecting labor-market context. Any action should focus on program planning, local market awareness, and prioritization, not on making individual-level causal claims about a trainee.

**Recalibrate before live use.** This is a public benchmark dataset, not current operational data. Before deployment, the model would need updated data, fairness checks, calibration review, and monitoring for AUC drift.

---

## 9. Limitations

The dataset is public and benchmark-oriented, so the results should not be treated as direct evidence about a specific employer or training provider.

Several predictors may act as proxies for broader socioeconomic or labor-market conditions. That makes model interpretation useful for planning, but risky if translated into individual-level decisions without fairness review.

The workflow uses transparent preprocessing and moderate model comparison rather than exhaustive hyperparameter tuning. That is appropriate for a compact CRISP-DM portfolio analysis, but a production build would require deeper validation.

---

## 10. Conclusion

This project shows how a job-change prediction task should be reasoned through from data description to model evaluation and operational interpretation. The strongest result is not simply that gradient boosting "won." The stronger conclusion is that gradient boosting can rank cases meaningfully, but the default classification threshold does not catch enough positive cases for automated action. That distinction is what turns the model comparison into a practical analytics recommendation.

---

## References

Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.

Fawcett, T. (2006). An introduction to ROC analysis. *Pattern Recognition Letters, 27*(8), 861-874.
