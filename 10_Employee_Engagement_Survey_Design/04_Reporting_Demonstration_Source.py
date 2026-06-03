# ==============================================================================
# Employee Engagement Pulse Survey — Reporting & Scoring Demonstration
# ------------------------------------------------------------------------------
# WHAT THIS FILE IS AND WHY IT EXISTS
#
# Project 10 is a survey-DESIGN project: the deliverable is the instrument and
# the measurement plan, not an analysis of collected responses. No real
# employees were surveyed. To show how the designed instrument would actually
# behave once fielded — how subscale scores are computed, how reliability is
# checked, and how results are reported to leadership — this script generates a
# small ILLUSTRATIVE SYNTHETIC dataset that matches the instrument structure
# (3 subscales x 5 items, 5-point Likert, quarterly waves, department strata)
# and then runs the exact scoring/reporting pipeline specified in the design.
#
# The numbers below are simulated for demonstration. They are NOT real
# engagement data and must not be read as findings about any organization.
# The value of the figures is that they make the abstract scoring/reporting
# framework in the design specification concrete and inspectable.
# ==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Deterministic seed so the synthetic illustration is reproducible across runs.
RNG = np.random.default_rng(42)

OUT = "docs/figures"

# Instrument structure exactly as specified in the design (UWES-15 mapping).
SUBSCALES = {
    "Vigor": [f"V{i}" for i in range(1, 6)],
    "Dedication": [f"D{i}" for i in range(1, 6)],
    "Absorption": [f"A{i}" for i in range(1, 6)],
}
DEPARTMENTS = ["HR", "Sales", "Marketing", "Technical/IT",
               "Customer Support", "Operations", "Management"]
QUARTERS = ["2024 Q1", "2024 Q2", "2024 Q3", "2024 Q4"]

# Color palette kept colorblind-friendly and consistent across every figure.
PALETTE = {"Vigor": "#2c7fb8", "Dedication": "#41ab5d", "Absorption": "#d95f0e"}


def simulate_wave(quarter_index):
    """Simulate one quarterly wave of responses.

    WHY THIS DESIGN: each department is given a latent 'true' engagement level
    so that subgroup differences are visible (the reporting framework's whole
    point is detecting them). Item responses are drawn around the subscale mean
    and clipped to the 1-5 Likert range, mimicking how real Likert items behave.
    A small positive drift over quarters lets the trend figure show movement.
    """
    rows = []
    # Stable department baselines (some departments structurally more engaged).
    dept_offsets = {d: o for d, o in zip(
        DEPARTMENTS, [0.25, -0.35, 0.10, 0.20, -0.45, -0.10, 0.40])}
    subscale_base = {"Vigor": 3.6, "Dedication": 3.8, "Absorption": 3.5}
    for dept in DEPARTMENTS:
        n = RNG.integers(24, 38)  # ~30/dept, matching the n>=30 sampling target
        for _ in range(n):
            row = {"quarter": QUARTERS[quarter_index], "department": dept}
            for sub, items in SUBSCALES.items():
                # Person-level true score + dept offset + slow quarterly drift.
                mu = (subscale_base[sub] + dept_offsets[dept]
                      + 0.05 * quarter_index + RNG.normal(0, 0.35))
                for it in items:
                    val = np.clip(round(mu + RNG.normal(0, 0.6)), 1, 5)
                    row[it] = int(val)
            rows.append(row)
    return pd.DataFrame(rows)


def cronbach_alpha(df_items):
    """Cronbach's alpha = internal-consistency reliability of a set of items.

    Formula: alpha = (k/(k-1)) * (1 - sum(item_var)/total_var), where k is the
    item count. It estimates how consistently the items measure one construct.
    The design specifies alpha >= .70 as the acceptability threshold, so we
    compute it per subscale per wave to mirror the planned QA check.
    """
    k = df_items.shape[1]
    item_var = df_items.var(axis=0, ddof=1).sum()
    total_var = df_items.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - item_var / total_var)


