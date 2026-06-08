"""Generate the project's figures from the SQL-derived output tables.

This script reads the three result tables written by ``run_analysis.py``
(``funnel_metrics.csv``, ``subgroup_selection_ratios.csv``, and
``adverse_impact_screen.csv``) and renders three publication-quality
figures into ``docs/figures/``. Keeping figure generation separate from the
SQL run means the visuals can be rebuilt without touching the data layer, and
every figure traces back to a committed output table rather than to ad-hoc
in-memory state.

Run after ``run_analysis.py``:

    python3 analysis/run_analysis.py
    python3 analysis/make_figures.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

# Resolve project-relative paths so the script runs from anywhere in the repo.
# All inputs are committed CSVs; all outputs land in docs/figures/.
ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "analysis" / "outputs"
FIG_DIR = ROOT / "docs" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# A single muted, color-blind-safe palette is reused across figures so the
# same race/ethnicity group keeps the same color everywhere it appears.
THRESHOLD = 0.80  # 4/5ths (80%) rule reference line for the impact-ratio plot
INK = "#222222"
GRID = "#d9d9d9"
ACCENT = "#2b6cb0"
FLAG = "#c0392b"     # used for bars that fall below the 4/5ths threshold
NEUTRAL = "#90a4ae"  # used for bars at or above the threshold

# Stages in pipeline order. "applied" is the intake gate (everyone "passes"),
# so the subgroup/impact figures focus on the evaluative stages after it.
STAGE_ORDER = ["applied", "screen", "assessment", "interview", "offer", "hire"]
EVAL_STAGES = ["screen", "assessment", "interview", "offer", "hire"]

plt.rcParams.update({
    "font.size": 11,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "figure.dpi": 140,
})


def _clean_axes(ax) -> None:
    """Apply a minimal, readable theme: no top/right spines, soft y-grid."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def figure_funnel() -> Path:
    """Figure 1 — candidate counts at each pipeline stage, with the
    stage-to-stage conversion rate annotated between bars."""
    funnel = pd.read_csv(OUT_DIR / "funnel_metrics.csv").sort_values("stage_order")
    stages = funnel["stage"].tolist()
    counts = funnel["candidates"].tolist()

    fig, ax = plt.subplots(figsize=(8, 4.6))
    bars = ax.bar(stages, counts, color=ACCENT, width=0.62)
    _clean_axes(ax)
    ax.set_title("Hiring funnel: candidates remaining at each stage", fontweight="bold")
    ax.set_ylabel("Candidates (count)")
    ax.set_ylim(0, max(counts) * 1.16)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    # Label each bar with its absolute count, and annotate the share of the
    # previous stage that advanced (the stage-to-stage conversion rate).
    for i, (bar, n) in enumerate(zip(bars, counts)):
        ax.text(bar.get_x() + bar.get_width() / 2, n + max(counts) * 0.02,
                f"{n:,}", ha="center", va="bottom", fontsize=10, fontweight="bold")
        if i > 0 and counts[i - 1] > 0:
            conv = n / counts[i - 1]
            ax.text(bar.get_x() + bar.get_width() / 2, n / 2,
                    f"{conv:.0%}", ha="center", va="center", color="white",
                    fontsize=9, fontweight="bold")

    ax.text(0.0, -0.22,
            "Percentages show the share of the previous stage that advanced.",
            transform=ax.transAxes, fontsize=8.5, color="#555555")
    fig.tight_layout()
    out = FIG_DIR / "funnel_counts.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def figure_subgroup_pass_rates() -> Path:
    """Figure 2 — pass (selection) rate by race/ethnicity group across the
    evaluative stages, read from the aggregated adverse-impact table."""
    ai = pd.read_csv(OUT_DIR / "adverse_impact_screen.csv")
    race = ai[(ai["dimension"] == "race_ethnicity_group")
              & (ai["stage"].isin(["screen", "assessment", "interview", "offer", "hire"]))].copy()
    stages = ["screen", "assessment", "interview", "offer", "hire"]
    groups = ["Asian", "Black", "Hispanic/Latino", "Two+", "Unknown", "White"]
    palette = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#a6761d", "#666666"]

    pivot = race.pivot_table(index="stage", columns="group_name",
                             values="pass_rate").reindex(stages)[groups]

    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    x = range(len(stages))
    width = 0.13
    for j, (g, color) in enumerate(zip(groups, palette)):
        offsets = [i + (j - 2.5) * width for i in x]
        ax.bar(offsets, pivot[g].values, width=width, label=g, color=color)
    _clean_axes(ax)
    ax.set_title("Selection (pass) rate by race/ethnicity across pipeline stages",
                 fontweight="bold")
    ax.set_ylabel("Pass rate")
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_xticks(list(x))
    ax.set_xticklabels([s.capitalize() for s in stages])
    ax.legend(title="Race/ethnicity", ncol=3, fontsize=8.5, title_fontsize=9,
              loc="upper center", bbox_to_anchor=(0.5, -0.12), frameon=False)
    fig.tight_layout()
    out = FIG_DIR / "subgroup_pass_rates.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def figure_adverse_impact() -> Path:
    """Figure 3 — adverse-impact ratio by race/ethnicity group at the two
    stages where flags appear (assessment, hire), with the 0.80 threshold
    line. Bars below 0.80 are colored to mark the review trigger."""
    ai = pd.read_csv(OUT_DIR / "adverse_impact_screen.csv")
    race = ai[ai["dimension"] == "race_ethnicity_group"].copy()
    stages = ["assessment", "hire"]
    groups = ["Asian", "Black", "Hispanic/Latino", "Two+", "Unknown", "White"]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
    for ax, stage in zip(axes, stages):
        sub = race[race["stage"] == stage].set_index("group_name").reindex(groups)
        ratios = sub["impact_ratio"].values
        colors = [FLAG if r < THRESHOLD else NEUTRAL for r in ratios]
        bars = ax.bar(groups, ratios, color=colors, width=0.66)
        ax.axhline(THRESHOLD, color=INK, linestyle="--", linewidth=1.2)
        ax.text(len(groups) - 0.5, THRESHOLD + 0.015, "0.80 (4/5ths) threshold",
                ha="right", va="bottom", fontsize=8.5, color=INK)
        _clean_axes(ax)
        ax.set_title(f"{stage.capitalize()} stage", fontweight="bold")
        ax.set_ylim(0, 1.08)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:.2f}"))
        ax.set_xticks(range(len(groups)))
        ax.set_xticklabels(groups, rotation=30, ha="right", fontsize=9)
        for bar, r in zip(bars, ratios):
            ax.text(bar.get_x() + bar.get_width() / 2, r + 0.02, f"{r:.2f}",
                    ha="center", va="bottom", fontsize=8.5,
                    fontweight="bold" if r < THRESHOLD else "normal",
                    color=FLAG if r < THRESHOLD else INK)
    axes[0].set_ylabel("Impact ratio (group rate / highest group rate)")
    fig.suptitle("Adverse-impact ratios by race/ethnicity: bars below 0.80 flag for review",
                 fontweight="bold", y=1.02)
    fig.tight_layout()
    out = FIG_DIR / "adverse_impact_ratios.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def figure_adverse_impact_gender() -> Path:
    """Figure 4 — adverse-impact ratios by gender group across the evaluative
    stages, screening the second protected dimension. The single gender flag
    (Nonbinary/Other at hire) rests on a very small cell, so its label carries n."""
    ai = pd.read_csv(OUT_DIR / "adverse_impact_screen.csv")
    gen = ai[(ai["dimension"] == "gender_group") & (ai["stage"] != "applied")].copy()
    stages = ["screen", "assessment", "interview", "offer", "hire"]
    groups = ["Men", "Women", "Nonbinary/Other", "Unknown"]
    pivot = gen.pivot_table(index="stage", columns="group_name",
                            values="impact_ratio").reindex(stages)[groups]
    n_by = gen.pivot_table(index="stage", columns="group_name",
                           values="n_total").reindex(stages)[groups]

    palette = {"Men": "#2b6cb0", "Women": "#1b9e77", "Nonbinary/Other": "#d95f02", "Unknown": "#666666"}
    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    x = range(len(stages))
    width = 0.2
    for j, g in enumerate(groups):
        offs = [i + (j - 1.5) * width for i in x]
        vals = pivot[g].values
        # Color any bar that falls below the 0.80 line as a flag.
        colors = [FLAG if (pd.notna(v) and v < THRESHOLD) else palette[g] for v in vals]
        ax.bar(offs, vals, width=width, label=g, color=colors)
    ax.axhline(THRESHOLD, color=INK, linestyle="--", linewidth=1.2)
    ax.text(len(stages) - 0.5, THRESHOLD + 0.015, "0.80 (4/5ths) threshold",
            ha="right", va="bottom", fontsize=8.5, color=INK)
    _clean_axes(ax)
    ax.set_title("Adverse-impact ratios by gender across pipeline stages", fontweight="bold")
    ax.set_ylabel("Impact ratio")
    ax.set_ylim(0, 1.12)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:.2f}"))
    ax.set_xticks(list(x))
    ax.set_xticklabels([s.capitalize() for s in stages])
    # Mark the one flagged cell with its small sample size.
    nb_hire_n = int(n_by.loc["hire", "Nonbinary/Other"])
    ax.annotate(f"n={nb_hire_n}", xy=(4 + 0.5 * width, pivot.loc["hire", "Nonbinary/Other"]),
                xytext=(0, 6), textcoords="offset points", ha="center", fontsize=8.5,
                color=FLAG, fontweight="bold")
    ax.legend(title="Gender group", ncol=4, fontsize=8.5, title_fontsize=9,
              loc="upper center", bbox_to_anchor=(0.5, -0.12), frameon=False)
    fig.tight_layout()
    out = FIG_DIR / "adverse_impact_gender.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    written = [figure_funnel(), figure_subgroup_pass_rates(),
               figure_adverse_impact(), figure_adverse_impact_gender()]
    for path in written:
        print("Wrote:", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
