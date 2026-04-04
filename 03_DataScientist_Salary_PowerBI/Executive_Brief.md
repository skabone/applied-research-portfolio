# Data Scientist Salary Market Analysis (2021) — Executive Brief
**Dataset:** Kaggle / Glassdoor Scrape | **Analyst:** Mintay Misgano | **Year:** 2022

---

## The Business Problem

For early-career data professionals and HR teams building analytics functions, the data science labor market is notoriously opaque. Salary ranges vary wildly by location, seniority, and employer type — and job postings rarely reveal what technical skills actually drive compensation. This project asks: **where are DS roles concentrated, what do hiring organizations look like, and which technical skills most predict role type and pay?**

---

## Approach

- Sourced 742 data science job postings scraped from Glassdoor (via Kaggle), covering 42 attributes including salary estimates, company metadata, location, and tech stack requirements
- Cleaned and prepared data using RapidMiner (Python script included): removed duplicate/redundant columns, converted 16 binary tool indicators to boolean, resolved a known location entry error, standardized salary fields
- Validated statistics independently in Jamovi to confirm data integrity across tools
- Built an interactive multi-tab Power BI dashboard with global filters enabling cross-tab exploration by industry, size, seniority, degree, and job type
- Applied Key Influencers visual to identify which tools most strongly predict each role type (DS, DA, Data Engineer, Sr. DS)

---

## Key Findings

- **Python dominates — but the profile shifts with seniority.** Python and Excel are broadly required, but as roles increase in seniority and pay, Python and Keras become significantly more important while general tools recede.
- **Coastal concentration is real and intensifies at the top.** California, Massachusetts, and New York account for the highest role volume and salary. This effect strengthens as seniority and degree requirements increase.
- **The typical hiring organization is large, young, and private.** Most DS-hiring firms are 1,001–5,000 employees, under 50 years old, and private (410 vs. 193 public). IT, biotech/pharma, and business services dominate by sector.
- **Role ratings cluster tightly.** DS-hiring organizations rate between 3.5–4.0 out of 5 — a narrow band suggesting either consistent employee satisfaction or Glassdoor rating compression.
- **Flink and Google Analytics are nearly irrelevant.** Both tools appear in a negligible share of postings — not worth prioritizing for most DS job seekers.
- **Degree requirements escalate with pay.** BA degrees cover entry-level roles; MA and Ph.D. requirements increase sharply as role level and compensation rise.

---

## Recommendations

1. **For job seekers:** Prioritize Python fluency above all other tools — it is the single most consistent signal across all DS role types. Add Keras/deep learning frameworks as the target moves to senior or research-oriented roles.
2. **For HR/Talent teams building DS functions:** The compensation benchmarks in this analysis suggest geographic premiums are real — remote-first hiring strategies can access equivalent talent at lower cost outside CA/MA/NY.
3. **For workforce planners:** The concentration of DS roles in IT, biotech, and business services suggests cross-industry demand is uneven — adjacent industries may face talent shortages as DS adoption spreads.

---

## Impact

An interactive dashboard enables HR leaders, hiring managers, and job seekers to filter by industry, seniority, degree, and location — instantly surfacing the salary range and tool profile relevant to their specific context. This moves compensation benchmarking from static reports to a self-serve analytical tool.

---

*Analysis by Mintay Misgano | Tools: Python, RapidMiner, Jamovi, Power BI | Data: 742 job postings, Glassdoor via Kaggle, 2021*