# Build the full multi-wave synthetic dataset and persist it so the figures are
# fully reproducible from a committed artifact.
panel = pd.concat([simulate_wave(i) for i in range(len(QUARTERS))],
                  ignore_index=True)
for sub, items in SUBSCALES.items():
    panel[sub] = panel[items].mean(axis=1)
panel["Total"] = panel[[*sum(SUBSCALES.values(), [])]].mean(axis=1)
panel.to_csv("data/illustrative_engagement_synthetic.csv", index=False)

# ------------------------------------------------------------------------------
# FIGURE 1 (HERO): Instrument blueprint — the designed three-factor structure.
# Shows reviewers the construct map at a glance: one engagement construct, three
# subscales, five items each, before any data is involved.
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.2))
ax.axis("off")
ax.set_title("Employee Engagement Pulse Survey — Instrument Blueprint\n"
             "UWES-15: one construct, three subscales, five items each",
             fontsize=13, fontweight="bold")
# Top construct box.
ax.add_patch(FancyBboxPatch((3.7, 4.4), 2.6, 0.7, boxstyle="round,pad=0.05",
             fc="#253494", ec="none"))
ax.text(5.0, 4.75, "Work Engagement", color="white", ha="center",
        va="center", fontsize=11, fontweight="bold")
sub_x = {"Vigor": 1.7, "Dedication": 5.0, "Absorption": 8.3}
for sub, x in sub_x.items():
    ax.add_patch(FancyBboxPatch((x - 1.1, 3.0), 2.2, 0.6,
                 boxstyle="round,pad=0.05", fc=PALETTE[sub], ec="none"))
    ax.text(x, 3.3, sub, color="white", ha="center", va="center",
            fontsize=10, fontweight="bold")
    ax.plot([5.0, x], [4.4, 3.6], color="#888", lw=1)
    for j, it in enumerate(SUBSCALES[sub]):
        y = 2.4 - j * 0.42
        ax.add_patch(FancyBboxPatch((x - 0.95, y - 0.16), 1.9, 0.32,
                     boxstyle="round,pad=0.02", fc="#f0f0f0", ec="#cccccc"))
        ax.text(x, y, it, ha="center", va="center", fontsize=8.5)
        ax.plot([x, x], [3.0, y + 0.16], color="#ccc", lw=0.6)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.4)
plt.tight_layout()
plt.savefig(f"{OUT}/instrument-blueprint-1.png", dpi=150, bbox_inches="tight")
plt.close()

# ------------------------------------------------------------------------------
# FIGURE 2: Quarterly trend by subscale (the core monitoring view).
# Demonstrates the design's primary purpose: tracking engagement over time so
# decline is visible before it shows up in attrition.
# ------------------------------------------------------------------------------
trend = panel.groupby("quarter")[["Vigor", "Dedication", "Absorption"]].mean()
trend = trend.reindex(QUARTERS)
fig, ax = plt.subplots(figsize=(8, 4.8))
for sub in ["Vigor", "Dedication", "Absorption"]:
    ax.plot(trend.index, trend[sub], marker="o", lw=2,
            color=PALETTE[sub], label=sub)
ax.axhline(4.0, ls="--", color="#999", lw=1)
ax.text(0.02, 4.02, "Engaged threshold (4.0)", transform=ax.get_yaxis_transform(),
        fontsize=8, color="#666")
ax.set_ylim(3.2, 4.3)
ax.set_ylabel("Mean subscale score (1–5 Likert)")
ax.set_xlabel("Survey wave (quarterly)")
ax.set_title("Illustrative Quarterly Engagement Trend by Subscale\n"
             "(synthetic demonstration data)", fontsize=12, fontweight="bold")
ax.legend(title="Subscale", frameon=False)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/quarterly-trend-1.png", dpi=150, bbox_inches="tight")
plt.close()

