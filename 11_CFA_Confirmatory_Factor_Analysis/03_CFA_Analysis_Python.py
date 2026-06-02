"""
Confirmatory Factor Analysis: GRMSAAW Scale Validation
=======================================================
Analyst  : Mintay Misgano
Tool     : Python 3 | semopy, pandas, matplotlib, seaborn
Dataset  : dfGRMSAAW.csv — simulated from Keum et al. (2018)
           published factor loadings and item descriptives.
           GRMSAAW — Gendered Racial Microaggressions Scale for
           Asian American Women (N=304, 22 items, 4 subscales)

Replicates the R lavaan CFA workflow using semopy, which shares
lavaan-compatible model syntax. Compares:
  Model 1 — Unidimensional (all 22 items on one factor)
  Model 2 — First-order correlated four-factor model

Fit indices: χ², CFI, GFI, RMSEA, SRMR, AIC, BIC
"""

# =============================================================================
# 1. IMPORTS
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")   # non-interactive backend (script / notebook execution)
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
from scipy.stats import chi2 as chi2_dist
import warnings
warnings.filterwarnings("ignore")

try:
    import semopy
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "semopy", "-q"])
    import semopy

print(f"semopy  : {semopy.__version__}")
print(f"pandas  : {pd.__version__}")
print(f"numpy   : {np.__version__}")

# =============================================================================
# 2. DATA LOADING
#    Data were pre-simulated in R using MASS::mvrnorm with empirical=TRUE
#    from published loadings (Keum et al., 2018, Table 2) and item
#    descriptives (Table 4).  See CFA_Scale_Validation.Rmd for full
#    simulation code.
# =============================================================================
df = pd.read_csv("01_dfGRMSAAW.csv").astype(float)

item_names = list(df.columns)
print(f"\nDataset shape : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Items         : {item_names[:4]} ... {item_names[-2:]}")
print(f"Value range   : {df.values.min():.0f} – {df.values.max():.0f}")

# =============================================================================
# 3. DESCRIPTIVE STATISTICS
# =============================================================================
desc = df.describe().T[["mean", "std", "min", "max"]]
desc.columns = ["Mean", "SD", "Min", "Max"]
desc["Skewness"] = df.skew().round(2)
desc["Kurtosis"] = df.kurtosis().round(2)

print("\nTable 1. Descriptive Statistics for GRMSAAW Items (N = 304)")
print("=" * 60)
print(desc.round(2).to_string())

# =============================================================================
# 4. INTER-ITEM CORRELATION HEATMAP
# =============================================================================
item_order = (
    [f"AS{i}"  for i in range(1, 10)] +
    [f"AF{i}"  for i in range(1, 5)]  +
    [f"MI{i}"  for i in range(1, 6)]  +
    [f"AUA{i}" for i in range(1, 5)]
)
cor_matrix = df[item_order].corr()

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(
    cor_matrix, annot=True, fmt=".2f", cmap="RdBu_r",
    center=0, vmin=-1, vmax=1, linewidths=0.4,
    annot_kws={"size": 7}, ax=ax
)
ax.set_title(
    "Figure 1: GRMSAAW Inter-Item Correlation Matrix\n"
    "(Items ordered by subscale: AS → AF → MI → AUA)",
    fontsize=13, fontweight="bold", pad=12
)
plt.tight_layout()
plt.savefig("fig1_correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nFigure 1 saved: fig1_correlation_heatmap.png")

# =============================================================================
# 5. MODEL 1: UNIDIMENSIONAL CFA
#    NOTE: semopy requires each model equation on a single line —
#    no line continuations. We build the string programmatically.
# =============================================================================
print("\n" + "=" * 60)
print("MODEL 1: UNIDIMENSIONAL CFA")
print("=" * 60)

uni_spec = "GRMSAAW =~ " + " + ".join(item_names)

model1 = semopy.Model(uni_spec)
res1   = model1.fit(df)
stats1 = semopy.calc_stats(model1)

print("\nFit Statistics — Unidimensional Model:")
print(stats1.T.round(3).to_string())

# Extract key indices (stats1 shape: (1, 14); iloc[0] → Series indexed by metric names)
s1 = stats1.iloc[0]
cfi1   = float(s1["CFI"])
rmsea1 = float(s1["RMSEA"])
srmr1  = float(s1["SRMR"]) if "SRMR" in s1.index else np.nan
aic1   = float(s1["AIC"])
bic1   = float(s1["BIC"])
chi1   = float(s1["chi2"])
dof1   = float(s1["DoF"])

# =============================================================================
# 6. MODEL 2: FOUR-FACTOR CORRELATED CFA
#    lavaan-style syntax, one factor per line.
#    By default, semopy correlates all latent variables (oblique model).
# =============================================================================
print("\n" + "=" * 60)
print("MODEL 2: FOUR-FACTOR CORRELATED CFA")
print("=" * 60)

