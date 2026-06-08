# =============================================================================
# U.S. Data Scientist Market Analysis (2021) — Analysis and Visualization
# =============================================================================
# Tools:   Python / pandas / matplotlib
# Data:    Public feature-level extract derived from a Kaggle Glassdoor scrape
#          (data/ds_salary_public.csv, N = 742 postings, 36 fields)
# Purpose: Reproduce the labor-market analysis behind the dashboard project as a
#          self-contained, public-safe Python pipeline. Every number reported in
#          the README, summary, and report is computed and printed here, and the
#          seven figures embedded in those documents are generated into
#          docs/figures/. The original cleaning was done in RapidMiner/Jamovi and
#          the visuals in Power BI; this script makes the same evidence
#          reproducible from the repository without proprietary tooling.
# =============================================================================

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Resolve paths from the project folder or the repo root so the script runs from
# either location without editing. Figures are written to docs/figures/ so the
# written documents can reference them by a stable relative path.
HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "ds_salary_public.csv"
if not DATA.exists():
    DATA = HERE / "03_Data_Scientist_Market_Analysis" / "data" / "ds_salary_public.csv"
FIGDIR = DATA.parent.parent / "docs" / "figures"
FIGDIR.mkdir(parents=True, exist_ok=True)

# A single readable theme is applied to every figure so the visual language is
# consistent across the project: light background, muted grid, no chartjunk.
plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 120,
    "savefig.bbox": "tight",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
})
ACCENT = "#2c6e9c"      # primary blue used for the focal series
ACCENT2 = "#c25a3c"     # warm contrast used to highlight one comparison
NEUTRAL = "#9aa7b1"     # muted gray for context bars


# =============================================================================
# 1. LOAD THE PUBLIC EXTRACT
# =============================================================================
# The repository stores a feature-level extract, not raw job descriptions.
# Company names, headquarters, competitors, and posting free-text are excluded
# at the source so nothing identifying or contact-bearing is published here.
df = pd.read_csv(DATA)
print("Public data shape:", df.shape)

TOOLS = ["python", "spark", "aws", "excel", "sql", "sas", "keras", "pytorch",
         "scikit", "tensor", "hadoop", "tableau", "power_bi", "flink", "mongo",
         "google_analytics"]
# Tool indicators arrive as 0/1 integers; cast to boolean so a mean() reads
# directly as "share of postings that require this tool" rather than a sum.
df[TOOLS] = df[TOOLS].astype(bool)
df["avg_salary_k"] = pd.to_numeric(df["avg_salary_k"], errors="coerce")


# =============================================================================
# 2. NORMALIZE ROLE LABELS INTO ANALYSIS GROUPS
# =============================================================================
# The scraped job titles are noisy (e.g. "data analitics", "na",
# "Data scientist project manager"). Collapsing them into a small set of role
# groups makes salary and tool comparisons legible while keeping every posting.
def role_group(raw: str) -> str:
    r = str(raw).lower()
    if "machine learning" in r:
        return "ML Engineer"
    if "director" in r or "project man" in r:
        return "Lead/Director"
    if "data engineer" in r or "modeler" in r:
        return "Data Engineer"
    if "analyst" in r or "analitics" in r:
        return "Analyst"
    if "data scientist" in r:
        return "Data Scientist"
    if "other scientist" in r:
        return "Other Scientist"
    return "Other/NA"


df["role_grp"] = df["role_family"].apply(role_group)

# Plain-language degree and seniority labels for axis readability.
df["deg"] = df["degree_required"].map(
    {"na": "Not specified", "M": "Master's", "P": "PhD"})
df["sen"] = df["seniority"].map({"na": "Unspecified", "sr": "Senior", "jr": "Junior"})


# =============================================================================
# 3. HEADLINE STATISTICS (printed for traceability)
# =============================================================================
n = len(df)
sal = df["avg_salary_k"]
print("\n=== HEADLINE ===")
print(f"N postings: {n}")
print(f"Avg salary (K): median {sal.median():.1f}, mean {sal.mean():.1f}, "
      f"min {sal.min():.1f}, max {sal.max():.1f}")

role_counts = df["role_grp"].value_counts()
role_sal = df.groupby("role_grp")["avg_salary_k"].median().sort_values(ascending=False)
print("\nRole group counts:\n", role_counts.to_string())
print("\nMedian salary by role group:\n", role_sal.round(1).to_string())

tool_demand = (df[TOOLS].mean() * 100).sort_values(ascending=False)
print("\nTool demand (% of postings):\n", tool_demand.round(1).to_string())