# ------------------------------------------------------------------------------
# FIGURE 3: Department subgroup comparison (latest wave).
# Demonstrates the stratified reporting layer: where engagement concentrates and
# which subgroups would be flagged for targeted follow-up.
# ------------------------------------------------------------------------------
latest = panel[panel["quarter"] == QUARTERS[-1]]
dept_means = latest.groupby("department")["Total"].mean().sort_values()
fig, ax = plt.subplots(figsize=(8, 4.8))
colors = ["#d73027" if v < 3.5 else "#4575b4" for v in dept_means.values]
ax.barh(dept_means.index, dept_means.values, color=colors)
ax.axvline(4.0, ls="--", color="#999", lw=1)
ax.set_xlim(3.0, 4.3)
ax.set_xlabel("Mean total engagement score (1–5 Likert)")
ax.set_title("Illustrative Engagement by Department — Latest Wave (2024 Q4)\n"
             "Red bars fall below 3.5 and would trigger item-level review",
             fontsize=12, fontweight="bold")
for i, v in enumerate(dept_means.values):
    ax.text(v + 0.01, i, f"{v:.2f}", va="center", fontsize=8.5)
ax.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/department-comparison-1.png", dpi=150, bbox_inches="tight")
plt.close()

# ------------------------------------------------------------------------------
# FIGURE 4: Reliability QA — Cronbach's alpha per subscale per wave.
# Demonstrates the planned data-quality gate: every administration is checked
# against the alpha >= .70 acceptability threshold before results are trusted.
# ------------------------------------------------------------------------------
alpha_rows = []
for q in QUARTERS:
    wave = panel[panel["quarter"] == q]
    for sub, items in SUBSCALES.items():
        alpha_rows.append({"quarter": q, "subscale": sub,
                           "alpha": cronbach_alpha(wave[items])})
alpha_df = pd.DataFrame(alpha_rows)
fig, ax = plt.subplots(figsize=(8, 4.8))
for sub in SUBSCALES:
    s = alpha_df[alpha_df["subscale"] == sub]
    ax.plot(s["quarter"], s["alpha"], marker="s", lw=2,
            color=PALETTE[sub], label=sub)
ax.axhline(0.70, ls="--", color="#d73027", lw=1.2)
ax.text(0.02, 0.705, "Acceptability threshold (.70)",
        transform=ax.get_yaxis_transform(), fontsize=8, color="#d73027")
ax.set_ylim(0.55, 0.95)
ax.set_ylabel("Cronbach's α (internal consistency)")
ax.set_xlabel("Survey wave (quarterly)")
ax.set_title("Illustrative Reliability Check by Subscale and Wave\n"
             "(synthetic demonstration data)", fontsize=12, fontweight="bold")
ax.legend(title="Subscale", frameon=False)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/reliability-check-1.png", dpi=150, bbox_inches="tight")
plt.close()

# ------------------------------------------------------------------------------
# FIGURE 5: Item-level mean profile (latest wave).
# Demonstrates the deepest reporting layer: when a subscale is low, which
# specific items drive it and would inform targeted intervention design.
# ------------------------------------------------------------------------------
all_items = sum(SUBSCALES.values(), [])
item_means = latest[all_items].mean()
item_colors = []
for it in all_items:
    for sub, items in SUBSCALES.items():
        if it in items:
            item_colors.append(PALETTE[sub])
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.bar(all_items, item_means.values, color=item_colors)
ax.set_ylim(3.0, 4.3)
ax.set_ylabel("Mean item score (1–5 Likert)")
ax.set_xlabel("Survey item (Vigor V1–V5, Dedication D1–D5, Absorption A1–A5)")
ax.set_title("Illustrative Item-Level Profile — Latest Wave (2024 Q4)\n"
             "(synthetic demonstration data)", fontsize=12, fontweight="bold")
handles = [plt.Rectangle((0, 0), 1, 1, color=PALETTE[s]) for s in SUBSCALES]
ax.legend(handles, list(SUBSCALES.keys()), title="Subscale", frameon=False)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/item-profile-1.png", dpi=150, bbox_inches="tight")
plt.close()

print("Figures written to", OUT)
print(alpha_df.pivot(index="quarter", columns="subscale", values="alpha").round(3))
print("\nLatest-wave department totals:\n", dept_means.round(2))
