# ANOVA Methods Collection: One-Way, Factorial, Repeated Measures, and Mixed Design

**Mintay Misgano, PhD**
*Statistical Methods and Research Design*

---

## Abstract

Analysis of Variance (ANOVA) is among the most frequently applied statistical frameworks in behavioral research, yet the family of ANOVA designs is often treated as a single technique rather than a set of related tools, each suited to a different data structure. This project demonstrates four ANOVA designs applied to four simulated social science datasets: a one-way between-subjects ANOVA, a 2×3 factorial ANOVA, a one-way repeated measures ANOVA, and a 3×3 mixed design ANOVA. Across designs, results illustrate the core statistical logic while highlighting the practical implications of each design choice: controlling for individual differences, testing interaction effects, and managing Type I error across multiple comparisons.

---

## Introduction

The choice of ANOVA design is not merely a technical decision — it reflects the structure of the research question and the data collection strategy. Four structural considerations govern the choice:

**Number of independent variables.** A one-way ANOVA tests one factor; factorial designs test two or more, including their interaction. Interaction effects are often the most theoretically important finding: they indicate that the effect of one variable depends on the level of another.

**Between vs. within subjects.** Between-subjects designs compare independent groups; within-subjects (repeated measures) designs compare the same individuals across conditions or time points. Repeated measures designs are more powerful — they remove person-level variance from the error term — but they require additional assumptions (sphericity) and a different data structure (long format with participant IDs).

**Mixed designs** combine both: one or more between-subjects factors and one or more within-subjects factors in the same model. They are the standard design in longitudinal intervention research, where participants are randomly assigned to conditions and then measured at multiple time points.

**Effect size and Type I error.** Omnibus ANOVA results establish whether group differences exist; post hoc tests and follow-up comparisons reveal where. Each additional comparison increases the familywise Type I error rate, which requires systematic correction (Bonferroni, Holm, or Tukey HSD depending on context).

The four analyses in this project each instantiate one of these structural configurations, using simulated datasets drawn from published research in cross-cultural communication, pedestrian safety, resilience intervention, and prejudice reduction.

---

## Method

### Design Overview

**Study 1 — One-Way Between-Subjects ANOVA**
*Data:* Simulated from Tran and Lee (2014). N = 90 participants (n = 30 per condition).
*DV:* `moreTalk` — willingness to engage in additional cross-cultural communication (continuous, standardized).
*IV:* Training condition — Control, Low-intensity, High-intensity.
*Design:* One-way, between-subjects; three independent groups.

**Study 2 — Two-Way Factorial ANOVA (2×3)**
*Data:* Simulated from Coughenour et al. (2017). N = 180 crossings (n = 30 per cell).
*DV:* `NotStop` — number of cars that did not yield to the pedestrian at a midblock crosswalk.
*IVs:* Race of pedestrian (Black, White) × Neighborhood income (Low, Middle, High).
*Design:* 2×3 between-subjects factorial; tests main effects and interaction.

**Study 3 — One-Way Repeated Measures ANOVA**
*Data:* Simulated from Amodio et al. (2018). N = 50 participants × 3 waves = 150 observations.
*DV:* `Resilience` — psychological resilience score.
*IV:* Wave — Pre, Post, 6-month Follow-Up (within-subjects).
*Design:* One-way repeated measures; same participants measured three times.

**Study 4 — Mixed Design ANOVA (3×3)**
*Data:* Simulated from Brenick (2019). N = 300 participants × 3 waves = 900 observations.
*DV:* `GBE` — group-based exclusion attitudes.
*Between-subjects factor:* Training condition — Control, Skills, Skills+Contact.
*Within-subjects factor:* Wave — Pre, Post, 6-month Follow-Up.
*Design:* 3×3 mixed; combines between- and within-subjects factors.

### Statistical Assumptions

Each design was evaluated for its relevant assumptions prior to omnibus testing. For between-subjects components: normality (Shapiro-Wilk tests at each level; visual inspection of boxplots) and homogeneity of variance (Levene's test). For within-subjects components: sphericity (Mauchly's test; Greenhouse-Geisser correction applied when violated). For mixed designs: Box's M test for homogeneity of covariance matrices was also examined. All analyses were conducted in R using the `rstatix`, `car`, and `lsr` packages.

Type I error was managed using Tukey HSD for the one-way design, Holm sequential correction for pairwise comparisons, and Bonferroni correction for simple main effect omnibus tests in the mixed design. Effect sizes are reported as η² throughout (Cohen, 1988: small ≈ .01, medium ≈ .06, large ≥ .14).

---

## Results

### Study 1: One-Way ANOVA — Communication Training Effects

