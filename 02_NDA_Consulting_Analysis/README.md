# NDA Organization Bid Accuracy Analysis

**Author:** Mintay Misgano, PhD  
**Project Type:** Consulting case study using anonymized client data  
**Tools:** R, ggplot2, dplyr, OLS regression

---

## Overview

This project examines bid accuracy for an anonymized consulting organization that provides assessment services in the public safety sector. Using two fiscal years of project records, the analysis evaluates which project, client, and staffing factors are associated with the gap between estimated bids and actual invoiced amounts.

The project was completed as part of graduate coursework in analytics using a real consulting engagement conducted under a Non-Disclosure Agreement. All client and personnel identifiers have been anonymized for portfolio presentation.

---

## Key Findings

- Consultant identity and client organization were the strongest recurring signals in estimation discrepancy.
- Industry sector and assessed rank were not meaningful standalone predictors in this dataset.
- Travel-related estimates showed a pattern of overestimation.
- Missing department or intake information appeared to be associated with poorer estimation quality.
- The analysis suggests that bid accuracy issues were concentrated in specific consultant-client patterns rather than broad service categories.

---

## Read This Project

- Start here for the project overview and file map
- Read `NDA_Organization_Project_Summary.md` for the short consulting-case narrative
- Read `NDA_Organization_Project_Report.md` for methods, results, and limitations in full
- Use `NDA_Organization_Project_Report.Rmd` as the source file for the long-form report

---

## Project Files

| File | Purpose |
|---|---|
| `NDA_Organization_Project_Summary.md` | Short narrative summary of the project and what it demonstrates |
| `NDA_Organization_Project_Report.md` | Full public-facing report |
| `NDA_Organization_Project_Report.Rmd` | R Markdown source file for the report |
| `data.csv` | Anonymized working dataset used in the analysis |

---

## Data and Confidentiality Note

This project uses anonymized client data from a real consulting engagement. The organization, personnel, and client entities are masked as part of NDA compliance. The public materials are intended to demonstrate analytical and consulting workflow, not to disclose client-sensitive details.
