# The Modern Data Scientist Market in the United States (2021)
### An Exploratory Analysis of Salary, Location, and Tool Demand Using Power BI

**Author:** Mintay Misgano — Industrial-Organizational Psychology / People Analytics, Seattle Pacific University
**Tools:** Python · RapidMiner · Jamovi · Power BI
**Dataset:** Kaggle — Glassdoor DS Job Postings · N = 742 job postings · 40 features (post-cleaning)

---

## Abstract

This project explores the 2021 United States data science labor market using a Glassdoor-scraped dataset of 742 job postings across 42 attributes. The analysis addresses three business questions: (1) what types of organizations are actively hiring data scientists and related roles, (2) which geographic markets offer the highest salary and role volume, and (3) which technical tools are most in demand — and how do tool requirements shift by role type and seniority. Data was cleaned in RapidMiner, validated in Jamovi, and visualized through an interactive multi-tab Power BI dashboard. Key findings include: Python is the universally dominant tool; coastal markets (CA, MA, NY) account for disproportionate role volume and compensation; and hiring organizations are predominantly large, young, and private, concentrated in IT and biotech sectors.

---

## 1. Introduction and Business Problem

The data science labor market is one of the fastest-growing and most widely discussed in the technology economy — yet it remains difficult to navigate for job seekers, HR teams, and workforce planners alike. Salary ranges published in aggregate often obscure meaningful variation by geography, seniority, industry, and technical skill profile. Hiring managers building analytics functions lack a clean market reference for what competitive compensation looks like in their sector. And job seekers — particularly those transitioning into data science from adjacent fields like psychology, business analysis, or research — often lack a clear signal about which technical investments will yield the highest career return.

This project was motivated by a personal question that is also a professional one: what does the data science job market actually look like, and where should someone position themselves to enter it successfully?

The three core research questions driving the analysis are:

1. What types of organizations are hiring data scientists and related roles (data analysts, data engineers, senior data scientists)?
2. Where are these roles geographically concentrated, and how does location interact with salary and seniority?
3. Which technical tools are most in demand across role types, and how do requirements shift as roles become more senior or specialized?

---

## 2. Data Description

### 2.1 Source

The dataset was retrieved from Kaggle. It was created by scraping job postings related to data science positions from Glassdoor using Selenium, capturing postings available during 2021. The raw dataset contains 742 rows and 42 columns.

### 2.2 Feature Overview

| Domain | Variables |
|--------|-----------|
| Job characteristics | Job Title, job_title_sim (simplified), seniority_by_title, Degree |
| Salary | Salary Estimate, Lower Salary, Upper Salary, Avg Salary(K), Hourly, Employer Provided |
| Company information | company_txt, Rating, Headquarters, Size, Founded, Type of Ownership, Industry, Sector, Revenue |
| Location | Job Location, Job Location (City, State) |
| Tools/languages required | Python, spark, aws, excel, sql, sas, keras, pytorch, scikit, tensor, hadoop, tableau, PowerBI, flink, mongo, Google Analytics (16 binary columns: 1 = required, 0 = not required) |
| Other | Job Description, Age (company age) |

### 2.3 Limitations of the Source Data

The data was scraped from Glassdoor — a self-reported, user-generated platform. Several limitations apply:

- Salary estimates are employer-provided or Glassdoor-estimated ranges, not verified compensation data. They should be treated as directional indicators, not precise benchmarks.
- The scrape captures a moment-in-time snapshot; it is not longitudinal and may not generalize to other years.
- The sample of 742 postings represents a subset of the full market — the sampling methodology of the scrape is unknown.
- A more authoritative source such as the Bureau of Labor Statistics Occupational Employment Statistics would strengthen any compensation benchmarking.

---

## 3. Data Preparation

Data cleaning was performed in RapidMiner and validated in Jamovi. The same steps are replicated in the accompanying Python script (`DS_Salary_Data_Prep.py`) for reproducibility.

### 3.1 Column Removal

Two columns were removed as uninformative:

- **Company Name:** A combined field containing company name and rating as a single string (e.g., "Microsoft 4.2"). Redundant with the separate `company_txt` and `Rating` columns.
- **Competitors:** Approximately 60% missing values. Not relevant to the core research questions about salary drivers, location, and tool demand.

