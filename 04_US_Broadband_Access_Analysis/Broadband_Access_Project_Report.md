# America's Broadband Problem
### A County-Level Analysis of Broadband Access and Equity in the United States

**Author:** Mintay Misgano, PhD
**Tools:** Python · RapidMiner · Tableau
**Dataset:** IMLS / BroadbandNow / FCC / ACS / Simple Maps · N = 3,102 U.S. counties

---

## Abstract

This project examines county-level variation in U.S. broadband access using a merged dataset of 3,102 counties drawn from IMLS, BroadbandNow, FCC-linked indicators, ACS-based measures, and county geodata. The analysis was completed as a data-visualization and public-policy project, with cleaning performed in RapidMiner and documented in a companion Python script, and findings presented through a Tableau story. The main descriptive patterns are straightforward: broadband outcomes vary sharply across counties, poverty rate is more informative than formal coverage-style metrics when interpreting likely access, regional gradients are visible in the mapped data, and counties with higher concentrations of Black residents are overrepresented among poorer broadband outcomes in this dataset.

---

## 1. Project Context and Research Questions

Broadband access became an especially visible public issue during the COVID-19 era, but uneven connectivity across U.S. counties predates the pandemic. This project was designed to examine that variation at the county level rather than relying on national or state averages, which can conceal important local differences in access, affordability, and infrastructure quality.

The project addresses two core research questions:

1. **Which U.S. counties and states appear most at risk of being left behind in broadband access?**
2. **Do counties with higher concentrations of Black residents also appear to experience poorer broadband outcomes in this dataset?**

---

## 2. Data Description

### 2.1 Sources

The dataset integrates three primary sources blended prior to analysis:

**IMLS Indicators Workbook (primary):**
The Institute of Museum and Library Services compiled county-level broadband indicators from multiple sources, including ACS 5-year estimates, BroadbandNow commercial FCC-linked data, and Bureau of Labor Statistics unemployment statistics.

**BroadbandNow Open Data Challenge (supplementary):**
A publicly available dataset hosted on GitHub that provides additional county-level broadband metrics.

**Simple Maps U.S. Counties (geodata):**
Used to add county coordinates and supporting geographic fields for mapping in Tableau.

### 2.2 Variable Overview

| Domain | Variables |
|--------|-----------|
| Geography | County name, state, state abbreviation |
| Demographics | Population, Black population overlay, selected county composition indicators |
| Economic | Unemployment rate, poverty rate, SNAP receipt, health insurance coverage |
| Technology access | No home computer, no home internet, home broadband rate |
| Broadband infrastructure | Provider counts, availability indicators, broadband cost |
| Additional broadband metrics | Wired access, 25 Mbps coverage, download speed, related access indicators |

### 2.3 Data Quality Note

A central issue in the project was the mismatch between provider-style coverage measures and more meaningful indicators of likely household access. In particular, BroadbandNow provider counts appeared substantially higher than expected at the county level, which raised concerns about how formal broadband availability was being represented. Where overlapping measures existed, IMLS-derived fields were generally preferred over lower-quality alternatives.

---

## 3. Data Preparation

Data cleaning was performed in RapidMiner. The full process is documented in the accompanying Python script (`Broadband_Access_Data_Prep.py`).

### 3.1 Missing Data

- The primary broadband cost variable retained the IMLS version and removed a small number of rows with missing values.
- Five continuous broadband variables with minimal missingness were imputed using column means.
- Two county-level values were manually checked and filled from external reference sources.

### 3.2 Column Selection

Several BroadbandNow columns were removed when higher-quality or less redundant IMLS alternatives were available, including overlapping population, provider-count, and price variables.

### 3.3 Final Dataset

The final analysis file contains **3,102 counties and 20 variables** after cleaning and consolidation.

---

## 4. Visualization Approach

The Tableau story was designed to move from broad national patterns to more detailed county-level comparisons:

| Level | Dashboard Focus |
|-------|------------------|
| National overview | State-level broadband patterns |
| County detail | County-level access comparisons |
| Geographic gradients | Latitude and longitude views for regional pattern detection |
| Equity overlay | Demographic layering for contextual interpretation |

