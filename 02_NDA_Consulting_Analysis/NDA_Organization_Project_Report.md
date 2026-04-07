# NDA Organization Bid Accuracy Analysis — Project Report
### Identifying Drivers of Estimation Discrepancy in an Anonymized Consulting Engagement

**Author:** Mintay Misgano, PhD
**Date:** March 2023
**Tools:** R, RStudio, OLS Regression
**Dataset:** 279 project records, Fiscal Years 2020–2021

> **Confidentiality Note:** This project was completed under a Non-Disclosure Agreement (NDA). The organization is presented here as "NDA Organization." Client and personnel identifiers have been anonymized for public presentation. The analytical workflow, variable structure, and findings reflect the original project, but identifying details have been removed.

---

## Abstract

This project examines bid-to-invoice discrepancy in an anonymized consulting engagement using two years of project records (N = 279, FY2020-2021). Ten ordinary least squares (OLS) regression models were estimated to identify which project-level, personnel, and client-level factors best predict the difference between estimated project bids and actual invoiced amounts. Four of five OLS assumptions were violated, so the results are interpreted cautiously using a more stringent significance threshold (p < 0.01). The strongest recurring signals came from consultant identity and a small number of client organizations, while industry sector and assessed position rank were not meaningful standalone predictors. Completed as graduate coursework using protected client data, the project is best read as a consulting analytics case that demonstrates how an operational pricing question can be translated into structured analysis.

---

## 1. Introduction and Business Problem

Consulting firms operating on a project-bid model face an inherent estimation challenge: they must quote a project cost before the scope of work is fully known. In this engagement, the anonymized client organization provided assessment-related services in the public safety sector, where project scope, travel requirements, and client-specific variation all had the potential to shift actual costs away from quoted estimates.

Two failure modes arise from bid inaccuracy:

- **Overestimation** (bid too high relative to actual invoice): The firm risks losing contracts to lower-bidding competitors, or eroding client confidence if adjusted invoices differ substantially from quotes.
- **Underestimation** (bid too low): The firm absorbs costs beyond what was quoted, directly damaging profitability and potentially compromising service delivery.

Over a two-year period, the organization accumulated 279 project records containing estimated bids, actual invoiced amounts, project metadata, and personnel information. This analysis uses that dataset to answer a central business question:

> *Which project-level, personnel, and client-level factors most strongly predict the discrepancy between estimated bids and actual invoiced amounts?*

The dependent variable (DV) is defined as:

```
DV = Invoice Total − Estimated Bill
```

- **Positive DV** → underestimation (charged more than projected)
- **Negative DV** → overestimation (charged less than projected)
- **DV = 0** → perfect estimation

---

## 2. Analytical Framing

This project sits at the intersection of consulting operations and organizational analytics. In project-based service work, pricing accuracy depends not only on broad service categories but also on the interaction of consultant judgment, client-specific complexity, and internal process quality. That framing is useful here because the practical question is not simply whether bids are off. It is whether the mismatch appears to come from broad structural features or from narrower patterns that the organization could calibrate more directly.

The analysis uses OLS regression as an exploratory tool rather than as a final predictive system. Given the structure of the dataset and the business question, the value of the model is interpretive: it helps identify which variables are consistently associated with discrepancy and which apparently plausible explanations do not carry much signal in this sample.

---

## 3. Data and Methods

### 3.1 Data Source and Structure

The dataset combines two fiscal years (2020 and 2021) of internal project records from the anonymized client organization's project management system. Records were pre-merged and cleaned in Excel prior to R import. A year flag was added to allow year-level comparisons. The final analytical dataset contains 279 observations across 15 variables after removing records with missing values on critical fields (Invoice Total, Estimated Bill, Client ID).

### 3.2 Variable Definitions

| Variable | Type | Description |
|----------|------|-------------|
| `PL` (Project Lead) | Character | Anonymized consultant identifier (Consultant A–K) |
| `AC` (Associate Consultant) | Logical | Whether an associate consultant was assigned |
| `ID` (Client ID) | Integer | Anonymized client organization identifier |
| `Industry` | Factor | Public safety sector (fire, police, corrections, transit, general, dispatch) |
| `Rank` | Factor | Position level being assessed (sergeant, firefighter, etc.) |
| `PType` (Project Type) | Factor | Assessment center (AC), written exam (WE), product, general, transit, licensing |
| `BTravel` (Billable Travel) | Logical | Whether the project required billable travel |
| `BShip` (Billable Shipping) | Logical | Whether the project required billable shipping |
| `InvoiceT` (Invoice Total) | Numeric | Actual amount invoiced to the client |
| `PCost` (Project Cost) | Numeric | Actual project costs incurred |
| `Bill` (Estimated Bill) | Numeric | Estimated bid amount |
| `Net` | Numeric | Estimated profit (Bill − estimated costs) |
| `NetProfit` | Numeric | Reported net profit from records |
| `Materials` | Factor | Department responsible: Operations, Consulting, or unlisted |
| `Year` | Integer | Fiscal year (2020 or 2021) |

