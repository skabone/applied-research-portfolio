# Project 12: Measurement Invariance Testing
**Mintay Misgano | People Analytics Portfolio**

---

## What I Did

I tested whether the Ableist Microaggressions Scale (AMS; Conover et al., 2017) — a 20-item, four-factor instrument — functions equivalently across disability severity groups (Mild, n = 548; Severe, n = 285; total N = 833). Using multi-group confirmatory factor analysis (MGCFA) in R and Python, I ran the full configural → weak → strong → strict invariance hierarchy.

---

## Key Finding

| Level | Constraint | ΔCFI | Decision |
|-------|-----------|------|---------|
| Configural | None — same factor structure | — | **Supported** |
| Weak | Equal factor loadings | .002 | **Supported** |
| Strong | + Equal item intercepts | .096 | **Not supported** |
| Strict | + Equal residuals | — | Not tested |

**Weak invariance holds; strong invariance fails.** Factor loadings are equivalent across groups — the four constructs (Helplessness, Minimization, Denial of Personhood, Otherization) are measured on the same metric in both groups. However, item intercepts differ: at equal latent factor levels, Severe respondents endorse items at systematically higher levels than Mild respondents. **Raw subscale means cannot be directly compared across groups without partial invariance corrections.**

---

## Why It Matters

This is a pattern that surfaces regularly in People Analytics: a well-validated survey that appears to measure the same thing across groups actually has item-level baseline differences that confound cross-group comparisons. Reporting group mean scores without an invariance check risks misattributing item-endorsement differences to genuine construct differences. The MGCFA workflow here applies directly to employee engagement, inclusion, and experience surveys where cross-segment comparisons are standard practice.

---

## Files

| File | Description |
|------|-------------|
| `01_dfAMSi.csv` | Simulated dataset (N = 833, 20 items + Severity group) |
| `02_Invariance_Analysis_R.md` | Full MGCFA in R — lavaan configural/weak/strong/strict with Δχ² tests |
| `03_Invariance_Analysis_Python.ipynb` | Python replication — semopy per-group CFA, loading comparison, visualizations |
| `04_Project_Report.md` | Full APA-style report with results, discussion, and references |
| `Python_Figures/` | Correlation heatmaps, loading comparison plots, item mean profiles |

---

*Dataset simulated from published loadings (Conover et al., 2017, Table 2) · seed = 211023 · R (lavaan) + Python (semopy)*