One important visualization choice was centering color scales on national averages rather than raw extremes. This makes above/below-baseline comparisons easier to interpret in a highly uneven county-level dataset.

---

## 5. Findings

### 5.1 County-Level Gaps Are Substantial

Broadband access, provider counts, speed, and cost vary meaningfully across counties. These differences are large enough that national or state averages can obscure important local conditions.

### 5.2 Poverty Is More Informative Than Coverage Metrics Alone

Survey-based or household-level access measures aligned more closely with poverty than official-style availability indicators. This suggests that formal provider presence does not fully capture whether broadband is realistically accessible.

### 5.3 Geographic Patterns Are Visible

Regional and rural-urban differences appear clearly in the mapped data. Northern counties generally perform better on several access-related measures, while poorer outcomes cluster more often in parts of the South and in rural counties.

### 5.4 Demographic Concentration Matters

Counties with higher concentrations of Black residents appear disproportionately among poorer broadband outcomes in this dataset. This does not establish causation, but it does make the equity dimension of broadband access easier to visualize and discuss.

---

## 6. Interpretation

### 6.1 Policy Interpretation

Several patterns in the dataset have practical policy relevance. First, county-level comparisons are more informative than state averages when the goal is to identify where broadband disadvantages cluster. Second, survey- or usage-adjacent indicators appear more helpful than coverage-style metrics alone when reasoning about likely real-world access. Third, the geographic overlap between poorer broadband outcomes, higher poverty, and counties with larger Black populations suggests that equity questions should remain central when interpreting broadband infrastructure data.

### 6.2 Visualization and Methodological Notes

The decision to center color scales on the national average rather than the raw min/max was meant to support interpretation. In a dataset with large population outliers and skewed county distributions, above/below-baseline comparisons are often easier to read than absolute extremes.

The comparison of state versus county summaries also reinforces a broader public-policy analytics lesson: the unit of analysis matters. Aggregating to the state level can simplify communication, but it also hides variation that may matter for targeting and interpretation.

### 6.3 Limitations

**Data vintage:** Much of the source data reflects the 2014–2018 period and may not represent current broadband conditions.

**Data quality:** Broadband availability measures remain difficult to interpret because provider presence and practical household access are not the same thing.

**Demographic scope:** The equity lens here focuses primarily on Black population concentration because of the fields available in the project workflow.

**Causal inference:** The findings are descriptive and observational. They are useful for pattern detection and discussion, not causal claims.

---

## 7. Conclusion

This project shows how county-level broadband data can be cleaned, compared, and visualized to make national inequalities more interpretable. The main contribution is not a causal claim about why gaps exist, but a clearer descriptive view of where access-related differences appear, how those patterns vary geographically, and how demographic and economic context can be layered into the analysis.

As a portfolio piece, the project demonstrates multi-source data preparation, public-data quality review, Tableau-based geographic storytelling, and cautious interpretation of descriptive findings from observational data.

---

## References

BroadbandNow. (2022). *BroadbandNow open data challenge dataset*. GitHub. https://github.com/BroadbandNow/Open-Data

Federal Communications Commission. (2021). *Fixed broadband deployment data*. FCC. https://www.fcc.gov/general/broadband-deployment-data

Institute of Museum and Library Services. (2020). *IMLS Indicators Workbook: Economic status and broadband availability and adoption*. IMLS. https://www.imls.gov

Pew Research Center. (2021). *Home broadband adoption, computer ownership vary by race, ethnicity in the U.S.* Pew Research Center. https://www.pewresearch.org

Simple Maps. (2021). *US counties database.* Simple Maps. https://simplemaps.com/data/us-counties

U.S. Census Bureau. (2019). *American community survey 5-year estimates, 2014–2018.* U.S. Census Bureau. https://www.census.gov/programs-surveys/acs

---

*Analysis by Mintay Misgano, PhD | Tools: Python, RapidMiner, Tableau | Data: 3,102 U.S. counties, IMLS/BroadbandNow/FCC/ACS, 2014–2020*
