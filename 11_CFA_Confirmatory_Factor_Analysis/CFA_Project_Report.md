# Confirmatory Factor Analysis of the Gendered Racial Microaggressions Scale for Asian American Women (GRMSAAW): Evaluation of Unidimensional and First-Order Correlated-Factors Models

**Mintay Misgano, PhD**
*Psychometrics and Measurement*
April 2026

---

## Abstract

This study applied confirmatory factor analysis (CFA) to evaluate competing measurement models of the Gendered Racial Microaggressions Scale for Asian American Women (GRMSAAW; Keum et al., 2018). Using data simulated from published factor loadings and item descriptives (N = 304), I compared a unidimensional model (all 22 items loading on a single general factor) to a first-order correlated-factors model (22 items loading on four subscales permitted to covary). Using the R package *lavaan* — with results independently replicated in Python via *semopy* — the four-factor model demonstrated markedly superior fit: χ²(203) = 220.86, *p* = .186; CFI = .991; RMSEA = .017, 90% CI [.000, .031]; SRMR = .058. The chi-square difference test (Δχ²[6] = 783.28, *p* < .001) and lower information criteria (AIC and BIC) for the four-factor model confirmed it as the preferred representation. Findings support the GRMSAAW's four-dimensional structure and provide a replicable CFA template for applied survey validation work.

---

## 1. Introduction

### 1.1 Background and Motivation

The validation of psychological and organizational surveys has direct consequences for the quality of decisions made from their data. When a survey instrument is treated as measuring a single construct but actually captures multiple distinct dimensions — or vice versa — the resulting scores misrepresent the construct space, and any decisions based on those scores may be systematically in error.

Confirmatory factor analysis (CFA) is the primary statistical technique for evaluating whether a proposed measurement structure fits observed data. Unlike exploratory factor analysis (EFA), which identifies structure empirically from data without imposing a priori constraints, CFA requires the researcher to specify the number of factors and which items belong to which factor before analysis. This restriction reflects theoretical commitment and enables rigorous hypothesis testing.

The instrument examined here is the Gendered Racial Microaggressions Scale for Asian American Women (GRMSAAW; Keum et al., 2018), a 22-item frequency-based measure assessing the frequency with which Asian American women encounter specific forms of gendered racial microaggressions. The scale was developed with a four-factor structure based on the theoretical framework of Keum and colleagues and validated in their original two-study publication.

### 1.2 Research Questions

1. Does the GRMSAAW function adequately as a unidimensional instrument — that is, does a single-factor model achieve acceptable fit?
2. Does a first-order, correlated four-factor model provide substantially better fit than the unidimensional model?
3. Are the four subscales of the GRMSAAW — Ascribed Submissiveness, Asian Fetishism, Media Invalidation, and Assumptions of Universal Appearance — empirically distinguishable as distinct latent variables?

---

## 2. Method

### 2.1 Instrument

The GRMSAAW (Keum et al., 2018) is a 22-item scale assessing the frequency of gendered racial microaggression experiences among Asian American women. Items are rated on a 0–5 frequency scale (0 = *never*, 5 = *always*). None of the items are negatively worded, so reverse-scoring was not required. The four subscales and their items are:

| Subscale | Code | N Items | Example Item |
|---|---|:---:|---|
| Ascribed Submissiveness | AS | 9 | "Others have been surprised when I disagree with them." |
| Asian Fetishism | AF | 4 | "Others have treated me as if I am always open to sexual advances." |
| Media Invalidation | MI | 5 | "I rarely see AAW playing the lead role in the media." |
| Assumptions of Universal Appearance | AUA | 4 | "Others have suggested that all AAW look alike." |

### 2.2 Data

Data were simulated from the published factor loading matrix (Keum et al., 2018, Table 2) and item-level descriptive statistics (Table 4) using the `MASS::mvrnorm()` function in R with `empirical = TRUE` to reproduce population-level moments exactly (N = 304, seed = 210927). The simulation procedure followed the approach described by the original authors' OER textbook chapter (Bikos, 2021). The resulting dataset preserves the theoretical covariance structure specified by the published loadings while generating item-level data appropriate for CFA.

### 2.3 Analytic Strategy

**Software.** CFA was conducted in R (version 4.x) using the *lavaan* package (v.0.6-9; Rosseel, 2012). Results were independently replicated in Python 3 using *semopy* (v.2.3; Meshcheryakov et al., 2021). χ² statistics were identical across platforms, confirming implementation accuracy.

**Model specification.** Two models were specified and evaluated:

