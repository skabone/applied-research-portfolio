# Psychometric Scale Validation: LGBTQ College Campus Climate Scale

**Analyst:** Mintay Misgano | **Year:** 2023 | **Tools:** R (psych, tidyverse, sjstats, apaTables) | **Dataset:** N = 646 simulated observations

---

## Abstract

This project demonstrates a complete psychometric scale validation workflow applied to the Perceptions of the LGBTQ College Campus Climate Scale (Szymanski & Bissonette, 2020), a six-item, seven-point Likert instrument designed to measure two dimensions of campus climate experienced by LGBTQ students. Item-level data were simulated from published factor loadings, item means, and sample size parameters to ensure full methodological transparency. The validation proceeded through four sequential stages: data preparation and scoring, internal consistency reliability analysis (Cronbach's alpha and McDonald's omega), item analysis (corrected item-total correlations and cross-subscale discriminant validity), and exploratory factor analysis (principal components analysis and principal axis factoring with orthogonal and oblique rotations). Results converge on a well-supported two-factor structure: a College Response subscale and a Stigma subscale. Subscale alphas were acceptable (α = .79 each), items showed strong within-scale convergent validity and near-zero cross-subscale correlations, and both PCA and PAF recovered the a priori two-factor solution with factor loadings ranging from .60 to .91. Implications for applied survey measurement in organizational and educational contexts are discussed.

---

## 1. Introduction

Measurement quality is foundational to any evidence-based decision-making process. In people analytics, HR research, and educational assessment, surveys and scales are the primary instruments through which latent constructs — engagement, climate, satisfaction, burnout — are quantified. Yet instruments are routinely deployed without rigorous psychometric evaluation, producing data whose structural validity, reliability, and interpretability remain unknown.

Psychometric scale validation is the systematic process of establishing that a measurement instrument does what it claims to do. It encompasses multiple evaluations that together answer a fundamental question: are the scores produced by this instrument reliable representations of the underlying construct? Validation is not a single test but a cumulative argument built from multiple independent lines of evidence.

This project applies a complete validation workflow to the Perceptions of the LGBTQ College Campus Climate Scale (Szymanski & Bissonette, 2020). The scale was developed to measure perceptions of how colleges and universities respond to LGBTQ students and the degree to which anti-LGBTQ stigma is visible on campus. It was selected as the demonstration instrument because it (1) has a theoretically motivated two-factor structure, (2) represents a socially important measurement domain, and (3) provides published psychometric parameters from which item-level data can be simulated reproducibly.

### 1.1 Research Questions

1. Does the LGBTQ Campus Climate Scale demonstrate acceptable reliability at the total scale and subscale levels?
2. Do individual items exhibit corrected item-total correlations consistent with their hypothesized subscale assignments?
3. Do items show stronger relationships with their own subscale than with the alternate subscale, supporting discriminant validity?
4. Does exploratory factor analysis recover the hypothesized two-factor solution using both PCA and PAF approaches?

---

## 2. Theoretical Framework

### 2.1 Classical Test Theory

The validation framework is grounded in Classical Test Theory (CTT), which models any observed score (X) as a function of a true score (T) and random measurement error (E): X = T + E. Reliability, in the CTT tradition, is the proportion of observed score variance attributable to true score variance rather than error. Perfect reliability would yield r_xx = 1.0; pure random error would yield r_xx = 0. In practice, reliability coefficients for applied social science scales typically fall between .70 and .95, with values below .70 considered marginal for research use.

### 2.2 Internal Consistency Reliability

Internal consistency reliability evaluates the degree to which items within a scale or subscale are measuring the same underlying construct. The two primary coefficients are:

**Cronbach's alpha (α):** The most widely reported internal consistency estimate, alpha is a function of the number of items and the average inter-item correlation. It assumes tau-equivalence — that all items contribute equally to the true score — an assumption that is rarely met in practice. Alpha is a lower-bound estimate of reliability and tends to increase artifactually with longer scales.

**McDonald's omega (ω):** A model-based reliability estimate that decomposes variance more precisely. Omega-total (ωt) represents the proportion of variance accounted for by all common factors; omega-hierarchical (ωh) reflects the proportion attributable to the general factor alone. When subscales are present, omega provides a more accurate picture of reliability at each level than alpha.