### 3.3 Data Preparation

**Missing Data Handling:**
- `AC` (150 missing): Converted to logical — `TRUE` if any associate was assigned, `FALSE` if blank (reflecting genuinely unassigned, not unknown).
- `Materials` (90 missing): Retained as a three-level factor, allowing the model to test whether unlisted department has a systematic effect on estimation error.
- `PCost` (37 missing): Treated as zero per business-contact approval — blank entries reflected projects with no tracked costs, not truly unknown costs.
- `InvoiceT`, `Bill`, `ID` (small N): Rows deleted — these fields are critical to DV construction and cannot be imputed.

**Feature Engineering:**
Three derived variables were created:
- `DV = InvoiceT − Bill` — the primary dependent variable (bid discrepancy in dollars)
- `NP = InvoiceT − PCost` — calculated net profit (invoice minus actual project costs)
- `NP1 = NP − NetProfit` — reporting inconsistency metric (difference between calculated and reported net profit)

### 3.4 Analytical Approach

Ten OLS regression models were estimated, organized to address the business question from multiple angles:

| Model | Predictors |
|-------|-----------|
| M1 | All predictors (full model) |
| M2 | All predictors, singularities removed |
| M3 | Project Lead only |
| M4 | Client Organization (ID) only |
| M5 | Industry only |
| M6 | Rank only |
| M7 | Project Type only |
| M8 | Department (Materials) only |
| M9 | Industry + Rank combined |
| M10 | Financial predictors (actual values only) |

Models were selected based on F-statistic significance, followed by adjusted R², MAE, and RMSE. The selection criterion hierarchy was: significance → parsimony → predictive accuracy.

---

## 4. Assumption Testing

OLS regression requires five key assumptions. All five were formally tested prior to modeling.

### Summary Table

| Assumption | Test Used | Result | Status |
|------------|-----------|--------|--------|
| Linearity | LOESS visual inspection | Non-linear relationships observed | ❌ Violated |
| Normality of Residuals | Anderson-Darling; Shapiro-Wilk | p < 0.001 on both tests | ❌ Violated |
| Homoscedasticity | Breusch-Pagan test | p > 0.05 | ✅ Met |
| No Multicollinearity | Correlation matrix | \|r\| > 0.7 among financial predictors | ❌ Violated |
| Independence | Structural inspection | Repeated PL and ID in data | ❌ Violated |

### Analytical Adjustment

Because four of five assumptions are violated, a **more stringent significance threshold of p < 0.01** was adopted (versus the standard p < 0.05). This reduces the probability of Type I error given the elevated risk from assumption violations. All results are reported with this threshold.

**Normality detail:** The Anderson-Darling test (A = 14.72, p < 0.001) and Shapiro-Wilk test (W = 0.891, p < 0.001) both reject normality of residuals from the base model. This is consistent with the observed right-skew in the DV distribution.

**Multicollinearity detail:** The correlation matrix reveals that `InvoiceT`, `NP`, `Bill`, and `Net` are highly intercorrelated (|r| > 0.7). Models including multiple financial predictors simultaneously should be interpreted with caution; coefficients may be unstable.

**Homoscedasticity detail:** The Breusch-Pagan test (BP = 3.12, p = 0.37) fails to reject the null of constant variance — this assumption is met, which provides some stability in the standard errors of coefficient estimates.

---

## 5. Results

### 5.1 Descriptive Summary of DV

| Statistic | Value |
|-----------|-------|
| N | 279 |
| Mean DV | +$412 |
| Median DV | +$75 |
| SD | $3,847 |
| Min | −$18,400 |
| Max | +$24,600 |
| Projects underestimated (DV > 0) | 161 (58%) |
| Projects overestimated (DV < 0) | 102 (37%) |
| Perfect estimates (DV = 0) | 16 (6%) |

The firm underestimates more often than it overestimates (58% vs. 37%), but the mean and median are close to zero, suggesting the overall portfolio balances out — masking significant project-level variance.

### 5.2 Model Comparison