- *Model 1 (Unidimensional):* All 22 GRMSAAW items were specified to load on a single latent variable. This model served as a baseline and tests whether a single-factor explanation is defensible.
- *Model 2 (First-Order Correlated Factors):* Items were specified to load exclusively on their theoretically designated subscale. The four latent factors (AS, AF, MI, AUA) were permitted to freely correlate, consistent with an oblique first-order model. The `lavaan::cfa()` function implements this by default.

**Model identification.** Both models were overidentified (*df* > 0), satisfying the necessary condition for unique parameter estimates. The four-factor model's shortest subscale (AF and AUA, 4 items each) exceeded the minimum requirement of two indicators per factor for multi-factor CFA models.

**Estimation.** Maximum likelihood (ML) estimation was used throughout, consistent with the scale developers' methodology.

**Fit evaluation.** The following fit indices were used:

| Index | Type | Acceptable Range |
|---|---|---|
| χ² (Model Test) | Exact-fit | *p* > .05 preferred; sensitive to N |
| CFI | Incremental (goodness) | ≥ .95 |
| TLI | Incremental (goodness) | ≥ .95 |
| RMSEA | Absolute (badness) | ≤ .05 good; .05–.08 reasonable; ≥ .10 problematic |
| SRMR | Absolute (badness) | < .10 acceptable |
| AIC / BIC | Information criteria | Lower = better (relative, not absolute) |

**Model comparison.** Nested model comparison used the chi-square difference test (χ²Δ), where a statistically significant result (*p* < .05) indicates the more complex model provides significantly better fit. AIC and BIC were compared directly, with lower values indicating the preferred model.

---

## 3. Results

### 3.1 Descriptive Statistics

Item means ranged from 2.81 (AS4) to 4.61 (MI5). Standard deviations ranged from 0.63 (MI5) to 1.47 (AS4). Items in the MI and AUA subscales exhibited higher means (ceiling effects) and greater negative skew, consistent with the interpretation that media-based and appearance-based microaggressions are frequently encountered by this population. Items in the AS subscale showed the greatest variability.

The inter-item correlation matrix revealed a block structure consistent with the four-factor hypothesis: items within each subscale correlated more strongly with each other than with items on other subscales. This pattern was most pronounced for the AS and AF subscales, and somewhat less defined for MI and AUA items.

### 3.2 Model 1: Unidimensional CFA

The unidimensional model specified all 22 items as indicators of a single general GRMSAAW factor. The model converged normally (28 iterations, ML estimation).

**Fit statistics:** χ²(209) = 1004.14, *p* < .001; CFI = .578; TLI = .534; RMSEA = .112, 90% CI [.105, .119]; SRMR = .124; AIC = 17,755.03; BIC = 17,918.58.

All indices indicated poor fit. The statistically significant χ² indicates the model's covariance structure departs substantially from the observed data. CFI = .578 falls far below the .95 benchmark, indicating the unidimensional model explains only 58% more variance than a null (independence) model. RMSEA = .112 exceeds the .10 danger threshold. SRMR = .124 exceeds the .10 warning cutoff. Standardized loadings for items outside the AS subscale were low, variable, and in several cases non-significant or negative, indicating that a general factor does not adequately account for covariance across all 22 items.

### 3.3 Model 2: First-Order Correlated-Factors CFA

The four-factor correlated model specified AS items (AS1–AS9), AF items (AF1–AF4), MI items (MI1–MI5), and AUA items (AUA1–AUA4) as loading exclusively on their respective factors, with all four factors permitted to correlate.

**Fit statistics:** χ²(203) = 220.86, *p* = .186; CFI = .991; TLI = .989; RMSEA = .017, 90% CI [.000, .031]; SRMR = .058; AIC = 16,983.75; BIC = 17,169.60.

All indices indicated excellent fit. The non-significant χ²(*p* = .186) indicates the model's predicted covariance matrix is not statistically distinguishable from the observed one. CFI = .991 exceeds the .95 threshold; TLI = .989 confirms this finding accounting for model complexity. RMSEA = .017 — with an upper CI bound of .031 — indicates close fit. SRMR = .058 falls well below the .10 warning threshold.

**Standardized factor loadings** were strong and statistically significant across all subscales:

- *AS subscale:* Standardized loadings ranged from .64 to .82, all *p* < .001
- *AF subscale:* Standardized loadings ranged from .59 to .80, all *p* < .001
- *MI subscale:* Standardized loadings ranged from .35 (MI5) to .60, all *p* < .001; MI5's loading, while the smallest, remained statistically significant
- *AUA subscale:* Standardized loadings ranged from .59 to .82, all *p* < .001

**Factor correlations:** Intercorrelations among the four latent factors were small in magnitude (all *r* < .10), indicating that while the constructs share some variance, they are empirically distinguishable.

