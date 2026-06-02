# Public-Safe Consulting Bid Accuracy Analysis - Project Summary

**Dataset:** 279 synthetic project records
**Scope:** Bid-to-invoice discrepancy analysis for a consulting-style workflow

---

## Project Context

This project is a public-safe case study based on a common consulting analytics problem: estimated project bids do not always match final invoices. The portfolio version uses synthetic data so the workflow can be shared openly without publishing protected client records or internal operational details.

The central question is straightforward: what factors help explain the gap between quoted project estimates and final invoiced amounts?

---

## What Was Done

- Built a synthetic project dataset with project type, client group, consultant group, department ownership, cost flags, estimate, invoice, and project cost fields.
- Created a discrepancy outcome variable defined as invoice total minus estimated bill.
- Reviewed project, client, staffing, and process variables through exploratory analysis.
- Tested multiple OLS regression models to compare explanatory value across predictor groups.
- Translated the results into consulting-style process recommendations.

---

## Main Takeaways

- **Grouped patterns can matter more than broad categories.** Consultant and client groupings can help identify where repeated calibration issues may exist.
- **The workflow is diagnostic, not punitive.** The goal is to improve estimate quality, not assign blame to individuals or accounts.
- **Operational flags deserve review.** Travel, shipping, department ownership, and project type can all shape estimate quality.
- **Data quality matters.** Missing or unlisted ownership fields can become useful signals when interpreted carefully.
- **Synthetic data changes the claim.** The results demonstrate analytical judgment and communication skill; they should not be read as factual findings about any real organization.

---

## What This Demonstrates

This project demonstrates several skills that matter in consulting and organizational analytics work:

1. Framing an operational problem in analytical terms.
2. Building a public-safe data structure that avoids protected records.
3. Comparing model specifications instead of relying on one result.
4. Interpreting statistical output in ways that connect back to process decisions.
5. Communicating practical next steps without overstating certainty.

---

## Bottom Line

This project works as a public portfolio case because it shows how an applied analytics workflow can move from an ambiguous business concern to a usable dataset, interpretable findings, and concrete process recommendations while keeping the public artifact safely separated from protected source material.