| Model | F-Statistic | p-value | Adj. R² | MAE | RMSE | Significant |
|-------|-------------|---------|---------|-----|------|-------------|
| M1: All Predictors (Full) | 8.41 | < 0.001 | 0.612 | $891 | $1,847 | ✓ Yes |
| M2: All Predictors (No Singularities) | 7.93 | < 0.001 | 0.589 | $912 | $1,903 | ✓ Yes |
| M3: Project Lead | 4.22 | < 0.001 | 0.134 | $1,841 | $2,847 | ✓ Yes |
| M4: Client Organization | 3.87 | < 0.001 | 0.319 | $1,612 | $2,541 | ✓ Yes |
| M5: Industry | 1.14 | 0.341 | 0.012 | $2,103 | $3,204 | No |
| M6: Rank | 0.98 | 0.452 | 0.008 | $2,211 | $3,319 | No |
| M7: Project Type | 2.91 | 0.013 | 0.042 | $1,998 | $3,087 | ✓ Yes |
| M8: Department (Materials) | 3.44 | 0.009 | 0.038 | $2,041 | $3,172 | ✓ Yes |
| M9: Industry + Rank | 1.02 | 0.428 | 0.011 | $2,187 | $3,298 | No |
| M10: Financial (Actual) | 412.3 | < 0.001 | 0.998 | $98 | $147 | ✓ Yes |

*Note: M10's near-perfect R² reflects that InvoiceT and Bill together algebraically construct DV — this model is financially informative but not predictively useful ex ante.*

### 5.3 Significant Predictors (p < 0.01)

**Project Lead (M3, p < 0.001):**
Consultant identity explains approximately 13% of variance in bid discrepancy (Adj. R² = 0.134). Three consultants show significant positive DV (systematic underestimation); two show significant negative DV (systematic overestimation). These patterns are stable across project types, suggesting individual calibration differences rather than project-mix effects.

**Client Organization (M4, p < 0.001):**
Client ID explains approximately 32% of variance (Adj. R² = 0.319), making it the strongest single categorical predictor. Four specific clients (out of 78 unique organizations) drive the majority of this effect — each showing DV extremes of $3,000–$8,000 above or below zero. These four clients likely represent systematically misunderstood project complexity.

**Project Type (M7, p = 0.013):**
Assessment center (AC) projects show the largest median underestimation; licensing and product projects show lower discrepancy variance. Written exam (WE) projects perform more accurately than AC projects on average.

**Department (M8, p = 0.009):**
Projects with no department listed (Materials = NA) show systematically higher overestimation than Operations- or Consulting-tracked projects. This suggests that unlisted projects may share structural characteristics (different team composition, less experienced oversight) that current estimates don't capture.

**Industry Sector (M5) and Rank (M6): Not significant.** The public safety sector served and the position level assessed do not independently predict estimation error at the p < 0.01 threshold.

### 5.4 Model Interpretation

**M1 (Full Model)** is the most useful model for broad business interpretation because it retains the widest set of project, client, and staffing variables. Its value is not just fit. It also helps separate the variables that appear actionable in practice from those that are less informative in this dataset.

---

## 6. Discussion and Interpretation

The results suggest that the organization's estimation problem is not purely structural. The firm does not systematically mis-price entire sectors or position types; instead, the strongest signals cluster around specific consultant and client patterns where estimation assumptions appear to break down.

This distinction matters because it changes the likely response. Structural problems would call for broad pricing-model changes. More localized patterns point instead toward targeted audits, consultant calibration, and client-specific adjustments.

The significance of department tracking (Materials) is best interpreted as a process-quality signal. When a project lacks department attribution, it is associated with worse estimation outcomes. That likely reflects broader issues in project intake, oversight, or record-keeping rather than a department effect in isolation.

The non-significance of industry sector and rank is also useful. It rules out an entire class of broad explanations and keeps attention on the narrower variables that appear more relevant in this dataset.

---

## 7. Recommendations

### 1. Audit the Highest-Discrepancy Client Organizations
A small number of clients account for a disproportionate share of estimation error. An internal review of archived project files for these organizations could help surface recurring scope, logistics, or pricing patterns that are not captured in the current estimation process.

### 2. Conduct Structured Estimate Debriefs with Key Consultants
The consultant-level patterns in the data suggest a calibration opportunity. A structured review comparing estimate sheets to final invoices by line item could help identify where assumptions about labor, travel, shipping, or scope differ from realized project costs.

### 3. Revisit the Travel Expense Estimation Formula
Projects with billable travel show a consistent pattern of overestimation. Reviewing the existing travel assumptions against historical travel records could help narrow one of the clearest recurring discrepancy sources.

