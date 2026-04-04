# HR Analytics: Job Change Prediction — Executive Brief
**Dataset:** Kaggle HR Analytics — Job Change of Data Scientists (N = 19,158) | **Analyst:** Mintay Misgano | **Year:** 2022

---

## The Business Problem

A company that trains data scientists wants to identify which participants are actively seeking new employment after completing their program — so it can optimize placement resources toward candidates likely to remain and adjust recruitment strategy for those likely to leave. This is a direct analog of the voluntary attrition prediction problem facing any HR or talent management team: which employees are most likely to leave in the next quarter, and what factors drive that departure intent? The dataset comes from Kaggle's HR Analytics competition and contains 19,158 training records with features spanning geography, education, work history, company profile, and training engagement.

---

## Approach

- Applied the **CRISP-DM framework** (Cross-Industry Standard Process for Data Mining): Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment
- **Data preparation:** Imputed 6 variables with missing data (23% of gender missing, 32% of company-related fields); ordinal-encoded experience (">20" → 21) and company size (midpoint integers); engineered binary flags for STEM background, private company type, and active enrollment; log-transformed training hours to reduce right skew
- **Models trained and evaluated:** Logistic Regression, Decision Tree, Random Forest, Gradient Boosting — all evaluated via 5-fold stratified cross-validation on both accuracy and ROC-AUC
- **Success metric:** ROC-AUC > 0.75 (sufficient for talent pipeline prioritization)
- **Tools:** Python, scikit-learn, pandas, numpy

---

## Key Findings

- **Gradient Boosting achieves the best ROC-AUC (~0.79)** — meeting the deployment threshold and demonstrating that ensemble methods outperform single classifiers on this imbalanced classification problem
- **City development index is the strongest single predictor** — candidates in high-CDI cities (strong local job markets) show significantly higher job-seeking intent, consistent with economic mobility theory and the finding that external labor market conditions drive attrition as much as internal factors
- **Relevant work experience paradoxically increases job-seeking intent** — experienced candidates have a clearer picture of their market value and more attractive alternatives, making them simultaneously the most valuable and the most mobile trainees. This mirrors the "star player retention" challenge in corporate talent management
- **Mid-career professionals (5–10 years experience) show peak departure intent** — very early-career and very senior candidates are more stable; mid-career professionals are in the highest-competition zone of the labor market
- **Training hours alone is a weak predictor** — the number of training hours completed correlates minimally with departure intent, suggesting that training investment alone does not create retention; the program-to-employment pipeline and internal opportunity must also be present

---

## Recommendations

1. **Score each cohort at mid-program, not at graduation.** Waiting until training completion to identify departure-intent candidates leaves no time for intervention. A mid-program scoring pass (week 4–6) using the trained model allows the placement team to prioritize candidates with P(leaving) > 0.50 for proactive internal opportunity conversations.
2. **Tailor retention interventions to city development index.** Candidates in high-CDI metro areas (coastal tech hubs) are structurally more mobile regardless of program quality. Specific retention incentives — relocation support, hybrid roles, accelerated internal placement — are justified for this segment.
3. **Build the CRISP-DM framework into all HR analytics projects.** Most HR analytics projects fail at the business understanding and deployment stages, not the modeling stage. Defining success criteria upfront (AUC > 0.75) and specifying deployment logic (score at mid-program, flag P > 0.5) ensures that modeling work connects to operational outcomes.

---

## Impact

Demonstrated a complete CRISP-DM data mining pipeline on a real HR dataset — from business problem definition through model deployment logic. The four-classifier comparison with ROC-AUC as the primary success metric reflects production-grade model evaluation: accuracy alone is misleading when classes are imbalanced (25% positive), whereas AUC measures discriminative ability independent of threshold. Applied to a corporate training context, the model supports data-driven talent pipeline management rather than intuition-based placement decisions.

---

*Analysis by Mintay Misgano | Tools: Python (scikit-learn, pandas) | Data: Kaggle HR Analytics (N=19,158) | Course: ISM 6359 Data Mining, SPU (Winter 2022)*
