# Measurement Invariance Testing of the Ableist Microaggressions Scale Across Disability Severity Groups

**Mintay Misgano, PhD**
*Psychometrics and Measurement*

---

## Abstract

Meaningful cross-group comparisons in survey research depend on the assumption that respondents from different groups interpret and respond to items in the same way. This project tests whether the Ableist Microaggressions Scale (AMS; Conover et al., 2017), a 20-item, four-factor instrument, functions equivalently across individuals reporting mild versus severe disability-related experiences (N = 833). The invariance sequence was evaluated using multi-group confirmatory factor analysis in R and Python. Results support configural and weak invariance, but not strong invariance, indicating that item intercepts differ systematically between groups. Practically, this means observed subscale means cannot be treated as directly comparable without additional invariance work.

---

## Introduction

Psychological measurement tools are often developed and validated on a single population, then deployed across diverse groups with the implicit assumption that the instrument behaves equivalently. When that assumption is violated, observed group differences in scale scores may be artifacts of how the scale functions rather than reflections of true differences in the construct. Testing measurement invariance — systematically evaluating whether a scale's factor structure, loadings, and intercepts hold across groups — is a prerequisite for defensible cross-group comparison.

Microaggression research illustrates this challenge acutely. Microaggressions are subtle, often ambiguous slights or indignities experienced by members of marginalized groups. Whether and how individuals perceive, label, and report microaggressions may itself vary with the severity or chronicity of one's experience. Individuals who have lived with disability for longer or who experience more severe functional limitations may interpret ambiguous interactions differently than those with mild or recent onset disability experiences. If this is the case, a self-report microaggression scale that assumes equivalence across disability severity groups may produce misleading comparisons.

The Ableist Microaggressions Scale (AMS; Conover et al., 2017) was developed to measure microaggressions directed toward individuals with disabilities. The 20-item instrument assesses four domains: Helplessness (unsolicited assistance and overprotection), Minimization (dismissal of disability experiences), Denial of Personhood (dehumanizing and objectifying treatment), and Otherization (exclusion and othering). While the AMS has been validated and shows sound psychometric properties in its development sample, its cross-group measurement equivalence has not been formally tested across disability severity.

The present analysis addresses this gap. Using a simulated dataset that reproduces the population-level factor structure and sample characteristics reported by Conover et al. (2017), I test the AMS across mild (n = 548) and severe (n = 285) disability-severity groups using the Vandenberg and Lance (2000) hierarchical invariance framework. The goals are: (1) to determine the level of invariance supported by the data, (2) to identify which aspects of the scale function equivalently and which do not, and (3) to offer practical guidance for researchers using the AMS in cross-group designs.

---

## Method

### Instrument

The Ableist Microaggressions Scale (AMS; Conover et al., 2017) is a 20-item self-report measure of disability-related microaggressions. Respondents rate the frequency with which they experience each item on a 0–5 scale (0 = *never*, 5 = *very often*). Items load onto four correlated factors:

- **Helplessness** (5 items; Help1–Help5): experiences of unsolicited assistance, overprotection, and being treated as incapable
- **Minimization** (3 items; Min1–Min3): having one's disability-related experiences dismissed or denied
- **Denial of Personhood** (5 items; Pers1–Pers5): dehumanizing, objectifying, or infantilizing treatment
- **Otherization** (7 items; Oth1–Oth7): being singled out, excluded, or made to feel different

### Data

Data were simulated to reproduce the population-level factor structure documented in Conover et al. (2017), Table 2. The published factor loading matrix (20 × 4) was used to derive an implied correlation/covariance matrix via the factor model equation Σ = ΛΦΛ' + Θ, where Φ was set to the identity matrix (standardized factors) and Θ contained item-specific uniqueness terms (Θ_ii = 1 − h²_i). The MASS package function `mvrnorm()` with `empirical = TRUE` was then used to generate N = 833 observations whose sample covariance matrix exactly reproduces the population-implied matrix. Item responses were scaled to the 0–5 range, rounded to integers, and clamped at the boundaries. Random seed 211023 ensures full reproducibility.

**Group assignment.** Disability severity groups were formed by ranking participants on their mean AMS item score (AMSm), which approximates the method used in the source study. The bottom 548 participants (66%) were assigned to the Mild group and the remaining 285 (34%) to the Severe group.

### Sample Characteristics

The final analytic dataset includes 833 observations across 20 items and 1 grouping variable. Both groups completed all 20 items; there are no missing data by design.

| Group | n | % |
|-------|---|---|
| Mild  | 548 | 65.8% |
| Severe | 285 | 34.2% |

Item means ranged from approximately 1.40 to 2.60 across groups, consistent with moderate-frequency endorsement of ableist microaggressions.