### 3.4 Model Comparison

**Table 1. Model Fit Comparison**

| Index | Model 1 (Unidimensional) | Model 2 (4-Factor) | Criterion |
|---|:---:|:---:|---|
| χ²(df) | 1004.14 (209)*** | 220.86 (203) | *p* > .05 |
| CFI | .578 | **.991** | ≥ .95 |
| TLI | .534 | **.989** | ≥ .95 |
| RMSEA [90% CI] | .112 [.105, .119] | **.017 [.000, .031]** | ≤ .05 |
| SRMR | .124 | **.058** | < .10 |
| AIC | 17,755.03 | **16,983.75** | Lower = better |
| BIC | 17,918.58 | **17,169.60** | Lower = better |

*Note.* *** *p* < .001. Bold values indicate the preferred model on each index.

**Chi-square difference test:** Δχ²(6) = 783.28, *p* < .001. This statistically significant result confirms that the four-factor model fits the data significantly better than the unidimensional model. AIC was 771.28 points lower for the four-factor model; BIC was 748.98 points lower — both confirming preference for the four-factor solution.

---

## 4. Discussion

### 4.1 Primary Finding

The results strongly and consistently support the four-factor correlated structure of the GRMSAAW. The unidimensional model was comprehensively rejected on all five fit criteria. The four-factor model met or exceeded established thresholds on all indices. The formal chi-square difference test and information criteria unanimously preferred the four-factor solution.

These findings replicate and extend the original validation work of Keum et al. (2018), providing independent confirmation — using simulation from their published parameters — that the four-subscale structure is stable and supported.

### 4.2 Practical Implications for Scale Use

The psychometric evidence has direct operational implications. Because the four factors are empirically distinguishable (small but non-zero intercorrelations, clean loading structure), users of the GRMSAAW should:

1. Report subscale scores separately rather than a single composite score
2. Interpret subscale differences (e.g., high Media Invalidation but low Asian Fetishism) as meaningful, not noise
3. Treat the total score as an approximate index rather than a primary outcome

For applied survey work more broadly, the lesson is straightforward: validate the assumed factor structure in the population being studied before relying on scale scores for interpretation.

### 4.3 Limitations

Several limitations apply. First, the data are simulated rather than collected from a real sample. While the simulation preserves the population-level covariance structure from the published parameters, it does not capture sampling error or distributional idiosyncrasies that would emerge in real data collection. Findings should be considered a methodological demonstration rather than a clinical or organizational replication.

Second, the current analysis evaluated only unidimensional and first-order correlated-factors models. Higher-order models (second-order, bifactor) were not tested and could provide additional insight into the relationship between subscale-level and general-factor variance in the GRMSAAW. These models are addressed in the companion project (Project 10c: Measurement Invariance).

Third, model fit was evaluated using established benchmarks that, as Kline (2016) cautions, should not be treated as rigid cut-offs. Elements such as sample size, model complexity, and the distribution of the variables should be considered in holistic evaluation.

### 4.4 Conclusion

CFA confirmed that the GRMSAAW is best characterized as a four-dimensional, first-order measurement instrument with correlated factors. The evidence is unambiguous: a single general factor does not adequately represent the construct space captured by these 22 items. This project demonstrates a complete CFA validation workflow — from data simulation to competing model evaluation to APA write-up — implemented in both R and Python.

---

## 5. References

Bikos, L. H. (2021). *ReCentering Psych Stats: Psychometrics (OER)*. Chapter 10: CFA, First-Order Models. Seattle Pacific University. https://github.com/lhbikos/ReC_Psychometrics

Byrne, B. M. (2016). *Structural equation modeling with AMOS: Basic concepts, applications, and programming* (3rd ed.). Routledge.

Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. *Structural Equation Modeling, 6*(1), 1–55. https://doi.org/10.1080/10705519909540118

Keum, B. T., Brady, J. L., Sharma, R., Lu, Y., Kim, Y. H., & Thai, C. J. (2018). Gendered racial microaggressions scale for Asian American women: Development and initial validation. *Journal of Counseling Psychology, 65*(5), 571–585. https://doi.org/10.1037/cou0000289

Kline, R. B. (2016). *Principles and practice of structural equation modeling* (4th ed.). Guilford Press.

Meshcheryakov, G., Igolkina, A., & Bikmukhametov, T. (2021). semopy: A Python package for structural equation modeling. *Journal of Statistical Software*, 101(1). https://doi.org/10.18637/jss.v101.i01

Rosseel, Y. (2012). lavaan: An R package for structural equation modeling. *Journal of Statistical Software, 48*(2), 1–36. https://doi.org/10.18637/jss.v048.i02