Assumption checks supported normality within each condition and homogeneity of variance across groups (Levene's test non-significant). The omnibus one-way ANOVA tested whether mean `moreTalk` differed significantly across the three training conditions. Descriptive statistics showed that the Control condition had the highest mean willingness to talk more, followed by Low-intensity and High-intensity training — a counterintuitive pattern worth flagging for substantive interpretation. Tukey HSD post hoc comparisons corrected the familywise error rate across the three pairwise contrasts, identifying which specific condition pairs drove the omnibus effect.

*Practical takeaway:* One-way ANOVA is appropriate whenever the research question involves comparing independent groups on a continuous outcome, and the investigator has no a priori reason to assume one-directional contrasts.

### Study 2: Two-Way Factorial ANOVA — Race and Neighborhood Income on Driver Yielding

The 2×3 factorial ANOVA tested both main effects and the Race × Neighborhood Income interaction. Levene's test supported homogeneity of variance across the six cells. The interaction effect is the key finding: if significant, it means the racial disparity in driver yielding (the main effect of Race) is not uniform across neighborhood income levels — yielding to Black vs. White pedestrians differs more starkly in some income-level contexts than others. Simple main effects of Race within each NbhdInc level, followed by Holm-corrected pairwise comparisons for NbhdInc within each Race, unpack the interaction.

*Practical takeaway:* In factorial designs, always examine the interaction first. A significant interaction qualifies and contextualizes main effects — reporting main effects in isolation when an interaction is present is a common analytical error with real interpretive consequences.

### Study 3: One-Way Repeated Measures ANOVA — Resilience Over Time

Mauchly's test evaluated the sphericity assumption for the within-subjects factor (Wave). Greenhouse-Geisser corrected degrees of freedom are reported where sphericity was violated. The omnibus test evaluated whether resilience scores changed significantly from Pre to Post to Follow-Up. Because the same 50 participants contributed scores at all three waves, individual differences in baseline resilience are partitioned out of the error term — giving the design substantially more statistical power than an equivalent between-subjects design would have with the same sample size. Holm-corrected paired-sample pairwise comparisons identified which specific wave-to-wave transitions (Pre→Post, Pre→Follow-Up, Post→Follow-Up) were statistically significant.

*Practical takeaway:* Repeated measures designs are the appropriate choice whenever measurement occurs at multiple time points on the same individuals. The within-subjects structure controls for individual baseline differences and reduces the standard error, increasing power without requiring a larger sample.

### Study 4: Mixed Design ANOVA — Prejudice Reduction Intervention

The 3×3 mixed design ANOVA tested three effects simultaneously: the main effect of Condition (does intervention matter overall?), the main effect of Wave (does GBE change over time overall?), and the Condition × Wave interaction (does the pattern of change over time differ by intervention condition?). The interaction is the primary test of intervention efficacy: a significant interaction indicates that conditions diverged over time, which is the expected signature of an effective intervention.

Consistent with the source manuscript results, the omnibus ANOVA yielded significant main effects for both Condition and Wave as well as a significant interaction (η² values in the small-to-medium range). Simple main effects of Condition within each Wave showed that condition differences were non-significant at Pre-test (as expected, since random assignment should produce equivalent baseline scores) but emerged at Post and grew by Follow-Up. Holm-corrected pairwise comparisons identified Skills+Contact as the condition most differentiated from Control by follow-up — suggesting that experiential contact paired with skills training produces more durable attitude change than skills training alone.

*Practical takeaway:* Mixed design ANOVA is the standard framework for pre-post intervention research with multiple groups.

---

## Comparative Design Logic

| Feature | One-Way | Factorial (2×3) | Repeated Measures | Mixed Design |
|---------|---------|----------------|-------------------|-------------|
| Independent variables | 1 | 2 | 1 (within) | 1 between + 1 within |
| Can test interactions | No | Yes | No | Yes |
| Controls individual differences | No | No | Yes | Partially (for within factor) |
| Sphericity assumption | No | No | Yes | Yes (for within factor) |
| Requires participant ID | No | No | Yes | Yes |
| Data format | Wide or long | Wide or long | Long (one row per obs) | Long |
| Post hoc approach | Tukey, Holm | Simple main effects | Paired pairwise | SME + pairwise |

---

## Discussion

### What Each Design Buys You

The one-way ANOVA is the entry point: simple, powerful, and widely understood. The factorial design adds explanatory depth by testing whether predictors interact — the most common and theoretically important class of research finding in applied behavioral science. Repeated measures ANOVA increases power by controlling for individual baseline differences, enabling smaller samples to detect meaningful effects. The mixed design integrates all of these advantages into a single model suited for longitudinal intervention research.

### Comparative Value of the Collection

The core analytical discipline is the same in every case: examine assumptions, test the omnibus effect, follow significant effects with appropriate post hoc tests, manage Type I error explicitly, and report effect sizes alongside p-values so that readers can assess practical significance rather than just statistical significance.

### Limitations

All four datasets are simulated from published population parameters. While this ensures known, reproducible results, it means that distributional characteristics are smoother than would be typical in observational data. In live applications, data cleaning, handling of skewed distributions, and decisions about whether to apply robust ANOVA alternatives (Welch's, permutation tests) become more consequential.

---

## References

Amodio, A., Collins, E., & Moss, M. (2018). Empowering youth with disability: A study of resilience and mindfulness. *Journal of Applied Developmental Psychology*.

Brenick, A. (2019). Teaching tolerance through empathy and contact. *Journal of Social Issues*.

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum.

Coughenour, C., Clark, S., Singh, A., Claw, E., Abelar, J., & Huebner, J. (2017). Examining racial bias as a potential factor in pedestrian crashes. *Accident Analysis & Prevention, 98*, 96–100.

Kline, R. B. (2016). *Principles and practice of structural equation modeling* (4th ed.). Guilford Press.

Tran, A. G. T. T., & Lee, R. M. (2014). You speak English well! Asian Americans' reactions to an [(in)validation] of linguistic identity. *Journal of Counseling Psychology, 61*(3), 451–461.

---

*All datasets are simulated from published population parameters. R packages: rstatix, ggpubr, psych, car, lsr.*