### Analytic Strategy

Multi-group confirmatory factor analysis (MGCFA) was used to test measurement invariance following the hierarchical sequence described by Vandenberg and Lance (2000). Four increasingly constrained models were estimated:

1. **Configural model:** The same four-factor structure is specified in both groups, but all parameters (loadings, intercepts, residuals, factor variances, factor covariances) are freely estimated within each group. This tests whether the same pattern of loadings holds across groups.

2. **Weak (metric) invariance model:** Factor loadings are constrained to equality across groups; intercepts, residuals, and factor parameters remain free. Supported weak invariance means the latent constructs are measured on the same metric — items relate to their factors with equivalent strength regardless of group.

3. **Strong (scalar) invariance model:** Factor loadings and item intercepts are constrained to equality. Supported strong invariance means that at equal levels of the latent factor, respondents from both groups endorse items at the same average level — a prerequisite for valid latent mean comparison.

4. **Strict invariance model:** Factor loadings, intercepts, and residual variances are all constrained to equality. Supported strict invariance indicates that item reliabilities are also equivalent across groups.

Models were estimated using maximum likelihood (ML) in lavaan (Rosseel, 2012) in R. Sequential model comparison used the likelihood ratio Δχ² test and Cheung and Rensvold's (2002) ΔCFI criterion (|ΔCFI| ≥ .010 indicates meaningful fit degradation). Absolute fit was evaluated against conventional benchmarks: CFI ≥ .95 (excellent), ≥ .90 (acceptable); RMSEA ≤ .05 (excellent), ≤ .08 (acceptable); SRMR ≤ .08 (acceptable). Python (semopy; Igolkina & Meshcheryakov, 2020) was used for per-group configural CFA, loading comparison visualizations, and supplementary fit verification.

---

## Results

### Descriptive Statistics

Item means in the Mild group ranged from 1.41 (*Help4*) to 2.58 (*Oth1*), with standard deviations between 1.20 and 1.65. In the Severe group, means ranged from 1.62 (*Help4*) to 3.08 (*Oth1*), with standard deviations between 1.28 and 1.72. As expected by the group-formation procedure, Severe participants reported higher mean endorsement across virtually all items. Inter-item correlations within each factor subscale were moderate-to-strong (within-factor r range: .28–.72), consistent with internally coherent subscales.

### Model 1: Configural Invariance

The configural model fit the data adequately in both groups, confirming that the same four-factor structure applies across disability severity. Fit indices for the combined configural model are presented in Table 1. CFI and RMSEA values met acceptable thresholds in both groups, supporting the conclusion that the 4-factor AMS structure is replicable across mild and severe disability-severity respondents.

### Model 2: Weak (Metric) Invariance

Constraining factor loadings to equality across groups produced negligible fit degradation relative to the configural baseline. The Δχ² test was non-significant, and ΔCFI was well below the .010 threshold, indicating that the loading constraints did not substantially worsen fit. **Weak invariance is supported.**

This finding means that each AMS item relates to its underlying factor with the same strength regardless of disability severity. In practice, a one-unit increase in the Helplessness latent factor corresponds to the same expected change in Help1 (for example) in both the Mild and Severe groups. The scale operates on the same metric across groups.

### Model 3: Strong (Scalar) Invariance

Adding intercept constraints to the weak model produced substantial and statistically significant fit degradation. The Δχ² test was highly significant and ΔCFI substantially exceeded the .010 threshold. **Strong invariance is not supported.**

This finding means that item intercepts differ across groups: at equal levels of the latent factor (e.g., equal Helplessness scores), Mild and Severe respondents endorse items at systematically different average levels. Several items appear to have elevated intercepts in the Severe group — Severe respondents with the same latent Otherization score, for instance, endorse Oth1–Oth3 at higher raw levels than Mild respondents at the same latent score. This is consistent with the hypothesis that individuals with more severe disability experiences may have a lower threshold for perceiving and labeling interactions as microaggressions, or may more readily endorse explicit item wording, independent of their actual construct level.

### Model 4: Strict Invariance

Strict invariance was not evaluated following the failure of strong invariance. Testing residual equality constraints on top of a model with already non-equivalent intercepts would conflate two sources of misfit and yield uninterpretable results.

### Fit Index Summary

**Table 1.** Fit Indices for the Measurement Invariance Sequence — AMS (N = 833)

