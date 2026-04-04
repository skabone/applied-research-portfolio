# Project Bid Accuracy Analysis — Executive Brief
**Client:** NDA Org — Organizational Survey & Assessment Firm | **Analyst:** Mintay Misgano | **Year:** 2023

---

## The Business Problem

A Pacific Northwest organizational assessment firm specializing in public safety pre-employment testing was losing competitive bids due to systematic mispricing. When projects were overestimated, lower-bidding competitors won the contract. When underestimated, the firm absorbed unrecovered costs. With project-based pricing and a relatively small annual volume (~150 projects/year), even moderate estimation error had material impact on revenue, client retention, and competitive positioning.

The firm needed to know: **which factors drive the gap between quoted estimates and actual invoices — and what can be done about it?**

---

## Approach

- Merged and cleaned two years of internal project records (2020–2021), yielding **279 completed consulting projects × 16 variables**
- Engineered the target metric: **Discrepancy (DV) = Actual Invoice − Estimated Bid** (positive = underestimate; negative = overestimate)
- Conducted assumption testing on all five OLS regression assumptions prior to modeling; adopted stricter p < 0.01 threshold due to assumption violations
- Ran **10 linear regression models**, testing categorical predictors (project lead, client, industry, project type) and financial predictors individually and in combination
- Selected the best model based on F-statistic, p-value, MAE, RMSE, and business interpretability

---

## Key Findings

- **Project lead matters most.** Specific consultants were significantly associated with consistent over- or under-estimation — not all consultants, but identifiable ones whose project patterns differ from peers.
- **Four client organizations drive outsized discrepancy.** Out of 78 unique clients, 4 accounted for the most statistically significant and directionally consistent estimation errors — all in the direction of underestimation (the firm charges less than it costs to serve them).
- **Billable travel estimates are systematically too high.** Projects requiring travel showed a consistent pattern of overestimation — the firm's travel buffer appears to exceed actual travel spend.
- **Industry and rank do not predict estimation error.** Whether a project is for fire, police, or corrections — or tests a sergeant vs. a captain — has no statistically significant effect on bid accuracy. Estimation problems are organizational and process-driven, not industry-driven.
- **Data gaps are themselves predictive.** Projects with no department recorded (32% of the sample) were significantly more likely to be overestimated, suggesting that incomplete intake processes correlate with poorer cost visibility.

---

## Recommendations

1. **Audit the four high-discrepancy clients** — a file review of past projects with these organizations should reveal complexity factors (scope shifts, custom deliverables, unusual logistics) that are not captured in current pricing formulas.
2. **Implement a consultant calibration process** — a structured debrief comparing estimate sheets to final invoices for the 2-3 consultants with the largest systematic discrepancies; this is a coaching opportunity, not a disciplinary one.
3. **Rebuild the travel cost estimation formula** — use two years of actual travel records to replace the current buffer-based approach with a data-driven model calibrated to project type and geography.
4. **Make Materials (department) a required intake field** — 90 missing values in this field both limits analytical insight and signals a process gap during project intake that likely contributes to estimation error.

---

## Impact

Closing even half the observed average discrepancy across the 4 high-risk clients and recalibrating consultant estimates could reduce revenue variance by an estimated 15–25% annually. More importantly, tighter bids — particularly on travel-heavy projects — would make the firm more competitive on contracts where it is currently being outbid by competitors with lower (possibly better-calibrated) proposals.

---

*Analysis by Mintay Misgano | Tools: R, RStudio, ggplot2, lmtest | Data: 279 projects, 2020–2021 | NDA Confidential — Client and personnel identifiers anonymized*
