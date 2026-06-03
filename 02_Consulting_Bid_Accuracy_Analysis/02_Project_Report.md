# Consulting Bid Accuracy Analysis — Project Report
### Identifying Drivers of Estimation Discrepancy in an Anonymized Consulting Engagement

- **Author:** Mintay Misgano, PhD
- **Date:** March 2023
- **Tools:** R, RStudio, OLS Regression
- **Dataset:** 279 synthetic public records modeled from protected project records, FY2020–2021

> **Confidentiality Note:** This project was completed under a Non-Disclosure Agreement. The client organization is not named. Personnel identifiers, client organization names, invoice numbers, and operationally identifying details have been removed. The public dataset is synthetic and anonymized, preserving the analytical structure of the engagement without exposing protected records.

---

## Abstract

This project examines bid-to-invoice discrepancy in a real consulting engagement using a synthetic, anonymized public dataset modeled from two years of protected project records (N = 279, FY2020–2021). Eight ordinary least squares (OLS) regression models were estimated to identify which project-level, personnel, and client-level factors best predict the difference between estimated bids and actual invoiced amounts. Four of five OLS assumptions were violated, so results are interpreted cautiously at p < .01. The strongest recurring signals came from consultant identity and a small number of specific client organizations. Service area and broad project type were not meaningful standalone predictors. The engagement was completed as graduate coursework using protected client data under NDA.

---

## 1. Business Problem

The client organization provided assessment-related services in the public safety sector, operating on a project-bid model where costs are quoted before the full scope of delivery is confirmed. Over two fiscal years they accumulated 279 project records — and a recurring problem: estimated bids and final invoices were frequently misaligned, with no clear picture of why.

Two failure modes arise from bid inaccuracy. Overestimation — quoting too high relative to what is ultimately invoiced — risks losing contracts to lower-bidding competitors or eroding client confidence when the final number comes in substantially lower than expected. Underestimation — quoting too low — means absorbing costs beyond what was quoted, directly affecting profitability and potentially compressing delivery quality.

The central question this engagement was designed to answer:

> *Which project-level, personnel, and client-level factors most strongly predict the discrepancy between estimated bids and actual invoiced amounts?*

The outcome variable is defined as:

```
bid_discrepancy = invoice_total − estimated_bill
```

Positive values indicate underestimation (the firm invoiced more than projected). Negative values indicate overestimation (the firm invoiced less than projected). Values near zero reflect accurate estimation.

---

## 2. Analytical Framing

The practical question is not simply whether bids are off — it is whether the mismatch appears to come from broad structural features the firm could reprice systematically, or from narrower patterns tied to specific clients, consultants, or project types that could be addressed through targeted calibration.

### What Is OLS Regression?

Ordinary least squares (OLS) regression is a method for estimating the linear relationship between one or more predictor variables and a continuous outcome variable. It works by finding the set of coefficients that minimizes the sum of squared differences between observed and predicted values of the outcome — hence "least squares" (Montgomery et al., 2021). Each coefficient represents the expected change in the outcome for a one-unit increase in a predictor, holding all other predictors constant. When multiple predictors are included, OLS partitions variance in the outcome across those predictors, making it possible to compare the relative contribution of each while statistically controlling for the others (Cohen et al., 2003).

### Why OLS, and What Else Could Have Been Used?

Three alternative approaches were considered for this analysis:

**Mixed-effects regression (multilevel modeling)** would be the most technically appropriate choice for this dataset, because project leads (consultants) and client organizations appear repeatedly across records — a clustered structure that violates OLS's independence assumption (Raudenbush & Bryk, 2002). Mixed-effects models handle this explicitly by estimating random effects for each cluster. However, with only 279 records distributed across 11 consultants and 78 clients, many cells would be underpowered for reliable random-effect estimation. Mixed-effects modeling is recommended as a follow-up once additional years of data are available.

**Robust regression** (e.g., Huber M-estimation) would reduce the influence of outliers and is more appropriate when residuals are non-normal — both of which apply here (Field, 2018). However, robust regression sacrifices some interpretability compared to OLS, and the goal of this engagement was to produce findings the firm's operational staff could act on without specialized statistical training. OLS with conservative significance thresholds preserves that interpretability while acknowledging the distributional limitations.

