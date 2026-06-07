# =============================================================================
# County-Level Broadband Access in the United States — Analysis Pipeline
# =============================================================================
# Reproducible source for the figures and statistics reported in
# 01_Project_Summary.md and 02_Project_Report.md.
#
# Data: public county-level extract (IMLS Indicators Workbook + BroadbandNow
#       Open Data Challenge), 3,142 raw rows -> 3,102 counties after cleaning.
# Run:  python 04_Source_Code.py   (writes 7 figures to docs/figures/)
#
# Every number printed here is the number used in the written documents, so the
# documents can be re-verified by re-running this file.
# =============================================================================

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# 0. Paths and shared plot style
# -----------------------------------------------------------------------------
# Resolve paths relative to this file so the pipeline runs from the project
# folder or the repository root without editing absolute paths.
HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "broadband_access.csv"
if not DATA.exists():                      # fallback to the legacy in-folder copy
    DATA = HERE / "broadband_access.csv"
FIG = HERE / "docs" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 110, "savefig.dpi": 110, "savefig.bbox": "tight",
    "axes.grid": True, "grid.alpha": 0.25,
    "font.size": 11, "axes.titlesize": 13, "axes.titleweight": "bold",
})
INK = "#1b3a5b"      # primary
ACC = "#c0392b"      # accent / "worse" highlight
GRN = "#2e7d52"      # "better" highlight


def save(fig, name):
    """Write a figure to docs/figures/ and report the path."""
    p = FIG / name
    fig.savefig(p)
    plt.close(fig)
    print(f"  saved {p.relative_to(HERE)}")


# -----------------------------------------------------------------------------
# 1. Load and clean
# -----------------------------------------------------------------------------
# The raw extract is latin-1 encoded. Cleaning mirrors the original RapidMiner
# workflow: drop the redundant BroadbandNow price column, drop the 40 rows
# (1.3%) missing the IMLS cost field, mean-impute five near-complete continuous
# fields, fill the two single-county gaps from public reference values, and drop
# the two BroadbandNow columns superseded by more reliable IMLS equivalents
# (population and provider count: BroadbandNow averaged ~12 providers/county vs.
# the FCC national average near 4, an implausible figure).
def load_clean():
    df = pd.read_csv(DATA, encoding="latin1")
    raw = df.shape
    df = df.drop(columns=["Lowestpricepermonth_bbn"]).dropna(subset=["broad_cost"])
    for c in ["wired_bbn", "all25_bbn", "downave_bbn", "access_bbn", "slowfrac_bbn"]:
        df[c] = df[c].fillna(df[c].mean())
    df["unemp_19%"] = df["unemp_19%"].fillna(21.0)        # Kalawao County, HI
    df["poverty_rate%"] = df["poverty_rate%"].fillna(24.0)  # Rio Arriba County, NM
    df = df.drop(columns=["population_bbn", "provide_bbn"])
    print(f"Raw {raw} -> clean {df.shape}")
    return df


# Census region lookup so geographic patterns can be summarized at the region
# level instead of relying on the eye to group 49 states on a chart.
NE = {"Connecticut", "Maine", "Massachusetts", "New Hampshire", "Rhode Island",
      "Vermont", "New Jersey", "New York", "Pennsylvania"}
MW = {"Illinois", "Indiana", "Michigan", "Ohio", "Wisconsin", "Iowa", "Kansas",
      "Minnesota", "Missouri", "Nebraska", "North Dakota", "South Dakota"}
S = {"Delaware", "Florida", "Georgia", "Maryland", "North Carolina",
     "South Carolina", "Virginia", "West Virginia", "District of Columbia",
     "Alabama", "Kentucky", "Mississippi", "Tennessee", "Arkansas",
     "Louisiana", "Oklahoma", "Texas"}
W = {"Arizona", "Colorado", "Idaho", "Montana", "Nevada", "New Mexico", "Utah",
     "Wyoming", "Alaska", "California", "Hawaii", "Oregon", "Washington"}