### 4. Make Department Attribution a Required Field
Approximately 32% of projects had no department (Materials) recorded. Requiring this field during project intake would improve both operational visibility and future analytical quality.

### 5. Standardize Labor Hour Tracking at the Project Level
Project cost tracking was incomplete for part of the sample. More consistent labor-hour and cost tracking would improve future estimation review and make follow-up analyses more reliable.

---

## 8. Limitations

**Sample Size:** With 279 observations over two years, some factor levels are underpowered — particularly rare industries and position ranks. Results for infrequent categories should be interpreted cautiously and validated with additional data.

**Assumption Violations:** Four of five OLS assumptions were violated. The p < 0.01 threshold mitigates but does not eliminate the risk of false positives. Mixed-effects regression (accounting for the clustered structure of repeated project leads and client organizations) is the appropriate next step given more data.

**Missing Labor Cost Data:** PCost was imputed as zero for 37 projects. If these projects had actual unreported costs, this introduces systematic error into both DV and NP calculations. The direction of this bias is unknown without additional data.

**Single Time Window:** Two fiscal years may not generalize beyond 2020–2021. Market competition, client mix, pricing strategy, and staff composition all change. Annual replication is recommended to establish whether findings are stable over time.

**Definitional Ambiguity in NP1:** The reporting inconsistency variable (NP1 = calculated net profit − reported net profit) flagged meaningful variance. This could reflect legitimate accounting differences, data entry inconsistencies, or systematic misreporting. Further investigation into the source of NP1 variance is warranted.

---

## 9. Conclusion

This analysis identified a set of recurring drivers of bid-to-invoice discrepancy in an anonymized consulting engagement. The strongest signals point more toward specific client-consultant patterns than toward broad structural factors like industry sector or assessed position rank. From a consulting standpoint, that is useful because it suggests the problem may be addressed through targeted review, calibration, and data-quality improvements rather than wholesale redesign of the pricing model.

Reasonable next steps would be:

1. Improve intake and tracking fields so future projects are easier to analyze
2. Conduct structured debriefs on the consultant patterns that appear most discrepant
3. Review archived records for the client organizations with the largest recurring discrepancy
4. Rerun this analysis after one additional year of data with the improved dataset
5. Explore mixed-effects regression to properly account for the clustered structure of the data

Overall, this project demonstrates how a consulting analytics engagement can move from an operational problem to a structured statistical analysis and then to targeted process recommendations, even when the available data are imperfect.

---

## References

Cohen, J., Cohen, P., West, S. G., & Aiken, L. S. (2003). *Applied multiple regression/correlation analysis for the behavioral sciences* (3rd ed.). Lawrence Erlbaum Associates.

Field, A. (2018). *Discovering statistics using IBM SPSS statistics* (5th ed.). SAGE Publications.

Flyvbjerg, B. (2006). From Nobel Prize to project management: Getting risks right. *Project Management Journal, 37*(3), 5–15. https://doi.org/10.1177/875697280603700302

Hill, C. W. L., & Jones, G. R. (2007). *Strategic management: An integrated approach* (8th ed.). Cengage Learning.

Hogg, R. V., McKean, J. W., & Craig, A. T. (2019). *Introduction to mathematical statistics* (8th ed.). Pearson.

Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). *Noise: A flaw in human judgment*. Little, Brown Spark.

Kutner, M. H., Nachtsheim, C. J., Neter, J., & Li, W. (2005). *Applied linear statistical models* (5th ed.). McGraw-Hill Irwin.

Meehl, P. E. (1954). *Clinical versus statistical prediction: A theoretical analysis and a review of the evidence*. University of Minnesota Press.

Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to linear regression analysis* (6th ed.). Wiley.

Nunnally, J. C., & Bernstein, I. H. (1994). *Psychometric theory* (3rd ed.). McGraw-Hill.

Schmidt, F. L., & Hunter, J. E. (1998). The validity and utility of selection methods in personnel psychology: Practical and theoretical implications of 85 years of research findings. *Psychological Bulletin, 124*(2), 262–274. https://doi.org/10.1037/0033-2909.124.2.262

Zitzmann, S., & Hecht, M. (2019). Going beyond convergence in Bayesian estimation: Why precision matters too and how to assess it. *Structural Equation Modeling: A Multidisciplinary Journal, 26*(4), 646–661.

---

*Analysis by Mintay Misgano, PhD | R / RStudio | Data: 279 observations, FY2020–2021 | Public version anonymized for NDA compliance*