four_spec = "\n".join([
    "AS  =~ " + " + ".join([f"AS{i}"  for i in range(1, 10)]),
    "AF  =~ " + " + ".join([f"AF{i}"  for i in range(1, 5)]),
    "MI  =~ " + " + ".join([f"MI{i}"  for i in range(1, 6)]),
    "AUA =~ " + " + ".join([f"AUA{i}" for i in range(1, 5)]),
])
print("Model syntax:\n", four_spec)

model4 = semopy.Model(four_spec)
res4   = model4.fit(df)
stats4 = semopy.calc_stats(model4)

print("\nFit Statistics — Four-Factor Model:")
print(stats4.T.round(3).to_string())

s4 = stats4.iloc[0]
cfi4   = float(s4["CFI"])
rmsea4 = float(s4["RMSEA"])
srmr4  = float(s4["SRMR"]) if "SRMR" in s4.index else np.nan
aic4   = float(s4["AIC"])
bic4   = float(s4["BIC"])
chi4   = float(s4["chi2"])
dof4   = float(s4["DoF"])

# --- Factor loadings table ---
# semopy inspect() uses columns: lval, op, rval, Estimate, Std. Err, z-value, p-value
params4 = model4.inspect(mode="list", what="est")

# Factor loadings: op == "~" with lval = item, rval = factor
# (semopy uses reflective notation: item ~ factor)
loadings4 = params4[params4["op"] == "~"].copy()
loadings4 = loadings4[["rval", "lval", "Estimate", "Std. Err", "z-value", "p-value"]].rename(
    columns={"rval": "Factor", "lval": "Item",
             "Std. Err": "SE", "z-value": "z", "p-value": "p"}
)
# Keep only rows where Factor is a latent variable (AS, AF, MI, AUA)
lat_factors = ["AS", "AF", "MI", "AUA"]
loadings4 = loadings4[loadings4["Factor"].isin(lat_factors)]

print("\nTable 2. Factor Loading Estimates — Four-Factor Model:")
print(loadings4.round(3).to_string(index=False))

# =============================================================================
# 7. FACTOR LOADINGS VISUALISATION
# =============================================================================
factor_colors = {"AS": "#2166ac", "AF": "#d73027", "MI": "#4dac26", "AUA": "#d01c8b"}
factor_labels = {
    "AS":  "Ascribed Submissiveness (AS)",
    "AF":  "Asian Fetishism (AF)",
    "MI":  "Media Invalidation (MI)",
    "AUA": "Universal Appearance (AUA)"
}

fig, ax = plt.subplots(figsize=(10, 8))
for _, row in loadings4.iterrows():
    color = factor_colors.get(row["Factor"], "gray")
    ax.barh(row["Item"], row["Estimate"], color=color, alpha=0.82)

ax.axvline(0,   color="black", linewidth=0.8)
ax.axvline(0.3, color="gray",  linewidth=0.8, linestyle="--", alpha=0.6)
ax.set_xlabel("Loading Estimate", fontsize=12)
ax.set_title(
    "Figure 2: Factor Loadings — Four-Factor CFA\n"
    "(dashed line = .30 practical threshold)",
    fontsize=13, fontweight="bold"
)
legend_els = [
    Patch(facecolor=factor_colors[k], label=factor_labels[k])
    for k in lat_factors
]
ax.legend(handles=legend_els, loc="lower right", fontsize=10)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("fig2_factor_loadings.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nFigure 2 saved: fig2_factor_loadings.png")

# =============================================================================
# 8. MODEL COMPARISON
# =============================================================================
print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

compare_df = pd.DataFrame({
    "Model":      ["Model 1 (Unidimensional)", "Model 2 (4-Factor)"],
    "χ²":         [round(chi1, 3), round(chi4, 3)],
    "df":         [int(dof1), int(dof4)],
    "CFI":        [round(cfi1, 3), round(cfi4, 3)],
    "RMSEA":      [round(rmsea1, 3), round(rmsea4, 3)],
    "SRMR":       [round(srmr1, 3) if not np.isnan(srmr1) else "-",
                   round(srmr4, 3) if not np.isnan(srmr4) else "-"],
    "AIC":        [round(aic1, 2), round(aic4, 2)],
    "BIC":        [round(bic1, 2), round(bic4, 2)],
}).set_index("Model")

print("\nTable 3. Model Fit Comparison")
print(compare_df.to_string())

# Chi-square difference test
dchi2 = chi1 - chi4
ddf   = dof1 - dof4
pval  = 1 - chi2_dist.cdf(dchi2, ddf)
crit  = chi2_dist.ppf(0.95, ddf)

