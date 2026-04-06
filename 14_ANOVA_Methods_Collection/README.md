# Project 14: ANOVA Methods Collection
**Mintay Misgano | People Analytics Portfolio**

---

## What I Did

Demonstrated four ANOVA designs — one-way between-subjects, two-way factorial, one-way repeated measures, and mixed design — each applied to a different simulated research dataset. The goal: show that ANOVA is a family of tools, not a single technique, and that design choice drives both statistical power and interpretive scope.

---

## The Four Designs

| Design | Dataset | Key Question | Finding |
|--------|---------|-------------|---------|
| **One-Way ANOVA** | mTalk (N = 90) | Do communication training conditions differ in willingness to talk more? | Significant group differences; Tukey post hoc identifies which pairs diverge |
| **Factorial 2×3** | Curbside (N = 180) | Does racial bias in driver yielding vary by neighborhood income? | Significant Race × NbhdInc interaction — the racial disparity is context-dependent |
| **Repeated Measures** | Resilience (N = 50 × 3 waves) | Does resilience change Pre→Post→Follow-Up? | Within-subjects design removes individual baseline noise; detects wave-level change |
| **Mixed Design 3×3** | GBE prejudice (N = 300 × 3 waves) | Does an intervention reduce group-based exclusion attitudes differentially over time? | Significant Condition × Wave interaction; Skills+Contact condition shows greatest reduction by follow-up |

---

## Why It Matters

The mixed design result is the most directly applicable to People Analytics: it's the standard framework for evaluating whether an organizational intervention (onboarding, training, DEI program) produces differential improvement across groups over time. The factorial result illustrates a principle just as important: **always check the interaction before reporting main effects**. Ignoring a significant interaction while reporting only main effects is one of the most common analytical errors in applied research.

---

## Files

| File | Description |
|------|-------------|
| `01a_mTalk.csv` | One-way ANOVA dataset (N = 90, communication training) |
| `01b_Curb2X3.csv` | Factorial 2×3 dataset (N = 180, driver yielding at crosswalks) |
| `01c_Amodio.csv` | Repeated measures dataset (N = 50 × 3 waves, resilience) |
| `01d_GBE.csv` | Mixed design dataset (N = 300 × 3 waves, prejudice reduction) |
| `02_ANOVA_Analysis_R.md` | Full R analysis — all four designs with assumption checks, omnibus tests, post hoc comparisons, and figures |
| `03_Project_Report.md` | Full APA-style report with comparative design logic and discussion |

---

*Data simulated from Tran & Lee (2014), Coughenour et al. (2017), Amodio et al. (2018), Brenick (2019) · R (rstatix, ggpubr, car, lsr)*