### 2.3 Item Analysis

Item analysis assesses the functioning of individual items within a scale. The corrected item-total correlation (r.drop) — the correlation between each item and the sum of all other items in its scale — is the primary diagnostic statistic. Items with r.drop values below approximately .30 are typically reviewed for potential revision or deletion, as they contribute little to the scale's internal coherence. Items with exceptionally high r.drop values may indicate undesirable redundancy.

Cross-subscale correlations extend item analysis to evaluate discriminant validity at the item level: if an item is truly tapping its intended subscale construct, it should correlate more strongly with that subscale (corrected for itself) than with any other subscale score. This pattern — high within-scale, low cross-scale — constitutes evidence for the scale's ability to measure distinct constructs.

### 2.4 Exploratory Factor Analysis

Exploratory factor analysis (EFA) identifies the latent dimensional structure underlying a set of observed variables without imposing a pre-specified structure. Two approaches are applied here:

**Principal Components Analysis (PCA):** Technically a data reduction technique rather than factor analysis. PCA extracts linear combinations (components) that maximize explained variance in the observed variables. It models all variance in the correlation matrix, including unique and error variance. PCA is appropriate as a preliminary exploration of structure but should not be treated as equivalent to latent factor modeling.

**Principal Axis Factoring (PAF):** A true factor analytic approach that models only the common variance shared among items, excluding item-specific and error variance. PAF identifies latent factors assumed to causally produce item responses — a theoretically appropriate model when the goal is to identify constructs underlying a survey instrument.

Both approaches are evaluated under orthogonal (varimax) rotation, which constrains factors to be uncorrelated, and oblique (oblimin) rotation, which permits factors to correlate. When two subscales are expected to be distinct but within the same broad domain, oblique rotation is generally preferred as it is a less restrictive assumption.

---

## 3. The Measurement Instrument

### 3.1 Scale Description

The Perceptions of the LGBTQ College Campus Climate Scale (Szymanski & Bissonette, 2020) is a six-item instrument measuring LGBTQ students' perceptions of their campus environment. Items are rated on a seven-point Likert scale ranging from 1 (*strongly disagree*) to 7 (*strongly agree*). Higher scores indicate more negative perceptions of the campus climate.

The scale's authors proposed and validated a two-subscale structure:

**College Response subscale (3 items):**
- "My university/college is cold and uncaring toward LGBTQ students." (*cold*)
- "My university/college is unresponsive to the needs of LGBTQ students." (*unresponsive*)
- "My university/college provides a supportive environment for LGBTQ students." (*supportive* — reverse-scored)

**Stigma subscale (3 items):**
- "Negative attitudes toward LGBTQ persons are openly expressed on my university/college campus." (*negative*)
- "Heterosexism, homophobia, biphobia, transphobia, and cissexism are visible on my university/college campus." (*heterosexism*)
- "LGBTQ students are harassed on my university/college campus." (*harassed*)

### 3.2 Data Source

Item-level data were simulated from Table 2 of Szymanski and Bissonette (2020) using the `MASS::mvrnorm()` function with `empirical = TRUE`. The simulation reproduced the published factor loading matrix (6 items × 2 factors), item means, and item standard deviations exactly, with N = 646 matching the original study sample size. The random seed was fixed at 210827 for full reproducibility. The simulation approach is methodologically transparent: all parameters are reported in the published article, and the resulting data structure directly reflects the scale's intended psychometric properties.

---

## 4. Data Preparation

### 4.1 Simulation and Bounding

Following simulation, responses were rounded to whole numbers (consistent with a discrete Likert format) and bounded at the 1–7 scale limits to prevent out-of-range values created by multivariate normal simulation. A participant ID variable was added and placed in the first column.

### 4.2 Reverse Scoring

The *supportive* item is directionally reversed relative to the other five items: agreement reflects a positive campus climate perception rather than a negative one. This item was reverse-scored (8 − raw score on a 1–7 scale) and renamed *unsupportive* to explicitly signal its rescaled direction. Reverse scoring was completed before any reliability, item analysis, or factor analysis calculations.

