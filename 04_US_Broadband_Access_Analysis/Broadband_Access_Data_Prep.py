# =============================================================================
# America's Broadband Problem — Data Preparation
# =============================================================================
# Author:  Mintay Misgano, PhD
# Date:    2022
# Tools:   Python / Pandas (replicates cleaning originally done in RapidMiner)
# Data:    Kaggle blend of IMLS + BroadbandNow data (county-level, USA)
# Purpose: Clean and prepare county-level broadband data for Tableau analysis
# =============================================================================
# Research Questions:
#   1. Which U.S. counties and states are most at risk of being left behind
#      in broadband access?
#   2. Do counties with higher concentrations of Black Americans show
#      disparate broadband outcomes (disparate impact analysis)?
# =============================================================================

import pandas as pd

# =============================================================================
# 1. LOAD SOURCE DATASETS
# =============================================================================

# Primary dataset: Kaggle blend of two sources:
#   - IMLS (Institute of Museum and Library Services) Indicators Workbook
#     (ACS 5-year 2014-2018 estimates + BroadbandNow commercial FCC aggregator
#     + Bureau of Labor Statistics local area unemployment statistics)
#   - BroadbandNow Open Data Challenge dataset (GitHub)
# Note: Simple Maps county data was joined directly in Tableau (inner join
# on county/state) to obtain latitude/longitude for mapping.

df = pd.read_csv("broadband_access.csv", encoding="latin1")

print("Raw data shape:", df.shape)
print("Columns:", list(df.columns))

# =============================================================================
# 2. HANDLE MISSING DATA
# =============================================================================

# --- Price_BBN (111 missing) and Broad_Cost_IMLS (40 missing) ---
# Min, max, and average for both price columns were nearly identical,
# indicating the two sources measured the same underlying quantity.
# Decision: Use Broad_Cost_IMLS (IMLS data is more authoritative);
# drop Price_BBN entirely.
# Remove the 40 rows where Broad_Cost_IMLS is missing (40/3142 = 1.3% — negligible).

if "Lowestpricepermonth_bbn" in df.columns:
    df = df.drop(columns=["Lowestpricepermonth_bbn"])

df = df.dropna(subset=["broad_cost"])
print(f"\nAfter dropping missing broad_cost rows: {df.shape}")
# Expected: ~3102 rows

# --- Five attributes with small numbers of missing values ---
# Each had <14 missing values (<0.5% of rows). Replaced with column mean.
# Imputing the mean is appropriate given the negligible proportion of missing
# cases and the continuous, roughly symmetric nature of these variables.

impute_mean_cols = ["wired_bbn", "all25_bbn", "downave_bbn", "access_bbn", "slowfrac_bbn"]

for col in impute_mean_cols:
    if col in df.columns and df[col].isnull().any():
        col_mean = df[col].mean()
        df[col] = df[col].fillna(col_mean)
        print(f"  Imputed {col} mean = {col_mean:.4f}")

# --- Unemployment and Poverty Rate (1 missing each) ---
# Manually looked up from authoritative sources:
#   - Kalawao County, HI unemployment: 21%  (source: datausa.io)
#   - Rio Arriba County, NM poverty rate: 24% (source: datausa.io)

if "unemp_19%" in df.columns:
    mask_unemp = df["unemp_19%"].isnull()
    if mask_unemp.any():
        df.loc[mask_unemp, "unemp_19%"] = 21.0
        print("  Filled 1 missing unemployment value (Kalawao County, HI = 21%)")

if "poverty_rate%" in df.columns:
    mask_pov = df["poverty_rate%"].isnull()
    if mask_pov.any():
        df.loc[mask_pov, "poverty_rate%"] = 24.0
        print("  Filled 1 missing poverty rate value (Rio Arriba County, NM = 24%)")

# =============================================================================
# 3. REMOVE REDUNDANT COLUMNS
# =============================================================================

# Three BBN columns were replaced by higher-quality IMLS equivalents:
#
# - population_bbn → use population_19 (IMLS)
#     BBN population had more missing data and diverged from other sources
# - provide_bbn → use broadProviders_num (IMLS)
#     BBN showed avg 12 providers/county vs. FCC national average of 4.1 —
#     wildly implausible; IMLS data is substantially more reliable
# (Price_BBN already dropped above)

cols_to_drop = ["population_bbn", "provide_bbn"]
cols_to_drop = [c for c in cols_to_drop if c in df.columns]
df = df.drop(columns=cols_to_drop)

print(f"\nAfter removing redundant BBN columns: {df.shape}")
# Expected: ~3102 rows × 20 columns

# =============================================================================
# 4. VALIDATE FINAL DATASET
# =============================================================================

missing_final = df.isnull().sum()
missing_final = missing_final[missing_final > 0]

if missing_final.empty:
    print("\nNo remaining missing values.")
else:
    print("\nRemaining missing values:")
    print(missing_final)

print("\n=== Final Dataset ===")
print("Shape:", df.shape)
print("\nColumn list:")
for col in df.columns:
    print(f"  {col}: {df[col].dtype}")

print("\nSample:")
print(df.head(3))

# =============================================================================
# 5. EXPORT CLEANED DATA
# =============================================================================

df.to_csv("broadband_clean.csv", index=False)
print("\nCleaned data saved to broadband_clean.csv")

# =============================================================================
# NOTE ON VISUALIZATION
# =============================================================================
# The cleaned dataset was imported into Tableau where it was inner-joined with
# Simple Maps county data (lat/long) to enable geographic mapping.
#
# Key visualizations built in Tableau:
#   - County-level broadband access map (color-scaled to national average)
#   - State vs. county comparison dashboards
#   - Scatter-plot map using lat/long to show N/S and E/W access gradients
#   - Black American population overlay (Map Layers)
#   - Broadband availability vs. poverty rate relationship
#   - Story combining dashboards into a narrative arc
#
# Key design decision: Color scales were centered on the national average
# rather than min/max, to show which counties are above or below baseline —
# a more meaningful reference than arbitrary endpoints.
# =============================================================================
