# Consulting Bid Accuracy Analysis — Project Summary

- **Dataset:** 279 synthetic public records modeled from protected project records, FY2020–2021
- **Engagement:** Real consulting project completed under NDA

---

## The Problem

A regional assessment services firm operated on a project-bid model — quoting costs before the full scope of delivery was known. Over two fiscal years, they accumulated records showing that estimated bids and final invoiced amounts were frequently misaligned. The firm needed to understand what was driving that gap and where to focus calibration efforts.

This project was completed as part of a graduate consulting engagement. The central analytical question was: which project, personnel, and client factors are most consistently associated with the difference between what was estimated and what was actually invoiced?

For public presentation, the project uses a synthetic and anonymized version of the dataset. The public file preserves the structure of the real engagement while removing client, personnel, invoice, and operationally identifying details.

---

## Approach

The starting point was constructing a clean outcome variable — bid discrepancy, defined as invoice total minus estimated bill — and then examining which project-level features were associated with larger or more systematic gaps. Two years of records (N = 279) were combined, cleaned, and prepared in R, with missing values handled based on business logic reviewed with the project contact rather than assumed away.

From there, eight OLS regression models were compared, each testing a different slice of the predictors: project lead identity, client account, service area, project type, department ownership, operational flags, and financial predictors. Comparing models this way — rather than running one and calling it done — made it possible to distinguish which categories of information actually carry signal from which appear useful but don't hold up.

![Estimated bill compared with final invoice](docs/figures/eda-bill-vs-invoice-1.png)

The diagonal line represents perfect estimate accuracy. The spread around it shows why the firm needed more than a single average-error number: some projects were close to estimate, while others missed enough to warrant account- and consultant-level review.

---

## What Was Found

The strongest and most consistent signals came from consultant identity and specific client accounts, not from broad structural categories. Service area and broad project category, which seemed like plausible predictors, did not explain much discrepancy on their own. Travel estimates showed a recurring pattern of overestimation. Projects with missing department or intake ownership information tended to have worse bid accuracy — which pointed to a data quality and process discipline issue, not just an analytical gap.

![MAE and RMSE by model specification](docs/figures/results-viz-1.png)

The full model produces the lowest prediction error, but the single-predictor models are more useful diagnostically. The pattern supports a targeted response: review recurring account and project-lead patterns before considering a broad pricing redesign.

Because four of the five standard OLS assumptions were violated in this dataset, all results were interpreted cautiously using a conservative significance threshold (p < .01) and framed as diagnostics rather than definitive conclusions.

---

## Recommendations Delivered

- Begin review with grouped summaries by consultant and client account, where the most consistent patterns appeared.
- Document travel and shipping assumptions explicitly before quoting — that's where overestimation was most recoverable.
- Require department ownership at project intake so that "Unlisted" stops functioning as an invisible signal.
- Treat the OLS results as a starting point; a follow-up mixed-effects model would be more appropriate once the data quality issues are addressed.

---

## Bottom Line

This was a real operational problem from a protected consulting engagement. The public version uses synthetic data so the analysis can be shared safely, but the workflow still shows how the project moved from a loosely defined business concern to a structured dataset, a multi-model comparison, and specific process recommendations that a small consulting firm could act on without needing a data team. The findings were interpreted carefully within the limits of the data — not overstated.
