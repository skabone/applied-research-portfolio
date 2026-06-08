"""Attach statistical inference to the 4/5ths adverse-impact flags.

The 4/5ths rule is a point estimate: it compares two observed pass rates and
ignores how many candidates produced them, so a flag from a 20-person cell is
treated the same as a flag from a 200-person cell. This script adds the missing
piece. For every flagged subgroup it (1) runs a two-proportion z-test against the
stage's highest-passing comparison group and (2) puts a 95% confidence interval
around the impact ratio, so a reader can tell which flags reflect a stable
difference and which are small-sample noise.

Outputs ``analysis/outputs/impact_inference.csv`` and renders
``docs/figures/impact_ratio_ci.png``. Run after ``run_analysis.py``:

    python3 analysis/run_analysis.py
    python3 analysis/inferential_tests.py
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis" / "outputs"
FIG = ROOT / "docs" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

THRESHOLD = 0.80
PARITY = 1.0


def _norm_sf(z: float) -> float:
    """Upper-tail standard-normal probability via the complementary error
    function (keeps the script dependency-light — no SciPy required)."""
    return 0.5 * math.erfc(z / math.sqrt(2))


def _two_proportion_z(x1: int, n1: int, x2: int, n2: int) -> tuple[float, float]:
    """Two-proportion z-test under the pooled-variance null that the focal and
    comparison groups share one underlying pass rate. Returns (z, two-sided p)."""
    p1, p2 = x1 / n1, x2 / n2
    pooled = (x1 + x2) / (n1 + n2)
    se = math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    if se == 0:
        return 0.0, 1.0
    z = (p1 - p2) / se
    return z, 2 * _norm_sf(abs(z))


def _impact_ratio_ci(p1: float, n1: int, p2: float, n2: int) -> tuple[float, float, float]:
    """Impact ratio (focal rate / comparison rate) with a 95% CI built on the
    log scale, the standard relative-risk interval. A CI whose upper bound sits
    below 1.0 means the gap is distinguishable from parity at 95% confidence."""
    ir = p1 / p2
    se_log = math.sqrt((1 - p1) / (p1 * n1) + (1 - p2) / (p2 * n2))
    lo = math.exp(math.log(ir) - 1.96 * se_log)
    hi = math.exp(math.log(ir) + 1.96 * se_log)
    return ir, lo, hi


def main() -> None:
    rows = list(csv.DictReader((OUT / "adverse_impact_screen.csv").open()))

    # Group the screen by dimension+stage so each group can be compared to the
    # highest-passing group at its own stage (the impact-ratio denominator).
    from collections import defaultdict
    cells = defaultdict(list)
    for r in rows:
        cells[(r["dimension"], r["stage"])].append(r)

    results = []
    for (dim, stage), rs in cells.items():
        if stage == "applied":
            continue  # everyone passes intake; no contrast to test
        top = max(rs, key=lambda x: float(x["pass_rate"]))
        x2, n2, p2 = int(top["n_passed"]), int(top["n_total"]), float(top["pass_rate"])
        for r in rs:
            if r["group_name"] == top["group_name"]:
                continue
            if int(r["flagged_under_4_5ths"]) != 1:
                continue  # inference is reported for the flagged cells
            x1, n1, p1 = int(r["n_passed"]), int(r["n_total"]), float(r["pass_rate"])
            if p1 == 0:
                continue
            z, pval = _two_proportion_z(x1, n1, x2, n2)
            ir, lo, hi = _impact_ratio_ci(p1, n1, p2, n2)
            results.append({
                "dimension": dim, "stage": stage, "group_name": r["group_name"],
                "comparison_group": top["group_name"], "n_focal": n1, "pass_rate": round(p1, 4),
                "impact_ratio": round(ir, 4), "ci_low": round(lo, 4), "ci_high": round(hi, 4),
                "z": round(z, 3), "p_value": round(pval, 4),
                "significant_05": int(pval < 0.05),
            })

    results.sort(key=lambda d: (d["dimension"], d["stage"], d["group_name"]))
    with (OUT / "impact_inference.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    # Forest-style plot: impact ratio per flagged cell with its 95% CI, the 0.80
    # screening threshold, and the 1.00 parity line. Whether a CI crosses 1.00 is
    # the visual test for statistical reliability.
    labels = [f"{r['group_name']}\n{r['stage']} (n={r['n_focal']})" for r in results]
    irs = [r["impact_ratio"] for r in results]
    los = [r["impact_ratio"] - r["ci_low"] for r in results]
    his = [r["ci_high"] - r["impact_ratio"] for r in results]
    sig = [r["significant_05"] for r in results]
    colors = ["#c0392b" if s else "#90a4ae" for s in sig]

    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    y = range(len(results))
    ax.errorbar(irs, list(y), xerr=[los, his], fmt="none", ecolor="#555555",
                elinewidth=1.4, capsize=4, zorder=1)
    ax.scatter(irs, list(y), c=colors, s=70, zorder=2, edgecolor="white", linewidth=0.8)
    ax.axvline(PARITY, color="#222", linewidth=1.1)
    ax.axvline(THRESHOLD, color="#222", linestyle="--", linewidth=1.1)
    ax.text(PARITY + 0.01, -0.62, "parity (1.00)", va="center", ha="left", fontsize=8.5)
    ax.text(THRESHOLD - 0.01, -0.62, "0.80", va="center", ha="right", fontsize=8.5)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, 1.5)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:.2f}"))
    ax.set_xlabel("Impact ratio with 95% confidence interval")
    ax.set_title("Which 4/5ths flags hold up to a significance test?", fontweight="bold")
    for sp in ["top", "right"]:
        ax.spines[sp].set_visible(False)
    ax.invert_yaxis()
    # Annotate each point with its p-value so the figure is self-contained.
    for yi, r in zip(y, results):
        ax.text(1.52, yi, f"p={r['p_value']:.3f}", va="center", fontsize=8.5,
                color="#c0392b" if r["significant_05"] else "#555555")
    ax.text(0.0, -0.16,
            "Red = significant at p<.05 (CI excludes parity). Grey = not distinguishable from parity.",
            transform=ax.transAxes, fontsize=8.5, color="#555555")
    fig.tight_layout()
    fig.savefig(FIG / "impact_ratio_ci.png", bbox_inches="tight", dpi=140)
    plt.close(fig)

    for r in results:
        print(f"{r['dimension'][:4]} {r['stage']:11} {r['group_name']:16} "
              f"IR={r['impact_ratio']:.3f} CI=[{r['ci_low']:.3f},{r['ci_high']:.3f}] "
              f"p={r['p_value']:.4f} sig={r['significant_05']}")
    print("Wrote: analysis/outputs/impact_inference.csv and docs/figures/impact_ratio_ci.png")


if __name__ == "__main__":
    main()