Post-removal: 742 rows × 40 columns.

### 3.2 Column Renaming

Several columns were renamed for clarity and interpretability:
- `bi` → `PowerBI` (full product name)
- `Location` → `Job Location` (to disambiguate from `Headquarters`)
- `google_an` → `Google Analytics`

### 3.3 Binary Tool Column Conversion

All 16 tool/language columns (Python, spark, aws, excel, sql, sas, keras, pytorch, scikit, tensor, hadoop, tableau, PowerBI, flink, mongo, Google Analytics) were converted from integer (0/1) to boolean (False/True). This ensures correct aggregation behavior in Power BI and prevents inadvertent summation of binary indicators.

### 3.4 Data Entry Correction

One entry listed the job location as "Phila, PA." Cross-referencing against company size, headquarters, sector, and other records for the same company confirmed this referred to Philadelphia, PA. The value was corrected.

### 3.5 Missing Values

After the above steps, no missing values remained in the dataset — an atypically clean result attributable to the structured nature of the Glassdoor scrape template.

### 3.6 Power BI Finalization

After import into Power BI:
- All 16 tool columns were re-verified as True/False in the Data tab.
- Salary and pay variables were formatted as currency.
- Aggregation behavior was set: salary variables averaged (not summed); integer variables like Age set to non-summarized.

---

## 4. Visualization Approach

The Power BI dashboard was designed around the three core research questions, with cross-tab global filters enabling user-driven exploration. Dashboard structure:

| Tab | Key Visuals |
|-----|-------------|
| Salary by Location | 3D map (salary encoded as bar height) + 2D bubble map (salary encoded as circle size) |
| Company Profile | Industry, sector, size, ownership type, company age, rating distributions |
| Tool Demand | Key Influencers visual — select role type → see top tool predictors and prediction magnitude |
| Job Description Insights | WordCloud 2.0.0 of job description text |
| Salary Drivers | Salary vs. company features (age, rating, sector, industry, job title) |
| Seniority & Degree | Salary vs. seniority level and degree requirement |

**Global filters** (applied across all tabs): Organization Size, Industry, Job Title, Degree

**The Key Influencers visual** was the analytical centerpiece. It allows a user to select a specific role type (Data Scientist, Data Analyst, Data Engineer, Senior Data Scientist) and instantly see which tools most increase the likelihood of a posting belonging to that role type, along with the top feature combinations (segments) that characterize each role.

---

## 5. Findings

### 5.1 Geographic Distribution

Data science roles are heavily concentrated along the U.S. coasts. California, Massachusetts, and New York account for the highest role volume, highest average salary, and most senior role types. This coastal concentration intensifies as seniority and degree requirements increase — entry-level roles are distributed more broadly, but Ph.D.-level and senior roles cluster tightly in major metro areas on the coasts.

### 5.2 Organization Profile

The typical DS-hiring organization:
- Is **large** (1,001–5,000 employees)
- Is **young** (under 50 years old)
- Is **private** (410 private vs. 193 public companies)
- Is in **Information Technology, Biotech/Pharma, or Business Services**
- Hires primarily **Data Scientists** (131 postings), followed by **Data Engineers** (53), **Senior Data Scientists** (34), and **Data Analysts** (15)
- Carries a **Glassdoor rating of 3.5–4.0** out of 5

### 5.3 Tool Demand

| Tool | Demand Profile |
|------|---------------|
| Python | Universal — highest demand across all role types |
| Excel | Broadly required, especially at analyst and entry levels |
| SQL | Widely required; stronger at analyst and engineer levels |
| Keras | Strongly predictive of senior DS and research roles |
| PyTorch / Scikit | Common in DS and ML-focused roles |
| Tableau / PowerBI | More common in DA roles than DS roles |
| Flink | Negligible demand across all role types |
| Google Analytics | Negligible demand across all role types |

**Key Influencer finding:** For a Data Scientist role, knowing Python increases the probability of being classified as a DS by 2.94x relative to not knowing Python.

### 5.4 Degree Requirements

