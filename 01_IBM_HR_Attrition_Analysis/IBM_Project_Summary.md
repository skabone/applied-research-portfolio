# IBM Employee Attrition Analysis — Project Summary

**Dataset:** IBM HR Analytics public benchmark  
**Scope:** Attrition pattern analysis and model comparison

---

## Project Context

This project was completed as part of graduate coursework in people analytics and machine learning. It uses a public benchmark dataset to examine which workforce factors are associated with attrition and to compare several standard classification models in a structured workflow.

The goal is not to present a deployable attrition tool. The goal is to show how an attrition problem can be framed responsibly, translated into an analytical workflow, and interpreted with appropriate caution when the data come from a public benchmark.

---

## What Was Done

- Analyzed 1,470 employee records across demographic, job, compensation, satisfaction, and tenure variables
- Examined attrition patterns with exploratory visual analysis
- Addressed class imbalance, since attrition represents about 16% of the dataset
- Compared Logistic Regression, Decision Tree, and Random Forest performance
- Used PCA as a supplementary step to explore structure in the feature set

---

## Main Takeaways

- **Overtime stands out as a major attrition signal.** Employees working overtime show notably higher attrition rates in the benchmark data.
- **Compensation-related variables matter.** Monthly income and stock option level appear near the top of the feature rankings in tree-based models.
- **Risk is not evenly distributed across groups.** Younger employees, single employees, and some job roles show higher attrition patterns than others.
- **Modeling performance improved once class imbalance was handled.** This reinforces how important minority-class treatment is in attrition work.
- **Logistic Regression performed best in this project setup.** It achieved the strongest overall test metrics, including AUC = 0.934.

---

## What This Demonstrates

This project demonstrates several skills that matter in applied people analytics work:

1. Translating a broad workforce question into a staged analytical workflow
2. Handling class imbalance rather than relying on misleading accuracy alone
3. Comparing interpretable and non-linear modeling approaches instead of depending on a single model
4. Connecting model outputs back to understandable workforce patterns
5. Communicating findings with scope limits that match the data source

For a real organization, the findings suggest the kinds of issues that would be worth validating with internal data, especially workload patterns, compensation structure, early-tenure experience, and role-level variation. These are illustrative implications, not deployment recommendations.

---

## Bottom Line

This project shows a practical people analytics workflow for attrition modeling: define the question, inspect the data carefully, account for class imbalance, compare multiple models, and interpret the results in plain language. Its strongest value as a portfolio piece is not that it solves attrition universally, but that it demonstrates disciplined analytical thinking with a familiar workforce problem.
