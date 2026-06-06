# =============================================================================
# U.S. Data Scientist Market Analysis (2021) - Data Preparation
# =============================================================================
# Author:  Mintay Misgano, PhD
# Date:    2022-05-31
# Tools:   Python / Pandas
# Data:    Public analysis extract derived from a Kaggle Glassdoor scrape
# Purpose: Validate and prepare job-market data for dashboard analysis
# =============================================================================

from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent


# =============================================================================
# 1. LOAD PUBLIC ANALYSIS DATA
# =============================================================================

# The repository stores a feature-level public extract, not raw job descriptions.
# Fields that could carry contact details or unnecessary third-party text
# (job descriptions, company names, headquarters, competitors) are excluded.
df = pd.read_csv(PROJECT_DIR / "ds_salary_public.csv", encoding="utf-8")

print("Public data shape:", df.shape)
print("Columns:", list(df.columns))


# =============================================================================
# 2. STANDARDIZE COLUMN TYPES
# =============================================================================

tool_cols = [
    "python", "spark", "aws", "excel", "sql", "sas",
    "keras", "pytorch", "scikit", "tensor", "hadoop",
    "tableau", "power_bi", "flink", "mongo", "google_analytics",
]

salary_cols = ["lower_salary_k", "upper_salary_k", "avg_salary_k"]
flag_cols = ["hourly_flag", "employer_provided_flag"]

df[tool_cols + flag_cols] = df[tool_cols + flag_cols].astype(bool)
df[salary_cols] = df[salary_cols].apply(pd.to_numeric, errors="coerce")
df["company_rating"] = pd.to_numeric(df["company_rating"], errors="coerce")
df["company_age"] = pd.to_numeric(df["company_age"], errors="coerce")


# =============================================================================
# 3. VALIDATE
# =============================================================================

missing = df.isnull().sum()
missing = missing[missing > 0]

if missing.empty:
    print("\nNo missing values in required public fields.")
else:
    print("\nMissing values found:")
    print(missing)

print("\nSalary column types:")
print(df[salary_cols].dtypes)


# =============================================================================
# 4. SET INDEX
# =============================================================================

df = df.set_index("posting_id")


# =============================================================================
# 5. FINAL DATASET SUMMARY
# =============================================================================

print("\n=== Final Dataset ===")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nSample rows:")
print(df.head(3))


# =============================================================================
# 6. EXPORT CLEANED DATA
# =============================================================================

clean_path = PROJECT_DIR / "ds_salary_clean.csv"
df.to_csv(clean_path)
print(f"\nCleaned data saved to {clean_path.name}")


# =============================================================================
# NOTE ON VISUALIZATION
# =============================================================================
# The cleaned dataset was imported into Power BI for dashboard creation.
# Key dashboards built:
#   - Salary maps by state
#   - Tool demand by role family
#   - Salary vs. company features such as age, rating, sector, and industry
#   - Salary vs. role features such as seniority and degree requirement
# Global filters enabled cross-dashboard filtering by size, industry,
# role family, and degree throughout the report.
# =============================================================================