**Tree-based methods** (e.g., random forest, gradient boosting) could capture non-linear relationships and interactions without distributional assumptions. Given that LOESS inspection revealed non-linearity in the data, these methods have appeal. However, they are less suited to the communication goal here — the client needed to understand *which specific factors* explained estimation error, not just have a black-box prediction function. OLS coefficients map directly onto interpretable comparisons (e.g., "Assessment Center projects average $X more in discrepancy than Written Exam projects"), which is what an operations review requires.

OLS is used here as an exploratory and interpretive tool under those constraints — not as a production prediction system — and with the conservative p < .01 threshold adopted to compensate for the assumption violations documented in Section 4. Eight model specifications are compared rather than relying on a single model, which reduces the risk that findings are artifacts of one particular specification (Kutner et al., 2005).

---

## 3. Data and Methods

### 3.1 Data Source and Structure

The original engagement used two fiscal years of internal project records from the client organization's project management system. For GitHub, those records were converted into a synthetic, anonymized public dataset that preserves the variable structure and analytical relationships needed to review the workflow while removing protected identifiers and operational details. The final public dataset contains 279 observations across 15 variables.

### 3.2 Variable Definitions

| Variable | Type | Description |
|----------|------|-------------|
| `project_id` | Character | Synthetic public row identifier |
| `project_year` | Character | Public year grouping (Year_1, Year_2) |
| `consultant_id` | Factor | Anonymized project lead (Consultant_A through Consultant_K) |
| `client_id` | Factor | Anonymized client organization identifier |
| `service_area` | Factor | Generalized service category |
| `project_type` | Factor | Generalized project type |
| `department_owner` | Factor | Department responsible: Operations, Consulting, or Unlisted |
| `associate_assigned` | Logical | Whether a support consultant was assigned |
| `billable_travel` | Logical | Whether the project required billable travel |
| `billable_shipping` | Logical | Whether the project required billable shipping |
| `candidate_count` | Integer | Project volume indicator |
| `estimated_bill` | Numeric | Estimated bid amount |
| `invoice_total` | Numeric | Actual amount invoiced to the client |
| `project_cost` | Numeric | Actual project costs incurred |
| `bid_discrepancy` | Numeric | Outcome variable: invoice_total − estimated_bill |
| `net_profit` | Numeric | invoice_total − project_cost |

### 3.3 Data Preparation

Missing data handling was determined by the nature of each field, not by default assumptions:

- **`associate_assigned`:** Converted to logical — `TRUE` if any support consultant was assigned, `FALSE` if no associate was attached.
- **`department_owner`:** Retained as a three-level factor (Operations, Consulting, Unlisted), allowing the model to test whether unlisted ownership has a systematic relationship with estimation error.
- **`project_cost`:** Retained as the public cost field used for net-profit calculation.
- **`invoice_total`, `estimated_bill`, `client_id`:** Treated as required fields for constructing and interpreting the outcome.

Three derived variables were created:
- `bid_discrepancy = invoice_total − estimated_bill` — primary dependent variable in dollars
- `net_profit = invoice_total − project_cost` — calculated public net-profit field

### 3.4 Evaluation Metrics

Four metrics are used to compare models throughout the results. Each is defined here so the comparison table in Section 5 can be interpreted directly.

**Adjusted R²** is a measure of how much variance in the outcome variable is explained by the model's predictors, penalized for the number of predictors included (Cohen et al., 2003). Unlike standard R², adjusted R² decreases when a predictor is added that does not meaningfully improve the model — which makes it more appropriate for comparing models with different numbers of predictors. Values range from 0 to 1; higher values indicate more variance explained. In exploratory organizational research, values in the .10–.30 range are common for single-category predictors, while full models often reach .40–.60 (Cohen et al., 2003). An adjusted R² of .00 or negative indicates the model explains no more variance than the mean alone.

**F-statistic and p-value** test whether the overall model explains a statistically significant amount of variance in the outcome beyond what would be expected by chance (Montgomery et al., 2021). A significant F-statistic (p < .01, given the threshold adopted here) is a prerequisite for any further interpretation — a non-significant model is not meaningfully interpreted regardless of individual coefficient values.

**Mean Absolute Error (MAE)** is the average absolute difference between observed and predicted values of the outcome, expressed in the same units as the outcome variable (here, dollars) (Kutner et al., 2005). MAE is straightforward to communicate to non-technical audiences: an MAE of $900 means the model's predictions are off by an average of $900. Lower values indicate better predictive accuracy. MAE is less sensitive to extreme outliers than RMSE, making it useful for understanding typical prediction error in a dataset with some large discrepancies.