### 4.3 Scale Scoring

Scale scores were computed as mean scores rather than sums to facilitate interpretation and handle potential missing data. An available information approach (AIA; Parent, 2013) was applied using the `sjstats::mean_n()` function, allowing the total scale score to be computed if at least 80% of items were present (≥5 of 6). Subscale scores required all items to be present. Three scores were created: total scale score, College Response mean, and Stigma mean.

---

## 5. Reliability Analysis

### 5.1 Total Scale Reliability

The Cronbach's alpha for the full six-item scale was α = .64, with an average inter-item correlation of *r* = .23. This alpha falls below the commonly cited .70 threshold for adequate internal consistency. The relatively low average inter-item correlation — combined with the mix of items from two distinct constructs — suggests that treating the instrument as unidimensional produces a scale with limited internal coherence.

McDonald's omega-total (ωt) for the two-factor solution was consistent with the alpha estimate, while omega-hierarchical (ωh) — reflecting variance attributable to a single general factor — was considerably lower. This pattern reinforces the interpretation that the instrument's reliable variance is primarily organized into two subordinate factors rather than a single common dimension.

### 5.2 Subscale Reliability

Both subscales demonstrated substantially higher reliability than the total scale:

| Scale              | Items | α     | Avg inter-item *r* |
|:-------------------|:-----:|:-----:|:------------------:|
| Total              | 6     | .64   | .23                |
| College Response   | 3     | .79   | .56                |
| Stigma             | 3     | .79   | .56                |

The increase from total scale to subscale alphas — from .64 to .79 in both cases — is the diagnostic signature of a two-dimensional instrument. When items from two distinct constructs are pooled into a total score, the between-construct heterogeneity inflates the denominator of the alpha formula (total observed variance) without a proportional increase in the covariance term, suppressing alpha. Partitioning items into homogeneous subscales eliminates this suppression.

The average inter-item correlations for the subscales (.56 each) are more than double that of the total scale (.23), confirming that items within each subscale share substantially more variance with each other than with items from the other subscale.

---

## 6. Item Analysis

### 6.1 Corrected Item-Total Correlations

Corrected item-total correlations (r.drop) were computed separately for the total scale and each subscale. All six items showed r.drop values within the acceptable range for the total scale. For the subscales, corrected item-total correlations were uniformly strong:

**College Response subscale:**
- *cold*: r.drop = .69
- *unresponsive*: r.drop = .61
- *unsupportive*: r.drop = .59

**Stigma subscale:**
- *negative*: r.drop = .69
- *heterosexism*: r.drop = .63
- *harassed*: r.drop = .59

All six corrected item-total correlations exceed the commonly recommended threshold of .30, and the narrow range (.59–.69) indicates that no items are outliers in their contribution to subscale coherence. No items were identified for deletion or revision.

### 6.2 Cross-Subscale Discriminant Validity

Items from each subscale were correlated with the *other* subscale's mean score. For well-functioning items in a two-factor instrument, these cross-scale correlations should be substantially lower than the within-scale corrected item-total correlations.

| Item          | Within-scale *r.drop* | Cross-scale *r*  | Difference |
|:--------------|:---------------------:|:----------------:|:----------:|
| cold          | .69                   | −.02             | .71        |
| unresponsive  | .61                   | .09              | .52        |
| unsupportive  | .59                   | −.02             | .61        |
| negative      | .69                   | −.05             | .74        |
| heterosexism  | .63                   | −.01             | .64        |
| harassed      | .59                   | .13              | .46        |

The cross-scale correlations range from −.05 to .13 (|*r*| ≤ .13), compared to within-scale corrected item-total correlations of .59–.69. In every case, items correlate dramatically more strongly with their own subscale than with the alternate subscale. This pattern constitutes strong evidence for within-scale discriminant validity: the College Response and Stigma items are not merely two groups of items from a single undifferentiated construct — they reflect meaningfully distinct dimensions of campus climate experience.

---

## 7. Exploratory Factor Analysis

### 7.1 Suitability Diagnostics