print(f"\nChi-Square Difference Test:")
print(f"  Δχ²({ddf:.0f}) = {dchi2:.3f},  p = {pval:.6f}")
print(f"  Critical value (α=.05, df={ddf:.0f}): {crit:.3f}")
decision = "Model 2 is significantly superior (p < .001)" if pval < .001 else "No significant difference detected"
print(f"  → {decision}")

# =============================================================================
# 9. FIT COMPARISON VISUALISATION
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Left panel: CFI / RMSEA / SRMR
idx_labels = ["CFI", "RMSEA", "SRMR"]
# Use semopy computed values; fallback to 0 if NaN
srmr1_plot = srmr1 if not np.isnan(srmr1) else 0
srmr4_plot = srmr4 if not np.isnan(srmr4) else 0
m1_vals = [cfi1, rmsea1, srmr1_plot]
m4_vals = [cfi4, rmsea4, srmr4_plot]
x = np.arange(len(idx_labels))
w = 0.35

axes[0].bar(x - w/2, m1_vals, w, label="Model 1 (Unidimensional)", color="#2166ac", alpha=0.8)
axes[0].bar(x + w/2, m4_vals, w, label="Model 2 (4-Factor)",       color="#66c2a5", alpha=0.8)
axes[0].axhline(0.95, linestyle="--", color="#d73027", lw=1.2, label="CFI ≥ .95")
axes[0].axhline(0.10, linestyle=":",  color="gray",   lw=1.2, label="RMSEA/SRMR < .10")
axes[0].set_xticks(x); axes[0].set_xticklabels(idx_labels, fontsize=12)
axes[0].set_ylim(0, 1.1)
axes[0].set_ylabel("Index Value", fontsize=11)
axes[0].set_title("Fit Indices\n(higher CFI = better; lower RMSEA/SRMR = better)",
                  fontsize=11, fontweight="bold")
axes[0].legend(fontsize=8)

# Right panel: AIC / BIC
info_labels = ["AIC", "BIC"]
# Use semopy values (scaled per semopy convention)
m1_info = [aic1, bic1]
m4_info = [aic4, bic4]
x2 = np.arange(len(info_labels))
axes[1].bar(x2 - w/2, m1_info, w, label="Model 1 (Unidimensional)", color="#2166ac", alpha=0.8)
axes[1].bar(x2 + w/2, m4_info, w, label="Model 2 (4-Factor)",       color="#66c2a5", alpha=0.8)
axes[1].set_xticks(x2); axes[1].set_xticklabels(info_labels, fontsize=12)
axes[1].set_ylabel("Criterion Value", fontsize=11)
axes[1].set_title("Information Criteria\n(lower = better fit + parsimony)",
                  fontsize=11, fontweight="bold")
axes[1].legend(fontsize=8)

fig.suptitle("Figure 3: CFA Model Comparison — Unidimensional vs. Four-Factor",
             fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig("fig3_model_comparison.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nFigure 3 saved: fig3_model_comparison.png")

# =============================================================================
# 10. APA RESULTS SUMMARY
# =============================================================================
print(f"""
================================================================
APA-STYLE RESULTS SUMMARY
================================================================

Confirmatory factor analysis was conducted in Python using
semopy {semopy.__version__} (Meshcheryakov et al., 2021)
with maximum likelihood estimation (N = 304).

MODEL 1 — UNIDIMENSIONAL:
  χ²({int(dof1)}) = {chi1:.3f},  p < .001
  CFI = {cfi1:.3f}  |  RMSEA = {rmsea1:.3f}  |  AIC = {aic1:.2f}
  → Poor fit. Single-factor model rejected.
  (CFI well below .95 threshold; RMSEA exceeds .10 danger zone)

MODEL 2 — FOUR-FACTOR CORRELATED:
  χ²({int(dof4)}) = {chi4:.3f},  CFI = {cfi4:.3f}
  RMSEA = {rmsea4:.3f}  |  AIC = {aic4:.2f}  |  BIC = {bic4:.2f}
  → Substantially improved fit on all indices.

MODEL COMPARISON:
  Δχ²({int(ddf)}) = {dchi2:.3f},  p = {pval:.4f}
  ΔAIC = {aic1 - aic4:.2f}  (Model 2 lower — preferred)
  ΔBIC = {bic1 - bic4:.2f}  (Model 2 lower — preferred)
  → Four-factor correlated model is significantly superior.
     The GRMSAAW functions as a four-dimensional instrument.

NOTE: AIC/BIC values differ from R lavaan because semopy uses
a per-observation likelihood scaling. Use R output for
publication-ready AIC/BIC values; use semopy output for
relative within-Python model comparison.
================================================================
""")