**Root Mean Squared Error (RMSE)** is the square root of the average squared prediction error, also expressed in outcome units (Kutner et al., 2005). Because squaring the errors before averaging gives disproportionate weight to large errors, RMSE is more sensitive to outliers than MAE. When RMSE is substantially larger than MAE — as it is across most models here — that signals the presence of a small number of high-discrepancy projects pulling the squared error upward. Comparing MAE and RMSE together helps characterize the error distribution: a large gap between them indicates the model struggles most on the extreme cases.

### 3.5 Model Specifications

Eight OLS regression models were estimated, each approaching the business question from a different angle:

| Model | Predictors |
|-------|-----------|
| M1 | All predictors (full model) |
| M2 | Consultant identity only |
| M3 | Client organization only |
| M4 | Service area only |
| M5 | Project type only |
| M6 | Department ownership only |
| M7 | Operational flags |
| M8 | Financial predictors |

Model selection followed a hierarchy: F-statistic significance → adjusted R² → parsimony → MAE/RMSE.

---

## 4. Assumption Testing

OLS regression carries five standard assumptions that must hold — at least approximately — for coefficient estimates and significance tests to be trustworthy (Montgomery et al., 2021). All five were formally tested prior to modeling.

| Assumption | Test Used | Result | Status |
|------------|-----------|--------|--------|
| Linearity | LOESS visual inspection | Non-linear relationships observed | ❌ Violated |
| Normality of Residuals | Anderson-Darling; Shapiro-Wilk | p < .001 on both | ❌ Violated |
| Homoscedasticity | Breusch-Pagan test | BP = 3.12, p = .37 | ✅ Met |
| No Multicollinearity | Correlation matrix | \|r\| > .70 among financial predictors | ❌ Violated |
| Independence | Structural inspection | Repeated project leads and clients in data | ❌ Violated |

**Linearity** requires that the relationship between each predictor and the outcome is linear. LOESS (locally estimated scatterplot smoothing) curves plotted for the continuous predictors revealed non-linear patterns, indicating this assumption is not fully met (Field, 2018).

**Normality of residuals** requires that the errors from the model are approximately normally distributed — a condition that becomes especially important with smaller samples (Cohen et al., 2003). The Anderson-Darling test (A = 14.72, p < .001) and Shapiro-Wilk test (W = .891, p < .001) both reject normality, consistent with the observed right-skew in the bid-discrepancy distribution.

**Homoscedasticity** requires that the variance of residuals is constant across fitted values. The Breusch-Pagan test (BP = 3.12, p = .37) fails to reject the null of constant variance — this assumption is met, which at minimum stabilizes standard errors across the range of predictions (Kutner et al., 2005).

**No multicollinearity** requires that predictors are not so highly intercorrelated that coefficient estimates become unstable (Montgomery et al., 2021). Financial predictors (`invoice_total`, `estimated_bill`, `project_cost`, `bid_discrepancy`, and `net_profit`) are highly intercorrelated (|r| > .70), so models including multiple financial variables simultaneously are interpreted with caution and the financial-predictor model (M8) is treated separately.

**Independence** requires that observations are not systematically related to one another. The repeated appearance of the same project leads and client organizations across records violates this assumption (Raudenbush & Bryk, 2002). This is the most substantive concern and the primary reason mixed-effects modeling is recommended as a follow-up.

Because four of five assumptions are violated, a more conservative significance threshold of **p < .01** was adopted throughout (rather than the standard p < .05). This reduces Type I error risk given the elevated uncertainty from assumption violations (Field, 2018).

![Linearity check for financial predictors](docs/figures/assumption-linearity-1.png)

The smoothed lines show non-linear patterns between financial predictors and bid discrepancy. This is one reason the final recommendations are framed as exploratory operational guidance rather than precise coefficient-based forecasts.

---

## 5. Results

### 5.1 Descriptive Summary

![Distribution of bid-to-invoice discrepancy](docs/figures/eda-dv-dist-1.png)

The distribution is centered near zero but has enough spread to create operational risk in both directions. That matters because the average discrepancy alone would make the estimation process look more stable than it was at the project level.

