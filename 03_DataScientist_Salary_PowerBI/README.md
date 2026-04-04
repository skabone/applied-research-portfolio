# The Modern Data Scientist Market in the United States (2021)
**Tools:** Python · RapidMiner · Power BI | **Domain:** Labor Market Analytics / Workforce Intelligence

---

## Overview

An exploratory analysis of 742 data science job postings scraped from Glassdoor, examining salary distribution, geographic concentration, organizational characteristics, and technical tool demand across DS, DA, Data Engineer, and Senior DS roles.

## Key Findings

- **Python is universally required** — and becomes even more dominant at senior levels alongside deep learning frameworks (Keras, PyTorch)
- **Coastal markets dominate** — California, Massachusetts, and New York account for the highest role volume, salary, and seniority. The effect intensifies as roles become more senior.
- **The typical hiring organization** is large (1,001–5,000 employees), young (<50 years), private, and in IT or biotech
- **Flink and Google Analytics** are nearly absent from postings — low-priority tools for most job seekers
- **Degree requirements escalate with pay** — BA covers entry-level; MA/Ph.D. become requirements for senior and research roles

## Files

| File | Description |
|------|-------------|
| `DS_Salary_Data_Prep.py` | Python script replicating data cleaning (originally done in RapidMiner) |
| `Executive_Brief.md` | 1-page summary for HR and workforce planning leaders |
| `DS_Salary_Project_Report.md` | Full written report with methodology, findings, and discussion |
| `ds_salary_original.csv` | Raw Kaggle dataset (742 rows × 42 columns) |
| `dashboard_1.png` · `dashboard_2.png` · `dashboard_3.png` | Power BI dashboard screenshots |

## Dashboard

The interactive Power BI dashboard includes salary maps (3D and 2D), tool demand analysis via Key Influencers, a job description word cloud, and salary breakdowns by company and personal features. Global filters allow cross-tab exploration by industry, seniority, degree, and organization size.

*Power BI file (.pbix) available on request — file size exceeds GitHub's 25MB display limit.*

---

*Mintay Misgano | People Analytics Portfolio | Seattle Pacific University, 2022*
