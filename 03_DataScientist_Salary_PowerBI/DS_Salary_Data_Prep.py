# =============================================================================
# Data Scientist Salary Market Analysis (2021) — Data Preparation
# =============================================================================
# Author:  Mintay Misgano
# Date:    2022-05-31
# Tools:   Python / Pandas (replicates cleaning originally done in RapidMiner)
# Data:    Kaggle — Data Scientist Salary Dataset (Glassdoor scrape, 742 rows)
# Purpose: Clean and prepare DS job posting data for Power BI visualization
# =============================================================================

import pandas as pd

# =============================================================================
# 1. LOAD RAW DATA
# =============================================================================

# Original Kaggle dataset: 742 job postings scraped from Glassdoor
# 42 columns covering job title, salary, company info, tech stack requirements
df = pd.read_csv("ds_salary_original.csv", encoding="latin1")

print("Raw data shape:", df.shape)
print("Columns:", list(df.columns))

# =============================================================================
# 2. REMOVE UNINFORMATIVE COLUMNS
# =============================================================================

# 'Company Name' is redundant — it combines company text and rating in one
# field (e.g., "Microsoft 4.2"). Separate columns 'company_txt' and 'Rating'
# already capture both pieces of information individually.
df = df.drop(columns=["Company Name"])

# 'Competitors' is ~60% missing and is not relevant to our core research
# questions about salary drivers, location, and tool demand.
df = df.drop(columns=["Competitors"])

print("\nAfter removing redundant columns:", df.shape)
# Expected: (742, 40)

# =============================================================================
# 3. RENAME COLUMNS FOR CLARITY
# =============================================================================

# Rename ambiguous column names to more intuitive labels
df = df.rename(columns={
    "bi":         "PowerBI",       # 'bi' is unclear; Power BI is the full name
    "Location":   "Job Location",  # disambiguate from 'Headquarters'
    "google_an":  "Google Analytics"
})

# =============================================================================
# 4. CONVERT BINARY TOOL COLUMNS TO BOOLEAN
# =============================================================================

# 16 columns indicate whether a given tool/language is required for the role:
# 0 = not required, 1 = required. Convert to True/False for cleaner reporting.

tool_cols = [
    "Python", "spark", "aws", "excel", "sql", "sas",
    "keras", "pytorch", "scikit", "tensor", "hadoop",
    "tableau", "PowerBI", "flink", "mongo", "Google Analytics"
]

df[tool_cols] = df[tool_cols].astype(bool)

print("\nTool columns converted to boolean:")
print(df[tool_cols].dtypes)

# =============================================================================
# 5. STANDARDIZE A KNOWN DATA ENTRY ERROR
# =============================================================================

# One entry listed "Phila, PA" instead of "Philadelphia, PA".
# Cross-checked against company size, headquarters, and sector — confirmed match.
df["Job Location"] = df["Job Location"].replace("Phila, PA", "Philadelphia, PA")

# =============================================================================
# 6. VALIDATE: CHECK FOR MISSING VALUES
# =============================================================================

missing = df.isnull().sum()
missing = missing[missing > 0]

if missing.empty:
    print("\nNo missing values — dataset is complete.")
else:
    print("\nMissing values found:")
    print(missing)

# =============================================================================
# 7. SALARY COLUMNS — ENSURE NUMERIC
# =============================================================================

# Salary columns should be numeric for aggregation in Power BI.
# Lower Salary, Upper Salary, Avg Salary(K) come in as integers from the
# Glassdoor scrape and should remain numeric (not summed — averaged in PBI).

salary_cols = ["Lower Salary", "Upper Salary", "Avg Salary(K)"]
df[salary_cols] = df[salary_cols].apply(pd.to_numeric, errors="coerce")

print("\nSalary column types:")
print(df[salary_cols].dtypes)

# =============================================================================
# 8. SET INDEX
# =============================================================================

# 'index' is the unique row identifier from the original scrape.
# Set as the DataFrame index — equivalent to Set Role in RapidMiner.
df = df.set_index("index")

# =============================================================================
# 9. FINAL DATASET SUMMARY
# =============================================================================

print("\n=== Final Dataset ===")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nSample rows:")
print(df.head(3))

# =============================================================================
# 10. EXPORT CLEANED DATA
# =============================================================================

# Save the cleaned dataset for import into Power BI
df.to_csv("ds_salary_clean.csv")
print("\nCleaned data saved to ds_salary_clean.csv")

# =============================================================================
# NOTE ON VISUALIZATION
# =============================================================================
# The cleaned dataset was imported into Power BI for dashboard creation.
# Key dashboards built:
#   - 3D and 2D salary maps by location
#   - Tool demand by job type (Key Influencers visual)
#   - Word cloud of job description keywords
#   - Salary vs. company features (age, rating, sector, industry)
#   - Salary vs. personal features (seniority, degree)
# Global filters enabled cross-dashboard filtering by size, industry,
# job title, and degree throughout the report.
# =============================================================================
