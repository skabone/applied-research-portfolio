# When the Average Hides the Answer: Four ANOVA Designs

A single comparison-of-means test can give the wrong answer when the research design does not match the data. The same group difference can be statistically invisible to one model and dominant in another; an effect that looks flat on average can reverse direction inside subgroups. This project works four social-science questions, each with the analysis-of-variance (ANOVA) design its data structure actually requires — one-way, factorial, repeated-measures, and mixed — and shows how the design choice, not just the p-value, determines what can be concluded.

The clearest case is driver yielding at crosswalks. A test for an overall difference between yielding to Black versus White pedestrians finds *nothing* (main effect of race: *F*(1, 174) = 0.01, *p* = .91). The bias is real but conditional:

![Cars failing to yield by pedestrian race across neighborhood income; lines cross, showing the racial gap reverses direction by income level](docs/figures/factorial-lineplot-1.png)

In low-income blocks, more drivers fail to yield to the Black pedestrian (mean 0.56 vs. 0.24 cars not stopping); in high-income blocks the gap reverses and disadvantages the White pedestrian (1.13 vs. 0.75). The crossing lines are a significant Race × Income interaction (*F*(2, 174) = 68.06, *p* < .001, η² = .21) that an averaged, one-factor test erases entirely. Design choice is the finding.

## What's here

- **[01_Project_Summary.md](./01_Project_Summary.md)** — a short, plain-language tour of all four results and what each design buys you. Start here.
- **[02_Project_Report.md](./02_Project_Report.md)** — the full technical write-up: each design defined, metric definitions, assumption checks, and a figure-by-figure walk through every result with exact values, citations, and references.
- **[03_Analysis_Workflow.md](./03_Analysis_Workflow.md)** — the rendered R workflow (code, tables, and figures inline), generated from **[04_Source_Analysis.Rmd](./04_Source_Analysis.Rmd)**.

## The four questions

| Design | Question | Headline result |
|---|---|---|
| One-way between-subjects | Does communication-training intensity change willingness to talk across cultures? | Yes, but downward: high-intensity scored lowest (*F*(2, 87) = 9.89, *p* < .001, η² = .19) |
| Two-way factorial (2×3) | Does driver yielding to a pedestrian depend on race, income, or both? | Neither alone — only their interaction (*F*(2, 174) = 68.06, *p* < .001) |
| One-way repeated measures | Does a resilience program move scores, and do gains hold? | Rises Pre→Post and holds at follow-up (*F*(2, 98) = 17.63, *p* < .001) |
| Mixed (3×3) | Do exclusion attitudes diverge by training condition over time? | Groups equivalent at baseline, separate by follow-up (interaction *F*(4, 594) = 7.94, *p* < .001) |

## Data and reproducibility

The four datasets (`01a_mTalk.csv`, `01b_Curb2X3.csv`, `01c_Amodio.csv`, `01d_GBE.csv`) are simulated from population parameters reported in published studies in cross-cultural communication, pedestrian safety, resilience, and prejudice reduction. Simulation keeps the data fully shareable and the results exactly reproducible while preserving the design structure of each original study. The analysis runs in R (`rstatix`, `car`, `lsr`, `ggpubr`, `psych`); rerunning `04_Source_Analysis.Rmd` regenerates every table and figure.