def region_of(state):
    if state in NE: return "Northeast"
    if state in MW: return "Midwest"
    if state in S:  return "South"
    if state in W:  return "West"
    return "Other"


# -----------------------------------------------------------------------------
# 2. Headline statistics (printed so the docs are re-verifiable)
# -----------------------------------------------------------------------------
def headline_stats(df):
    hb = df["home_havebroad%"]
    rp = hb.corr(df["poverty_rate%"])
    ra = hb.corr(df["broad_avail"])
    print("\n=== HEADLINE STATISTICS ===")
    print(f"Counties: {len(df)}  Variables: {df.shape[1]}")
    print(f"Home broadband %: median {hb.median():.1f}, "
          f"p5 {hb.quantile(.05):.1f}, p95 {hb.quantile(.95):.1f}, "
          f"range {hb.min():.1f}-{hb.max():.1f} ({hb.max()-hb.min():.1f} pts)")
    print(f"Poverty corr r = {rp:+.3f} | Availability corr r = {ra:+.3f}")
    return rp, ra


# -----------------------------------------------------------------------------
# 3. Figures
# -----------------------------------------------------------------------------
def fig01_distribution(df):
    # How wide is the county-level gap that national/state averages hide?
    hb = df["home_havebroad%"]
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.hist(hb, bins=40, color=INK, alpha=0.85, edgecolor="white")
    ax.axvline(hb.median(), color=ACC, lw=2,
               label=f"Median {hb.median():.1f}%")
    ax.axvline(hb.quantile(.05), color="#888", ls="--", lw=1.3,
               label=f"5th pct {hb.quantile(.05):.1f}%")
    ax.axvline(hb.quantile(.95), color="#888", ls=":", lw=1.3,
               label=f"95th pct {hb.quantile(.95):.1f}%")
    ax.set(title="County home-broadband adoption spans a 70-point range",
           xlabel="Households with home broadband (%)", ylabel="Counties")
    ax.legend(frameon=False)
    save(fig, "fig01-broadband-distribution.png")


def fig02_poverty_scatter(df):
    # The single strongest correlate of actual adoption.
    x, y = df["poverty_rate%"], df["home_havebroad%"]
    r = x.corr(y)
    b, a = np.polyfit(x, y, 1)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, y, s=8, alpha=0.30, color=INK, edgecolors="none")
    xs = np.linspace(x.min(), x.max(), 100)
    ax.plot(xs, a + b * xs, color=ACC, lw=2.4,
            label=f"OLS fit (r = {r:.2f}, slope {b:.2f} pts/1% poverty)")
    ax.set(title="Higher-poverty counties have markedly lower broadband adoption",
           xlabel="Poverty rate (%)", ylabel="Households with home broadband (%)")
    ax.legend(frameon=False)
    save(fig, "fig02-poverty-vs-broadband.png")


def fig03_correlates(df):
    # Poverty (a need/affordability signal) vs. formal availability (an
    # infrastructure signal): which tracks real adoption more closely?
    fac = {"Poverty rate": "poverty_rate%", "SNAP receipt": "SNAP_recieved%",
           "Avg download speed": "downave_bbn", "No health insurance": "nohealth_ins%",
           "Unemployment": "unemp_19%", "Formal availability": "broad_avail",
           "Provider count": "broadProviders_num", "Monthly cost": "broad_cost"}
    rows = [(k, df["home_havebroad%"].corr(df[v])) for k, v in fac.items()]
    rows.sort(key=lambda t: abs(t[1]))
    labels = [r[0] for r in rows]
    vals = [r[1] for r in rows]
    colors = [GRN if v > 0 else ACC for v in vals]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(labels, [abs(v) for v in vals], color=colors, alpha=0.9)
    for i, v in enumerate(vals):
        ax.text(abs(v) + 0.01, i, f"{v:+.2f}", va="center", fontsize=9)
    ax.set(title="Poverty correlates with adoption more than infrastructure does",
           xlabel="|Pearson correlation| with home-broadband adoption", xlim=(0, 0.75))
    ax.text(0.74, 0.5, "red = negative   green = positive", ha="right",
            transform=ax.transAxes, fontsize=8, color="#666")
    save(fig, "fig03-adoption-correlates.png")


