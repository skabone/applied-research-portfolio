# Public-Safe Consulting Bid Accuracy Analysis - Project Report

## Executive Summary

This project demonstrates a consulting analytics workflow for diagnosing bid-to-invoice discrepancy. The public version uses a fully synthetic dataset with 279 project records. It preserves the structure of an applied pricing-quality problem while excluding protected source material such as real client records, personnel names, customer IDs, invoice numbers, contact fields, exact dates, and operational notes.

The analysis compares several ordinary least squares (OLS) model specifications to identify which synthetic project features are associated with the difference between estimated bill and final invoice. In this demo dataset, the strongest explanatory signals come from combinations of consultant group, client group, project type, department ownership, and operational flags. The result is a public-safe case study that shows problem framing, data preparation, modeling judgment, and stakeholder-ready recommendations.

Important interpretation note: the results below are findings from a synthetic demo dataset. They demonstrate an analytical workflow and should not be read as factual findings about any real organization.

---

## 1. Business Question

Consulting teams that quote fixed or semi-fixed project estimates need a way to monitor whether estimates are calibrated to actual delivery costs. The central question for this case study is:

> Which project, client, staffing, and process factors are associated with bid-to-invoice discrepancy?

The target variable is:

```text
bid_discrepancy = invoice_total - estimated_bill
```

- Positive values indicate underestimation: the final invoice is higher than the estimate.
- Negative values indicate overestimation: the final invoice is lower than the estimate.
- Values near zero indicate stronger estimate calibration.

---

## 2. Public Data Design

The public dataset, `data.csv`, is synthetic. It contains 279 generated project records and 16 fields:

| Field | Description |
|---|---|
| `project_id` | Synthetic row identifier |
| `project_year` | Synthetic year grouping (`Year_1`, `Year_2`) |
| `consultant_id` | Synthetic consultant grouping (`Consultant_A` through `Consultant_H`) |
| `client_id` | Synthetic client grouping (`Client_001` style labels) |
| `service_area` | Generalized service grouping |
| `project_type` | Generalized project category |
| `department_owner` | Operations, Consulting, or Unlisted |
| `associate_assigned` | Whether a support consultant was assigned |
| `billable_travel` | Whether travel was billable |
| `billable_shipping` | Whether shipping was billable |
| `candidate_count` | Synthetic project volume indicator |
| `estimated_bill` | Synthetic quoted amount |
| `invoice_total` | Synthetic final invoice amount |
| `project_cost` | Synthetic delivery cost |
| `bid_discrepancy` | Invoice minus estimate |
| `net_profit` | Invoice minus project cost |

The dataset is designed for portfolio demonstration only. It is not a masked copy of a client system.

---

## 3. Analytical Approach

The workflow follows four steps:

1. Inspect the distribution of bid discrepancy.
2. Compare model specifications using OLS regression.
3. Evaluate explanatory value using adjusted R-squared, MAE, and RMSE.
4. Translate patterns into process recommendations.

The analysis uses OLS as an interpretive tool. In a real consulting environment, follow-up work would include residual diagnostics, mixed-effects modeling for repeated client and consultant groups, and review with business owners before any operational decision.

---

## 4. Descriptive Results

| Statistic | Value |
|---|---:|
| Records | 279 |
| Mean bid discrepancy | 656.1 |
| Median bid discrepancy | 692.6 |
| Standard deviation | 1086.2 |
| Minimum | -2640.1 |
| Maximum | 4157.0 |
| Underestimated projects | 202 |
| Overestimated projects | 77 |

The synthetic data is intentionally noisy. That makes the project more realistic as a diagnostic workflow: model results are useful for narrowing attention, but they are not strong enough to support automated pricing decisions.

---

## 5. Model Comparison

| Model | Predictors | Adjusted R-squared | MAE | RMSE | p-value |
|---|---|---:|---:|---:|---:|
| Full diagnostic model | Consultant, client, service area, project type, department, operational flags, volume, estimate, cost | 0.498 | 548.2 | 664.5 | < .001 |
| Consultant group | Consultant only | 0.099 | 808.0 | 1015.9 | < .001 |
| Client group | Client only | 0.164 | 716.1 | 903.7 | < .001 |
| Project type | Project type only | 0.101 | 825.0 | 1018.9 | < .001 |
| Department ownership | Department only | 0.016 | 855.8 | 1071.5 | .039 |
| Operational model | Project type, department, travel, shipping, associate assignment, volume | 0.204 | 756.1 | 947.8 | < .001 |

The full diagnostic model explains the most variance in the synthetic data, but the smaller models are more useful for communicating where an operations team might begin a review.

---

## 6. Interpretation

Three patterns are most useful in this public demo:

1. **Client and consultant groupings are diagnostic.** Repeated patterns by client or consultant group can point to calibration differences, scope ambiguity, or documentation gaps.
2. **Project type and operational flags add context.** Not all project categories carry the same level of estimation risk, and cost-related flags can change the expected discrepancy.
3. **Department ownership can function as a process-quality signal.** An "Unlisted" ownership category should not be treated as a simple missing value if it consistently appears with different outcomes.

The right interpretation is process-oriented. The analysis supports targeted review, estimate calibration, and data-quality improvement. It does not support individual blame or automated pricing rules on its own.

---

## 7. Recommendations

1. **Review high-discrepancy project groups.** Start with grouped summaries by client, consultant, and project type to identify recurring patterns.
2. **Standardize estimate assumptions.** Document assumptions for travel, shipping, project volume, and support staffing before quoting.
3. **Require ownership fields.** Make department ownership or intake owner a required field so future analyses do not rely on ambiguous blanks.
4. **Create estimate debriefs.** For projects with large discrepancy, compare the original estimate assumptions with actual delivery conditions.
5. **Use mixed-effects modeling as a next step.** Repeated client and consultant groups suggest that multilevel methods would be more appropriate for a production analysis.

---

## 8. Limitations

- The dataset is synthetic and designed for demonstration, not business inference.
- OLS is used for interpretability; real operational data would require stronger diagnostics and potentially mixed-effects modeling.
- Financial values are generated and rounded, so apparent precision should not be overinterpreted.
- The project intentionally excludes real source records, contacts, notes, and client-specific context.

---

## 9. Portfolio Value

This case study demonstrates how I approach a messy operational analytics problem: define a measurable outcome, build a transparent data structure, compare models, interpret results cautiously, and translate findings into process recommendations that a stakeholder could act on responsibly.