Before proceeding with factor extraction, two standard diagnostic tests were conducted on the 6×6 inter-item correlation matrix:

**Bartlett's test of sphericity:** Tests the null hypothesis that the correlation matrix is an identity matrix (no shared variance among items). A significant result is required to justify factor analysis. The Bartlett test was significant (*p* < .001), indicating that the items share sufficient common variance.

**Kaiser-Meyer-Olkin (KMO) measure of sampling adequacy:** Assesses whether the partial correlations among items are small relative to the zero-order correlations — a necessary condition for well-defined factors. The overall KMO value exceeded .70, indicating meritorious sampling adequacy. Individual item KMO values were uniformly above .60.

Both diagnostics confirmed the suitability of the data for factor analysis.

### 7.2 Factor Retention Criteria

**Scree plot:** The scree plot showed a pronounced elbow after the second eigenvalue, with a sharp drop from eigenvalue 2 to eigenvalue 3. The first two eigenvalues exceeded 1.0 while subsequent eigenvalues fell well below this threshold, suggesting a two-factor solution.

**Parallel analysis:** Parallel analysis compared the observed eigenvalues against eigenvalues generated from 100 simulated random datasets of the same size. The observed eigenvalues exceeded the simulated random eigenvalues for exactly two factors, confirming the retention of two factors.

### 7.3 PCA Results

A two-component PCA solution was extracted and rotated using both varimax (orthogonal) and oblimin (oblique) methods. Results from both rotations were nearly identical, reflecting the near-zero between-factor correlation observed in the oblique solution.

Under oblique rotation, the pattern matrix showed clear simple structure: the three College Response items loaded strongly on Component 1 (loadings: .87–.90) with negligible cross-loadings on Component 2 (<.10), and the three Stigma items loaded strongly on Component 2 (loadings: .76–.88) with negligible cross-loadings on Component 1. The between-component correlation was approximately zero, suggesting the two dimensions are empirically orthogonal.

The two-component solution accounted for approximately 73% of total item variance, with Component 1 (College Response) explaining roughly 38% and Component 2 (Stigma) explaining roughly 35%.

### 7.4 PAF Results

Two-factor PAF was extracted and rotated using varimax and oblimin methods. The PAF solution closely replicated the PCA pattern matrix, with College Response items loading on Factor 1 and Stigma items loading on Factor 2. Factor loadings under oblique rotation:

| Item          | Factor 1 (College Response) | Factor 2 (Stigma) |
|:--------------|:---------------------------:|:-----------------:|
| cold          | .88                         | −.03              |
| unresponsive  | .73                         | .10               |
| unsupportive  | .73                         | −.04              |
| negative      | −.07                        | .86               |
| heterosexism  | −.02                        | .76               |
| harassed      | .16                         | .71               |

Factor loadings on the target factor range from .71 to .88 across all six items. Cross-loadings are negligible (≤|.16|), indicating clean simple structure with no items showing meaningful dual loadings. The between-factor correlation under oblique rotation was near zero (r ≈ .00), confirming that orthogonal and oblique solutions produce equivalent results — and that the two subscales are empirically independent despite co-occurring within the same instrument.

The two-factor PAF solution explained approximately 65% of common variance.

### 7.5 Comparison of PCA and PAF

Both PCA and PAF recovered the same factor structure, mapping directly onto the a priori College Response and Stigma subscales. The primary difference is interpretive: PCA describes the data reduction properties of the items, while PAF models the latent causal structure. For the purposes of construct validation, PAF is the theoretically preferred approach. The convergence of both methods strengthens confidence in the two-factor solution.

---

## 8. Integrated Discussion

### 8.1 Convergence of Evidence

The four analytic stages produced a consistent and mutually reinforcing picture of the scale's structure:

**Reliability analysis** established that the instrument is more internally consistent at the subscale level (α = .79) than at the total scale level (α = .64). This was the first indicator that a two-factor rather than a unidimensional model better characterizes the data.

**Item analysis** demonstrated that all six items show strong within-scale corrected item-total correlations (.59–.69) and near-zero cross-scale correlations (|*r*| ≤ .13). No items were flagged for revision or deletion. The dramatic difference between within-scale and cross-scale correlations provided item-level evidence for both convergent and discriminant validity.