state_counts = df["job_state"].value_counts().head(8)
state_sal = df.groupby("job_state")["avg_salary_k"].median()
print("\nTop states by volume (count | median salary):")
for s in state_counts.index:
    print(f"  {s}: {state_counts[s]} | {state_sal[s]:.1f}")

deg_sal = df.groupby("deg")["avg_salary_k"].median()
print("\nMedian salary by degree:\n", deg_sal.round(1).to_string())

sen_sal = df.groupby("sen")["avg_salary_k"].agg(["count", "median"])
print("\nSalary by seniority:\n", sen_sal.round(1).to_string())

own = df["ownership_type"].apply(
    lambda x: "Private" if "Private" in str(x)
    else ("Public" if "Public" in str(x) else "Other"))
print("\nOwnership split:\n", own.value_counts().to_string())
print(f"\nCompany age (yrs): median {df.loc[df.company_age>=0,'company_age'].median():.0f}")
print(f"Company rating: median {df.loc[df.company_rating>0,'company_rating'].median():.2f}")
print("\nTop sectors:\n", df["sector"].value_counts().head(5).to_string())


# =============================================================================
# 4. FIGURES
# =============================================================================

# --- fig01: median salary by role group (the spine of the salary story) -------
# Inspect the ordered gap between the top and bottom role groups: this is the
# clearest single view of how compensation scales with role type.
order = role_sal.index.tolist()
fig, ax = plt.subplots(figsize=(8, 4.5))
colors = [ACCENT2 if r in ("ML Engineer", "Data Scientist") else ACCENT for r in order]
bars = ax.barh(order, role_sal[order].values, color=colors)
ax.invert_yaxis()
for b, r in zip(bars, order):
    ax.text(b.get_width() + 1.5, b.get_y() + b.get_height()/2,
            f"${role_sal[r]:.0f}K  (n={role_counts[r]})", va="center", fontsize=9)
ax.set_xlim(0, role_sal.max() * 1.25)
ax.set_xlabel("Median advertised salary (USD, thousands)")
ax.set_title("Median salary by role group, 2021 U.S. data-science postings")
fig.savefig(FIGDIR / "fig01-salary-by-role.png")
plt.close(fig)

# --- fig02: overall tool demand ----------------------------------------------
# The long-tail shape matters: a few core tools dominate while many specialized
# tools barely register. Highlight the three core tools clustered at the top.
fig, ax = plt.subplots(figsize=(8, 5.5))
labels = [t.replace("_", " ").title() for t in tool_demand.index]
cols = [ACCENT2 if v >= 50 else NEUTRAL for v in tool_demand.values]
bars = ax.barh(labels, tool_demand.values, color=cols)
ax.invert_yaxis()
for b, v in zip(bars, tool_demand.values):
    ax.text(b.get_width() + 0.6, b.get_y() + b.get_height()/2,
            f"{v:.0f}%", va="center", fontsize=9)
ax.set_xlim(0, 62)
ax.set_xlabel("Share of postings requiring the tool (%)")
ax.set_title("Tool and language demand across 742 postings")
fig.savefig(FIGDIR / "fig02-tool-demand.png")
plt.close(fig)

# --- fig03: geographic concentration (volume + pay together) ------------------
# Two encodings on one axis: bar height = posting volume, point = median salary.
# This shows whether the highest-volume markets also pay the most.
top_states = state_counts.index.tolist()
vol = state_counts.values
med = [state_sal[s] for s in top_states]
fig, ax1 = plt.subplots(figsize=(8.5, 4.5))
ax1.bar(top_states, vol, color=ACCENT, alpha=0.85, label="Posting volume")
ax1.set_ylabel("Number of postings", color=ACCENT)
ax1.tick_params(axis="y", labelcolor=ACCENT)
ax2 = ax1.twinx()
ax2.plot(top_states, med, color=ACCENT2, marker="o", linewidth=2,
         label="Median salary")
ax2.set_ylabel("Median salary (USD, thousands)", color=ACCENT2)
ax2.tick_params(axis="y", labelcolor=ACCENT2)
ax2.grid(False)
ax2.set_ylim(0, max(med) * 1.45)
for x, m in zip(top_states, med):
    ax2.text(x, m + 6, f"${m:.0f}K", ha="center", color=ACCENT2, fontsize=8)
ax1.set_title("Where the roles are vs. what they pay (top 8 states)")
ax1.set_xlabel("State")
fig.savefig(FIGDIR / "fig03-geo-concentration.png")
plt.close(fig)

# --- fig04: salary distribution by degree requirement -------------------------
# Box plots show the full spread, not just the center, exposing the degree
# gradient and its overlap rather than implying clean separation.
deg_order = ["Not specified", "Master's", "PhD"]
data_deg = [df.loc[df.deg == d, "avg_salary_k"].dropna().values for d in deg_order]
fig, ax = plt.subplots(figsize=(7.5, 4.5))
bp = ax.boxplot(data_deg, vert=True, patch_artist=True, widths=0.55,
                medianprops=dict(color="black", linewidth=2))
