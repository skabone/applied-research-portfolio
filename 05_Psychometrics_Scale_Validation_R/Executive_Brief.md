# Psychometric Scale Validation — Executive Brief
**Scale:** Perceptions of the LGBTQ College Campus Climate Scale (Szymanski & Bissonette, 2020) | **Analyst:** Mintay Misgano | **Year:** 2023

---

## The Business Problem

Organizations and institutions need measurement instruments they can trust. In educational, HR, and clinical research contexts, surveys are only as useful as their psychometric foundations are sound. When a scale is poorly designed — items that don't cohere, factors that don't replicate, reliability that doesn't hold — the data it produces misleads rather than informs. This project demonstrates a complete psychometric validation workflow applied to the **Perceptions of the LGBTQ College Campus Climate Scale**, a 6-item, 7-point Likert instrument proposed to measure two distinct dimensions of LGBTQ students' campus experiences: institutional responsiveness (College Response subscale) and the visibility of bias (Stigma subscale).

---

## Approach

- Simulated item-level data (N = 646) directly from published factor loadings, item means, and standard deviations using `MASS::mvrnorm()` — ensuring full transparency and methodological reproducibility
- Applied a complete four-stage validation workflow: data preparation and reverse-scoring → reliability analysis (α, ω) → item analysis (corrected item-total correlations, cross-subscale discriminant validity) → exploratory factor analysis (suitability diagnostics, scree/parallel analysis, PCA and PAF with orthogonal and oblique rotations)
- Compared two EFA approaches (Principal Components Analysis vs. Principal Axis Factoring) and two rotation strategies (varimax and oblimin) to evaluate the robustness of the factor structure
- **Tools:** R, psych, tidyverse, sjstats, apaTables

---

## Key Findings

- **Total scale alpha is marginal (α = .64); subscale alphas are acceptable (α = .79 each)** — the drop in total-scale reliability when items are pooled across subscales signals that the instrument captures two distinct dimensions, not one.
- **Item analysis confirms within-scale convergent and discriminant validity** — all six items show corrected item-total correlations of .59–.69 with their own subscale and near-zero correlations (|*r*| ≤ .13) with the other subscale. No items are candidates for deletion.
- **EFA recovers a clean two-factor solution** — both PCA and PAF produce factor structures that map directly onto the a priori College Response and Stigma subscales. Factor loadings range from .60 to .91 on the target factor and are negligible (<.20) on the non-target factor.
- **The two factors are largely orthogonal** — the between-factor correlation in oblique rotations is near zero, indicating that college responsiveness and campus stigma are empirically distinct constructs, not two facets of a single experience.
- **Parallel analysis confirms two-factor retention** — observed eigenvalues exceed simulated random eigenvalues for exactly two factors, consistent with the a priori structure.

---

## Recommendations

1. **Use subscale scores, not a total scale score.** The psychometric evidence does not support collapsing all six items into a single composite. Total scores would pool heterogeneous variance and reduce interpretive precision.
2. **Replicate this workflow with independent samples.** The current analysis uses data simulated from published parameters — confirmatory factor analysis (CFA) on new empirical data is the recommended next step to formally test the two-factor model.
3. **Apply this validation framework to organizational survey instruments.** The same workflow — reliability assessment, item analysis, EFA — applies directly to engagement surveys, exit surveys, and climate assessments used in people analytics contexts. Instruments that skip this step produce structurally ambiguous scores that are difficult to interpret and act on.

---

## Impact

A validated measurement instrument produces data that can be trusted. This project demonstrates the technical rigor required before a scale enters operational use — ensuring that subscale scores reflect meaningful, reliable, and structurally distinct constructs. Applied to organizational people analytics, this framework enables HR and I-O professionals to evaluate the measurement quality of any multi-item survey instrument before drawing workforce conclusions from it.

---

*Analysis by Mintay Misgano | Tools: R (psych, tidyverse, sjstats, apaTables) | Data: N = 646 simulated observations, LGBTQ Campus Climate Scale (Szymanski & Bissonette, 2020)*
