# Data — U.S. Data Scientist Market Analysis (2021)

## `ds_salary_public.csv`

A public, feature-level extract derived from a Kaggle release of 2021 Glassdoor job postings for data-science and related roles.

- **Rows:** 742 job postings
- **Fields:** 36 analysis columns (role, salary midpoint and range, location, employer attributes, and 16 boolean tool/skill flags)
- **Source:** Igamberdiev, T. (2021). *Data Science Job Salaries* [Data set]. Kaggle. https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

## What is and isn't included

This extract keeps only feature-level fields needed for the analysis. Raw job-description text, company names, headquarters, competitor lists, and any contact-bearing posting text are excluded at the source, so nothing identifying or contact-bearing is published here.

## Interpretation cautions

Salary fields are Glassdoor-estimated or employer-provided ranges, not verified compensation, and the postings are a non-probability convenience sample from a single 2021 scrape. Treat all figures as directional labor-market signals rather than authoritative benchmarks. For verified wages, see the U.S. Bureau of Labor Statistics Occupational Employment and Wage Statistics program (https://www.bls.gov/oes/).

## Reproducing the analysis

```bash
python3 04_Source_Code.py
```

This loads `data/ds_salary_public.csv`, prints every statistic cited in the README, summary, and report, and writes the seven figures to `docs/figures/`. The executed `03_Analysis_Notebook.ipynb` shows the same analysis with figures inline.