| Statistic | Value |
|-----------|-------|
| N | 279 |
| Mean bid discrepancy | +$412 |
| Median bid discrepancy | +$75 |
| SD | $3,847 |
| Min | −$18,400 |
| Max | +$24,600 |
| Projects underestimated (bid_discrepancy > 0) | 161 (58%) |
| Projects overestimated (bid_discrepancy < 0) | 102 (37%) |
| Perfect estimates (bid_discrepancy = 0) | 16 (6%) |

The firm underestimates more often than it overestimates (58% vs. 37%), but the mean and median are both close to zero — the overall portfolio roughly balances out, which masks substantial project-level variance.

![Estimated bill compared with final invoice](docs/figures/eda-bill-vs-invoice-1.png)

The diagonal line marks perfect estimate accuracy. Projects above the line were underestimated and projects below the line were overestimated, showing why the engagement focused on calibration rather than simply whether the firm was high or low overall.

![Bid discrepancy by project type](docs/figures/eda-project-type-1.png)

Project type shows some separation, but the overlap across categories is substantial. That visual pattern is consistent with the model results: project type carries some signal, but it does not explain the estimation problem on its own.

![Bid discrepancy by service area](docs/figures/eda-service-area-1.png)

Service-area differences are not strong enough to support a broad repricing strategy by category. This helped rule out one intuitive but overly broad explanation before moving to client and consultant patterns.

![Bid discrepancy by department ownership](docs/figures/eda-department-1.png)

Projects with unlisted department ownership show greater estimation instability. In practical terms, missing ownership behaves less like a neutral blank field and more like a data-quality signal.

![Correlation matrix for numeric project variables](docs/figures/eda-correlation-1.png)

The correlation matrix shows why financial predictors needed careful treatment. Estimated bill and invoice total are strongly related, and including too many related financial fields in the same model would make coefficients harder to interpret.

![Average bid discrepancy by project year](docs/figures/eda-year-1.png)

The year comparison provides a quick check for whether the issue was concentrated in one fiscal period. Because the pattern persisted across both years, the analysis treated bid accuracy as a recurring process issue rather than a one-year anomaly.

### 5.2 Model Comparison

| Model | F-Stat | p-value | Adj. R² | MAE | RMSE |
|-------|--------|---------|---------|-----|------|
| M1: All Predictors (Full) | 4.94 | < .001 | .498 | $548 | $665 |
| M2: Consultant Identity | 5.38 | < .001 | .099 | $808 | $1,016 |
| M3: Client Organization | 2.16 | < .001 | .164 | $716 | $904 |
| M4: Service Area | 0.50 | .685 | -.005 | $866 | $1,081 |
| M5: Project Type | 7.22 | < .001 | .101 | $825 | $1,019 |
| M6: Department Owner | 3.29 | .039 | .016 | $856 | $1,071 |
| M7: Operational Flags | 6.63 | < .001 | .075 | $829 | $1,035 |
| M8: Financial Predictors | 18.07 | < .001 | .109 | $817 | $1,020 |

*Note: the full model has the strongest predictive accuracy because it combines project, client, personnel, operational, and financial information. The single-predictor models are interpreted diagnostically to identify where the strongest process signals appear.*

![MAE and RMSE by model specification](docs/figures/results-viz-1.png)

The model comparison shows the lowest error in the full specification, followed by client-account patterns. The gap between MAE and RMSE indicates that a small set of high-discrepancy projects still drives much of the prediction difficulty.

### 5.3 Key Findings

**Consultant Identity (M2, Adj. R² = .099, p < .001)**
Consultant identity alone explains roughly 10% of bid discrepancy variance. Several consultants show systematic over- or underestimation patterns, pointing toward individual calibration differences rather than a project-mix artifact.

**Client Organization (M3, Adj. R² = .164, p < .001)**
Client ID is the strongest single categorical predictor in the public model set, explaining approximately 16% of variance. A small number of specific clients drive most of this effect, each showing discrepancy extremes above or below zero. These clients likely represent systematically misunderstood or underdocumented project complexity.

**Project Type (M5, Adj. R² = .101, p < .001)**
Project type explains a meaningful slice of bid discrepancy in the public model set. Some project categories are more prone to underestimation or overestimation than others, although the overlap across categories means project type should not be used as the only pricing adjustment.

**Department Owner (M6, p = .039)**
Projects with no department recorded (`department_owner = Unlisted`) show weaker evidence of estimation differences than consultant, client, or project-type models. The pattern is still operationally useful as a process-quality signal, but it is not interpreted as a strong standalone statistical driver at p < .01.