**Exploratory factor analysis** confirmed the two-factor structure through multiple approaches. Both PCA and PAF produced equivalent solutions under orthogonal and oblique rotations, with strong simple structure and a near-zero between-factor correlation. Parallel analysis objectively confirmed the retention of exactly two factors.

The convergence of reliability, item-level, and factor-structural evidence from four independent analytic angles represents the kind of multi-method validation that supports confident scale use.

### 8.2 Practical Implications

**Do not use a total scale score.** The psychometric evidence does not support collapsing all six items into a single composite. Total score = College Response score + Stigma score would conflate two empirically distinct constructs, reducing interpretive precision and masking potentially divergent relationships with external variables. Researchers and practitioners should report and analyze subscale scores separately.

**The subscales are reliable and structurally sound for research use.** With subscale alphas of .79, item-total correlations consistently above .59, and clean factor loadings above .71, both the College Response and Stigma subscales meet conventional thresholds for psychometric adequacy.

**The two dimensions capture distinct aspects of the campus experience.** The near-zero between-factor correlation means that an institution could score high on visible stigma but high on institutional responsiveness — or low on both, or any other combination. This orthogonality has real implications for intervention: policies targeting institutional responsiveness (training, formal procedures, resource allocation) may be wholly independent from interventions targeting peer-level stigma (climate campaigns, cultural programming). Treating total scores as if they represent a single construct would collapse this meaningful distinction.

### 8.3 Limitations

First, data in this project are simulated from published parameters rather than collected empirically. While the simulation accurately reproduces the published covariance structure, it cannot capture sampling variability, measurement artifacts, or item functioning specific to any real sample.

Second, the validation does not include external criterion validity — the correlations between subscale scores and theoretically related external variables (e.g., sense of belonging, psychological distress, academic engagement). Construct validity in the full sense requires evidence beyond internal structure.

Third, this is an exploratory rather than confirmatory analysis. Confirmatory factor analysis (CFA) using structural equation modeling would provide fit indices (CFI, RMSEA, SRMR) that formally quantify how well the two-factor model fits the data — a necessary next step before deploying this scale in high-stakes applied contexts.

---

## 9. Conclusion

This project demonstrated a complete psychometric scale validation workflow spanning data preparation, reliability analysis, item analysis, and exploratory factor analysis. Applied to the LGBTQ Campus Climate Scale, the workflow produced convergent evidence from four independent analytic angles supporting a two-factor measurement model. Subscale reliability was acceptable (α = .79), item functioning was strong and consistent with the hypothesized structure, and exploratory factor analysis under both PCA and PAF frameworks recovered a clean two-factor solution with loadings of .71–.88.

The same workflow is directly applicable to any multi-item survey instrument used in people analytics, organizational research, or educational assessment contexts. Organizations that deploy climate surveys, engagement surveys, or onboarding assessments without first establishing their psychometric properties risk drawing confident conclusions from structurally ambiguous data. Psychometric validation is not a theoretical nicety — it is the prerequisite for trustworthy measurement.

---

## References

Parent, M. C. (2013). Handling item-level missing data: Simpler is just as good. *The Counseling Psychologist, 41*(4), 568–600. https://doi.org/10.1177/0011000012445176

Revelle, W., & Condon, D. M. (2019). Reliability from α to ω: A tutorial. *Psychological Assessment, 31*(12), 1395–1411. https://doi.org/10.1037/pas0000754

Szymanski, D. M., & Bissonette, D. (2020). Perceptions of the LGBTQ College Campus Climate Scale: Development and psychometric evaluation. *Journal of Homosexuality, 67*(10), 1412–1428. https://doi.org/10.1080/00918369.2019.1591788

Thurstone, L. L. (1947). *Multiple factor analysis*. University of Chicago Press.

Zwick, W. R., & Velicer, W. F. (1986). Comparison of five rules for determining the number of components to retain. *Psychological Bulletin, 99*(2), 432–442. https://doi.org/10.1037/0033-2909.99.3.432