| Model | χ² | df | p | CFI | TLI | RMSEA | 90% CI | SRMR | ΔCFI | Decision |
|-------|----|----|---|-----|-----|-------|--------|------|------|---------|
| Configural | — | — | — | — | — | — | — | — | — | Supported |
| Weak | Δχ²(16) ≈ 11.07 | +16 | .805 | — | — | — | — | — | .002 | **Supported** |
| Strong | Δχ²(16) ≈ 292.23 | +16 | < .001 | — | — | — | — | — | .096 | **Not supported** |
| Strict | — | — | — | — | — | — | — | — | — | Not tested |

*Note.* See `02_Invariance_Analysis_R.md` for complete per-model fit indices from lavaan. Δχ² and ΔCFI values are from sequential model comparison using `lavTestLRT()`. ΔCFI threshold for meaningful degradation: |ΔCFI| ≥ .010 (Cheung & Rensvold, 2002).

---

## Discussion

### Summary of Findings

I tested measurement invariance of the AMS across disability severity groups using a simulated dataset that reproduces the population factor structure from Conover et al. (2017). Results supported configural invariance (the same four-factor structure holds in both groups) and weak invariance (factor loadings are equivalent), but not strong invariance (item intercepts differ).

The failure of strong invariance is practically significant. It means that the AMS subscale means cannot be directly compared across disability severity groups in their raw form. An observed difference in, say, mean Otherization between Mild and Severe participants reflects not only a real difference in experienced Otherization but also a difference in how each group endorses items at the same latent level. Treating raw subscale means as equivalent rulers across groups would overstate or misattribute group differences.

### Implications for Practice

**For researchers using the AMS:** Do not compare subscale mean scores across disability severity groups without first confirming invariance. If strong invariance holds in a new sample, latent mean comparison via SEM is appropriate. If it fails, as here, consider partial invariance models that constrain only the invariant intercepts and freely estimate the non-invariant ones. Items with large intercept differences are candidates for revision in future scale development.

**For applied survey researchers:** This analysis illustrates a pattern common in cross-group survey work. A well-validated instrument may still show systematic item-level endorsement differences across groups that are not attributable to genuine construct differences. Reporting group mean scores without invariance testing risks drawing misleading conclusions about where the real differences lie.

**For scale developers:** The fact that loadings are invariant but intercepts are not suggests that the four-factor structure is solid but that items carry group-specific baseline frequencies. Future revisions might consider items with more neutral or behavioral (rather than frequency-based) wording that reduces intercept sensitivity to group membership.

### Limitations

The dataset is simulated rather than collected. While the simulation faithfully reproduces the published factor structure, it does not capture sampling variability, correlated residuals that may be present in real data, or demographic characteristics beyond the binary disability severity grouping. Results should be interpreted as demonstrating the analytical workflow and expected pattern of findings rather than as confirmatory empirical conclusions about the AMS in a live sample.

### Technical Notes

All R analyses use lavaan 0.6+ with ML estimation. The Python replication (semopy 2.3+) fits the same model structure per group and confirms configural fit; semopy does not implement `group.equal` constraints natively, so the full invariance sequence (weak/strong/strict Δχ²) uses R as the primary tool. Both implementations read the same `01_dfAMSi.csv` dataset, ensuring exact cross-platform reproducibility.

---

## References

Cheung, G. W., & Rensvold, R. B. (2002). Evaluating goodness-of-fit indexes for testing measurement invariance. *Structural Equation Modeling: A Multidisciplinary Journal, 9*(2), 233–255. https://doi.org/10.1207/S15328007SEM0902_5

Conover, K. J., Riser, K., Hucks, D., McKelvey, S., Vansickle, M., & Carter, R. T. (2017). Development and initial validation of the Ableist Microaggressions Scale. *The Counseling Psychologist, 45*(4), 570–599. https://doi.org/10.1177/0011000017718426

Igolkina, A. A., & Meshcheryakov, G. (2020). semopy: A Python package for structural equation models. *Structural Equation Modeling: A Multidisciplinary Journal*. https://doi.org/10.1080/10705511.2021.1972574

Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting: The state of the art and future directions for psychological research. *Developmental Review, 41*, 71–90. https://doi.org/10.1016/j.dr.2016.06.004

Rosseel, Y. (2012). lavaan: An R package for structural equation modeling. *Journal of Statistical Software, 48*(2), 1–36. https://doi.org/10.18637/jss.v048.i02

Vandenberg, R. J., & Lance, C. E. (2000). A review and synthesis of the measurement invariance literature: Suggestions, practices, and recommendations for organizational research. *Organizational Research Methods, 3*(1), 4–70. https://doi.org/10.1177/109442810031002

---

*Dataset simulated from published loadings (Conover et al., 2017, Table 2) using MASS::mvrnorm (empirical = TRUE), seed = 211023, N = 833. Analysis conducted in R (lavaan) and Python (semopy). All files available in this repository.*
