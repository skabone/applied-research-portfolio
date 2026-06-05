# Who Survives Longer After an Advanced Lung Cancer Diagnosis?

Using records from 228 advanced lung cancer patients, this project asks a simple question — who lives longer, and which factors matter most — and answers it with the right statistical tools for survival data.

The challenge is that, by the end of the study, 63 of the 228 patients (28%) were still alive, so their full survival time was never observed. Plain averages would undercount survival by treating those patients as if they had died. The analysis uses methods built for this situation, where the *timing* of an event matters and some outcomes are still open.

**What the data show:**

![Survival by sex](docs/figures/km-by-sex-1.png)

- **Women survived substantially longer than men** — a typical (median) survival of 426 days versus 270 days, about five months more. The difference is statistically reliable, not chance (p = 0.001).
- **A patient's performance status — how functionally active they are — was the single strongest predictor of risk.** Each step toward being less active raised the risk of death by about 67%, and typical survival fell steadily from roughly 303 days for the most active patients to 118 days for the least active.
- **Age and weight loss did not independently predict survival** once performance status and sex were accounted for.
- The risk model correctly ranked which of two patients would die sooner about 65% of the time — useful discrimination from a small set of clinical factors.

**What it means:** performance status and sex, rather than age, should anchor how prognosis is discussed for patients like these — and for outcomes with this much incomplete follow-up, survival should always be reported with time-to-event methods rather than simple death rates.

For the full methodology — Kaplan-Meier estimation, log-rank testing, ANOVA, and a multivariable Cox proportional-hazards model with assumption checks and citations — see the [Project Report](./02_Project_Report.md). The reproducible R source is in [04_Source_Report.Rmd](./04_Source_Report.Rmd).