def fig04_states(df):
    # Where the gaps concentrate: 10 lowest and 10 highest states by county mean.
    st = df.groupby("state")["home_havebroad%"].mean().sort_values()
    sub = pd.concat([st.head(10), st.tail(10)])
    colors = [ACC] * 10 + [GRN] * 10
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.barh(sub.index, sub.values, color=colors, alpha=0.9)
    ax.axvline(df["home_havebroad%"].mean(), color="#444", ls="--", lw=1,
               label=f"National county mean {df['home_havebroad%'].mean():.1f}%")
    for i, v in enumerate(sub.values):
        ax.text(v + 0.3, i, f"{v:.1f}", va="center", fontsize=8)
    ax.set(title="Lowest- and highest-adoption states (county-mean broadband)",
           xlabel="Mean county home broadband (%)", xlim=(55, 90))
    ax.legend(frameon=False, loc="lower right")
    save(fig, "fig04-state-ranking.png")


def fig05_poverty_quartile(df):
    # Socioeconomic equity: adoption stepped down across poverty quartiles.
    d = df.copy()
    d["q"] = pd.qcut(d["poverty_rate%"], 4,
                     labels=["Q1\nlowest poverty", "Q2", "Q3", "Q4\nhighest poverty"])
    m = d.groupby("q", observed=True)["home_havebroad%"].mean()
    fig, ax = plt.subplots(figsize=(7.5, 5))
    bars = ax.bar(m.index.astype(str), m.values,
                  color=[GRN, "#7fae8f", "#c98f86", ACC], alpha=0.92)
    for b, v in zip(bars, m.values):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, f"{v:.1f}%",
                ha="center", fontsize=10, fontweight="bold")
    ax.set(title=f"Broadband adoption falls {m.iloc[0]-m.iloc[-1]:.0f} points "
                 f"from lowest- to highest-poverty counties",
           ylabel="Mean home broadband (%)", ylim=(55, 85))
    save(fig, "fig05-poverty-quartile.png")


def fig06_avail_vs_adoption(df):
    # Availability is not adoption: many fully-covered counties still lag.
    x, y = df["broad_avail"], df["home_havebroad%"]
    hi = df[df["broad_avail"] >= 90]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, y, s=8, alpha=0.25, color=INK, edgecolors="none")
    ax.scatter(hi["broad_avail"], hi["home_havebroad%"], s=10, alpha=0.5,
               color=ACC, edgecolors="none",
               label=f"availability >=90% (n={len(hi)}, "
                     f"mean adoption {hi['home_havebroad%'].mean():.1f}%)")
    ax.plot([0, 100], [0, 100], color="#444", ls="--", lw=1, label="parity line")
    ax.set(title="Formal availability does not guarantee adoption",
           xlabel="Formal broadband availability (%)",
           ylabel="Households with home broadband (%)")
    ax.legend(frameon=False, loc="lower right")
    save(fig, "fig06-availability-vs-adoption.png")


def fig07_region(df):
    # Regional gradient at a glance.
    d = df.copy()
    d["region"] = d["state"].map(region_of)
    m = d.groupby("region")["home_havebroad%"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    bars = ax.bar(m.index, m.values,
                  color=[ACC, "#c98f86", "#7fae8f", GRN], alpha=0.92)
    for b, v in zip(bars, m.values):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.3, f"{v:.1f}%",
                ha="center", fontsize=10, fontweight="bold")
    ax.set(title="The South trails other regions on broadband adoption",
           ylabel="Mean county home broadband (%)", ylim=(60, 85))
    save(fig, "fig07-region.png")


def main():
    df = load_clean()
    headline_stats(df)
    print("\n=== FIGURES ===")
    fig01_distribution(df)
    fig02_poverty_scatter(df)
    fig03_correlates(df)
    fig04_states(df)
    fig05_poverty_quartile(df)
    fig06_avail_vs_adoption(df)
    fig07_region(df)
    print("\nDone.")


if __name__ == "__main__":
    main()