for patch in bp["boxes"]:
    patch.set_facecolor(ACCENT)
    patch.set_alpha(0.6)
ax.set_xticklabels([f"{d}\n(n={len(v)})" for d, v in zip(deg_order, data_deg)])
ax.set_ylabel("Average advertised salary (USD, thousands)")
ax.set_title("Salary by required degree level")
for i, v in enumerate(data_deg, start=1):
    ax.text(i, np.median(v) + 3, f"median ${np.median(v):.0f}K",
            ha="center", fontsize=8)
fig.savefig(FIGDIR / "fig04-salary-by-degree.png")
plt.close(fig)

# --- fig05: seniority premium -------------------------------------------------
# A focused comparison of the senior vs. unspecified bands (junior n=3 is shown
# but flagged as too small to interpret).
sen_order = ["Junior", "Unspecified", "Senior"]
sen_med = [df.loc[df.sen == s, "avg_salary_k"].median() for s in sen_order]
sen_n = [int((df.sen == s).sum()) for s in sen_order]
fig, ax = plt.subplots(figsize=(7, 4.2))
cols = [NEUTRAL, NEUTRAL, ACCENT2]
bars = ax.bar(sen_order, sen_med, color=cols)
for b, m, c in zip(bars, sen_med, sen_n):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 1.5,
            f"${m:.0f}K\n(n={c})", ha="center", fontsize=9)
ax.set_ylim(0, max(sen_med) * 1.25)
ax.set_ylabel("Median advertised salary (USD, thousands)")
ax.set_title("Senior roles command a clear pay premium")
fig.savefig(FIGDIR / "fig05-salary-by-seniority.png")
plt.close(fig)

# --- fig06: tool demand by role group (heatmap) -------------------------------
# A role x tool matrix exposes how skill bundles differ: analysts cluster on
# Excel/SQL, scientists/ML on Python and deep-learning libraries.
heat_roles = ["Analyst", "Data Engineer", "Data Scientist", "ML Engineer"]
heat_tools = ["excel", "sql", "python", "aws", "spark", "tableau",
              "scikit", "tensor", "pytorch", "keras"]
mat = np.array([[df.loc[df.role_grp == r, t].mean() * 100 for t in heat_tools]
                for r in heat_roles])
fig, ax = plt.subplots(figsize=(9, 3.8))
im = ax.imshow(mat, cmap="Blues", aspect="auto", vmin=0, vmax=100)
ax.set_xticks(range(len(heat_tools)))
ax.set_xticklabels([t.replace("_", " ").title() for t in heat_tools], rotation=40, ha="right")
ax.set_yticks(range(len(heat_roles)))
ax.set_yticklabels(heat_roles)
for i in range(len(heat_roles)):
    for j in range(len(heat_tools)):
        v = mat[i, j]
        ax.text(j, i, f"{v:.0f}", ha="center", va="center",
                color="white" if v > 55 else "#333", fontsize=8)
ax.set_title("Tool demand (%) by role group")
fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02, label="% of postings")
ax.grid(False)
fig.savefig(FIGDIR / "fig06-tool-by-role.png")
plt.close(fig)

# --- fig07: employer profile (ownership + top sectors) ------------------------
# Context for "who is hiring": ownership split and the leading sectors.
fig, (axa, axb) = plt.subplots(1, 2, figsize=(10, 4))
oc = own.value_counts()[["Private", "Public", "Other"]]
axa.bar(oc.index, oc.values, color=[ACCENT, NEUTRAL, NEUTRAL])
for i, v in enumerate(oc.values):
    axa.text(i, v + 5, str(v), ha="center", fontsize=9)
axa.set_title("Ownership type")
axa.set_ylabel("Number of postings")
axa.set_ylim(0, oc.max() * 1.2)
sec = df["sector"].value_counts().head(6)[::-1]
axb.barh(sec.index, sec.values, color=ACCENT)
for i, v in enumerate(sec.values):
    axb.text(v + 1.5, i, str(v), va="center", fontsize=9)
axb.set_title("Leading sectors")
axb.set_xlabel("Number of postings")
axb.set_xlim(0, sec.max() * 1.25)
fig.suptitle("Employer profile of hiring organizations", fontweight="bold")
fig.savefig(FIGDIR / "fig07-employer-profile.png")
plt.close(fig)

print("\nSaved 7 figures to", FIGDIR)
for p in sorted(FIGDIR.glob("*.png")):
    print(" -", p.name)
