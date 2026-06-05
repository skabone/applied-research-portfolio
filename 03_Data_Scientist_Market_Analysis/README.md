# U.S. Data Scientist Market Analysis (2021)

**Author:** Mintay Misgano, PhD  
**Tools:** Python, RapidMiner, Jamovi, Power BI  
**Dataset:** Glassdoor job-posting data via Kaggle

---

## Overview

This project explores the 2021 U.S. data-science job market using a 742-row public feature extract derived from a Glassdoor job-posting dataset published on Kaggle. The analysis examines salary patterns, geographic concentration, employer characteristics, degree requirements, and tool demand across data scientist, data analyst, data engineer, and senior data scientist roles.

Completed as graduate coursework in data mining and analytics, the project is centered on an interactive Power BI dashboard supported by reproducible data-preparation steps.

---

## Key Findings

- Python appeared as the most consistently requested technical tool across role types.
- California, Massachusetts, and New York showed the highest concentration of roles and salary ranges.
- Hiring organizations were commonly large, relatively young, and private, with concentration in IT and biotech-related sectors.
- Degree requirements tended to increase with seniority and compensation level.
- Some tools, such as Flink and Google Analytics, appeared very rarely in the postings.

---

## Project Files

- `README.md` provides the project overview and file map.
- `Data_Scientist_Market_Project_Summary.md` provides the short narrative interpretation.
- `Data_Scientist_Market_Project_Report.md` provides methods, findings, and limitations in full.
- `Data_Scientist_Market_Data_Prep.ipynb` provides a rendered notebook version of the preparation workflow.
- `Data_Scientist_Market_Data_Prep.py` provides the script version.

---

## File Map

| File | Purpose |
|------|---------|
| `Data_Scientist_Market_Project_Summary.md` | Short narrative summary of the project and practical value |
| `Data_Scientist_Market_Project_Report.md` | Full project report with methods, findings, and limitations |
| `Data_Scientist_Market_Data_Prep.ipynb` | Rendered notebook companion for the preparation workflow |
| `Data_Scientist_Market_Data_Prep.py` | Reproducible data-preparation script |
| `ds_salary_public.csv` | Public feature-level analysis dataset used in the project |

---

## Data Note

This project uses a public feature-level extract derived from a Kaggle dataset of Glassdoor job postings. Raw job descriptions, company names, headquarters, competitors, and contact-bearing posting text are not stored in this repository. Salary ranges and company attributes should be treated as directional labor-market signals rather than authoritative compensation benchmarks.