**Service Area (M4): Not significant at p < .01**
Generalized service category does not independently predict estimation error. This rules out one broad structural explanation and keeps the interpretive focus on client, consultant, project-type, and operational patterns.

---

## 6. Discussion

The results suggest the organization's estimation problem is not primarily structural. The firm is not systematically mis-pricing entire service areas; instead, the strongest patterns cluster around specific consultant-client combinations where estimation assumptions appear to break down in recurring ways.

That distinction matters for how the organization responds. A structural problem calls for broad pricing model changes. A relational problem — one concentrated in specific accounts and individuals — calls for targeted audits, calibration conversations, and account-specific adjustments. The latter is generally more tractable and lower-risk to implement.

The significance of department tracking (`department_owner = Unlisted`) is most interpretable as a process-quality signal. Projects without department attribution were associated with worse estimation outcomes. That probably reflects broader intake discipline issues rather than a direct department effect — when projects are tracked carefully, they tend to be estimated more carefully too.

---

## 7. Recommendations

**1. Audit the highest-discrepancy client accounts.**
A small number of clients account for a disproportionate share of estimation error. An internal review of historical project files for those accounts could surface recurring scope, logistics, or pricing assumptions that aren't captured in current estimation templates.

**2. Conduct structured estimate debriefs with key project leads.**
The consultant-level patterns in M2 suggest a calibration opportunity. A structured review comparing estimate line items to final invoices — by project lead, for their most discrepant projects — could identify where assumptions about labor, travel, or scope consistently diverge from actual delivery.

**3. Revisit travel expense estimation.**
Projects with billable travel show a consistent overestimation pattern. Comparing current travel assumptions against historical actuals could identify a recoverable, concrete source of recurring discrepancy.

**4. Require department attribution at project intake.**
Approximately 32% of projects had no department recorded. Making this a required intake field improves both operational visibility and the quality of future analyses.

**5. Plan for mixed-effects modeling as a follow-up.**
The clustered structure of this dataset — repeated project leads and client organizations — violates OLS independence assumptions. A mixed-effects regression model would be the appropriate next step once intake fields are standardized and an additional year of data is available.

---

## 8. Limitations

**Sample size:** With 279 observations over two years, some factor levels are underpowered — particularly rare service areas, project types, client accounts, and consultant-client combinations. Results for infrequent categories should be treated cautiously.

**Assumption violations:** Four of five OLS assumptions were violated. The p < .01 threshold reduces but does not eliminate Type I error risk. Mixed-effects regression is the appropriate follow-up given the clustered structure.

**Synthetic public data:** The public dataset preserves the structure and modeling logic of the protected engagement, but it should not be treated as a raw client extract. Exact dollar values and record-level details are public-safe substitutes rather than protected operational records.

**Two-year window:** FY2020–2021 may not generalize across subsequent years as client mix, pricing strategy, and staffing change. Annual replication is advisable.

---

## 9. Conclusion

Two years of project records from this engagement pointed more toward specific consultant and client patterns than toward broad structural factors as the primary drivers of estimation error. That finding is operationally useful because it narrows the response from a systemic pricing overhaul toward more targeted review, calibration, and intake improvements.

Reasonable next steps: improve intake fields, conduct structured debriefs on the most discrepant accounts and consultants, review travel estimation assumptions, and rerun this analysis after one more year of data with a mixed-effects specification that properly accounts for the clustered structure.

---

## References

Cohen, J., Cohen, P., West, S. G., & Aiken, L. S. (2003). *Applied multiple regression/correlation analysis for the behavioral sciences* (3rd ed.). Lawrence Erlbaum Associates.

Field, A. (2018). *Discovering statistics using IBM SPSS statistics* (5th ed.). SAGE Publications.

Flyvbjerg, B. (2006). From Nobel Prize to project management: Getting risks right. *Project Management Journal, 37*(3), 5–15.

Kutner, M. H., Nachtsheim, C. J., Neter, J., & Li, W. (2005). *Applied linear statistical models* (5th ed.). McGraw-Hill Irwin.

Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to linear regression analysis* (6th ed.). Wiley.

Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical linear models: Applications and data analysis methods* (2nd ed.). SAGE Publications.

---

*Analysis completed March 2023 | R / RStudio | N = 279, FY2020–2021 | Public dataset synthetic and anonymized for NDA compliance*
