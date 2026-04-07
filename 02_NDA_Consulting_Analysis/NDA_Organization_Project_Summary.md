# NDA Organization Bid Accuracy Analysis — Project Summary

**Dataset:** 279 anonymized project records from FY2020-2021  
**Scope:** Bid-to-invoice discrepancy analysis for a consulting organization

---

## Project Context

This project was completed as part of graduate coursework in analytics using a real consulting engagement under a Non-Disclosure Agreement. The public version preserves the analytical structure of the project while anonymizing the organization, personnel, and client identities.

The central question was straightforward: what factors help explain the gap between quoted project estimates and final invoiced amounts?

---

## What Was Done

- Combined and cleaned two years of project records
- Created a discrepancy outcome variable defined as actual invoice minus estimated bid
- Reviewed project, client, staffing, and financial variables through exploratory analysis
- Tested multiple OLS regression models to compare explanatory value across different predictor groups
- Translated the results into process and consulting implications for pricing accuracy

---

## Main Takeaways

- **Consultant and client patterns mattered more than broad project categories.** The strongest signals came from specific project leads and specific client organizations rather than from industry sector alone.
- **The estimation problem looked relational rather than purely structural.** That suggests calibration and account-specific review may be more useful than changing the entire pricing system at once.
- **Travel estimates appeared to be systematically high.** This points to a concrete estimation rule that could be reviewed using historical records.
- **Data quality mattered.** Missing department or intake information appeared alongside poorer bid accuracy, suggesting that process discipline and analytic quality are linked.
- **Not every intuitive variable was useful.** Industry sector and assessed rank did not independently explain much estimation discrepancy in this dataset.

---

## What This Demonstrates

This project demonstrates several skills that matter in consulting and organizational analytics work:

1. Framing a real operational problem in analytical terms
2. Cleaning and anonymizing internal business data for responsible analysis
3. Comparing multiple model specifications instead of relying on one result
4. Interpreting statistical output in ways that connect back to process decisions
5. Communicating practical next steps while staying within NDA and data-limit boundaries

---

## Bottom Line

This project works well as a consulting case because it shows more than statistical output. It shows how an applied analytics project can move from an ambiguous business concern to a usable dataset, interpretable findings, and concrete process recommendations without overstating certainty or exposing protected client information.