- Entry-level roles (DA, junior DS): BA degrees are standard
- Mid-level roles (DS, DE): BA/MA split
- Senior and research roles (Sr. DS, research scientist): MA and Ph.D. requirements increase sharply with salary

---

## 6. Discussion

### 6.1 Applied Implications

**For job seekers entering data science:** Python fluency is non-negotiable. Beyond Python, the tool investment that yields the highest return depends heavily on target role type. Analysts should prioritize SQL and Excel; ML-focused DS roles reward deep learning frameworks (Keras, PyTorch). Geographic flexibility dramatically expands opportunity — or, alternatively, targeted remote work negotiations can maintain access to coastal salaries.

**For HR teams hiring DS talent:** The compensation data in this analysis (bearing in mind Glassdoor limitations) suggests a meaningful salary premium for coastal roles. Organizations in non-coastal markets may find it difficult to compete on compensation but can differentiate on role scope, growth trajectory, and flexibility.

**For workforce and talent planning:** The concentration of demand in IT, biotech, and business services raises questions about DS talent gaps in other sectors (healthcare, government, education) as analytics adoption spreads. Early movers in those sectors may find an untapped talent pool less constrained by the coastal compensation premium.

### 6.2 Methodological Reflections

The Key Influencers visual in Power BI is among the most analytically powerful — and most frequently misunderstood — features in the platform. It performs a logistic regression in the background and presents the results as a ranked list of drivers with effect sizes. Understanding this allows the analyst to translate the visual into proper probabilistic language: "knowing Python increases the probability of a Data Scientist classification by 2.94x" — not "Python causes someone to be a data scientist." Communicating this distinction to non-technical stakeholders is part of the analytical value-add.

The dual map approach (3D + 2D) addressed a real tension in geospatial visualization: the 3D map is engaging and communicates salary variation intuitively in small geographies, but becomes hard to read at the national level. The 2D bubble map sacrifices dimensionality for legibility at scale. Both together provide a more complete picture than either alone.

### 6.3 Limitations

- **Data source:** Glassdoor scrapes reflect self-reported or estimated salaries, not verified compensation. Bureau of Labor Statistics data would provide a more authoritative benchmark.
- **Sample size:** 742 postings is a reasonable exploratory sample but may not be representative of the full market, particularly for rare role types or niche industries.
- **Organization size encoding:** Size categories (e.g., "1001-5000 employees") are ordinal bands, not continuous values. Feature engineering into small/medium/large buckets would improve analytical flexibility.
- **Tool co-occurrence:** The analysis treats tool requirements as independent binary variables. In practice, tools co-occur in predictable patterns (e.g., Python + PyTorch + Keras in ML roles). A co-occurrence or network analysis would reveal the bundled skill profiles that characterize each role type more precisely.
- **Temporal snapshot:** 2021 data predates significant shifts in the DS labor market (post-2022 tech layoffs, AI tool proliferation). The market structure described here may have changed.

---

## 7. Conclusion

This analysis provides a practical market map of the 2021 U.S. data science labor market across the dimensions most relevant to job seekers, hiring managers, and workforce planners: where roles are, what organizations look like, and what technical skills are required. The central finding is that the DS market in 2021 was geographically concentrated, technically Python-dominant, and organizationally skewed toward large private technology and biotech firms on the coasts.

The interactive Power BI dashboard translates these findings into a self-service tool, enabling users to filter by their specific context — industry, degree, seniority, location — and extract relevant benchmarks without requiring any data science background to operate.

---

## References

Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research, 16*, 321–357.

Davenport, T. H., & Patil, D. J. (2012). Data scientist: The sexiest job of the 21st century. *Harvard Business Review, 90*(10), 70–76.

IBM Watson Analytics. (2021). *Data Scientist Salary Dataset*. Kaggle. https://www.kaggle.com

Igamberdiev, T. (2021). *Data Science Job Salaries.* Kaggle. https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

Microsoft Corporation. (2021). *Power BI Desktop documentation.* Microsoft Learn. https://learn.microsoft.com/en-us/power-bi/

---

*Analysis by Mintay Misgano | Tools: Python, RapidMiner, Jamovi, Power BI | Data: 742 job postings, Glassdoor via Kaggle, 2021*
