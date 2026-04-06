# Project 10b: Confirmatory Factor Analysis — GRMSAAW Scale Validation

> Psychometric validation of a 22-item microaggression scale using CFA in R (lavaan) and Python (semopy)

**Domain:** Psychometrics · Survey Validation · DEI Measurement
**Tools:** R (lavaan, semPlot, psych) · Python (semopy, pandas, matplotlib, seaborn)
**Dataset:** Simulated from Keum et al. (2018) published loadings — N = 304, 22 items, 4 subscales

---

## Overview

This project applies **Confirmatory Factor Analysis (CFA)** to evaluate the psychometric structure of the *Gendered Racial Microaggressions Scale for Asian American Women* (GRMSAAW; Keum et al., 2018). Two competing measurement models are compared:

| Model | Structure | CFI | RMSEA | SRMR |
|---|---|:---:|:---:|:---:|
| Unidimensional | All 22 items → 1 factor | .578 | .112 | .124 |
| **4-Factor Correlated** | Items → 4 subscales, factors covary | **.991** | **.017** | **.058** |

The four-factor model is confirmed as vastly superior (Δχ²[6] = 783.28, *p* < .001). The GRMSAAW captures four distinct but correlated dimensions of microaggression experience.

---

## Key Results

- **Unidimensional model rejected:** CFI = .578 (well below .95), RMSEA = .112 (exceeds .10 danger threshold)
- **Four-factor model: excellent fit:** CFI = .991, RMSEA = .017 [.000, .031], SRMR = .058
- **All 22 loadings significant:** standardized loadings range from .35 (MI5) to .82 (AUA1)
- **Factor correlations low** (all *r* < .10): subscales are distinct constructs
- **Results replicated identically in Python** (semopy χ² matches R lavaan exactly)

---

## Subscales

| Subscale | Items | Description |
|---|:---:|---|
| Ascribed Submissiveness (AS) | AS1–AS9 | Expectations of deference and compliance |
| Asian Fetishism (AF) | AF1–AF4 | Sexualization and racial fetishization |
| Media Invalidation (MI) | MI1–MI5 | Underrepresentation and stereotyping in media |
| Universal Appearance (AUA) | AUA1–AUA4 | Assumptions of shared physical features |

---

## Files

| File | Language | Description |
|---|---|---|
| `CFA_Scale_Validation.Rmd` | R | Full analysis: data simulation, CFA, model comparison. Knit in RStudio → produces `.md` + `_files/` for GitHub rendering |
| `CFA_Scale_Validation.md` | — | *(After knitting)* Rendered output — this is what GitHub displays |
| `CFA_Scale_Validation.ipynb` | Python | Executed Jupyter notebook with embedded output — renders on GitHub natively |
| `CFA_Scale_Validation.py` | Python | Clean source script (equivalent to the notebook) |
| `Executive_Brief.md` | — | 1-page practitioner summary for HR/DEI leaders |
| `CFA_Project_Report.md` | — | Full APA-style research report |
| `dfGRMSAAW.csv` | — | Dataset (N = 304, 22 items, simulated from Keum et al. 2018) |

---

## How to Render the R Analysis on GitHub

The `.Rmd` file requires a one-time knit to produce GitHub-visible output:

1. Open `CFA_Scale_Validation.Rmd` in **RStudio**
2. Press `Ctrl+Shift+K` (or click **Knit**)
3. This produces `CFA_Scale_Validation.md` + `CFA_Scale_Validation_files/` (plot images)
4. Commit all three to GitHub: `.Rmd`, `.md`, and the `_files/` folder
5. GitHub renders the `.md` automatically — full output including tables and plots

The Python `.ipynb` is already executed with embedded output — GitHub renders it immediately.

---

## Methods Demonstrated

- **Data simulation from published psychometric parameters** (MASS::mvrnorm with empirical=TRUE)
- **CFA model specification:** lavaan syntax (`=~`, `~~`), identification requirements
- **Fit index interpretation:** χ², CFI, TLI, RMSEA (with 90% CI), SRMR
- **Nested model comparison:** chi-square difference test (χ²Δ), AIC, BIC
- **Cross-platform replication:** R → Python, identical χ² output
- **APA-style results write-up** embedded directly in the analysis document

---

## Fit Comparison

```
Index         | Model 1 (Unidimensional) | Model 2 (4-Factor) | Criterion
--------------+-------------------------+--------------------+----------
CFI           |          .578           |        .991        |  ≥ .95
RMSEA         |          .112           |        .017        |  ≤ .05
SRMR          |          .124           |        .058        |  < .10
AIC           |       17,755            |      16,984        |  lower ↓
Δχ²(6)        |           —             |      783.28***     |  sig = better
```

---

## References

- Keum, B. T., et al. (2018). *Journal of Counseling Psychology, 65*(5), 571–585. https://doi.org/10.1037/cou0000289
- Rosseel, Y. (2012). lavaan. *Journal of Statistical Software, 48*(2). https://doi.org/10.18637/jss.v048.i02
- Kline, R. B. (2016). *Principles and practice of structural equation modeling* (4th ed.). Guilford Press.
- Meshcheryakov, G., et al. (2021). semopy. *Journal of Statistical Software, 101*(1). https://doi.org/10.18637/jss.v101.i01
