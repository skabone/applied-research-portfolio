# Psychometric Scale Validation — Project Summary

**Dataset:** 646 simulated observations based on published scale parameters  
**Scope:** Reliability, item analysis, and exploratory factor analysis

---

## Project Context

This project was completed as part of graduate coursework in psychometrics. It uses a published campus climate instrument as a demonstration case for a full scale-validation workflow in R.

The central question was whether the scale should be interpreted as a single overall measure or as two distinct subscales.

---

## What Was Done

- Simulated item-level data from published factor loadings, means, and sample size
- Reverse-scored and prepared the items for analysis
- Estimated internal consistency at the total-scale and subscale levels
- Reviewed corrected item-total correlations and cross-subscale relationships
- Compared PCA and PAF solutions using orthogonal and oblique rotations
- Used parallel analysis to evaluate factor retention

---

## Main Takeaways

- **The scale is better interpreted as two subscales than one total score.** The total scale showed weaker internal consistency than the subscales.
- **Item-level evidence supports the theorized structure.** Items related strongly to their own subscale and weakly to the alternate subscale.
- **The factor structure was stable across methods.** PCA and PAF both recovered the same two-factor solution.
- **The two dimensions appear empirically distinct.** The near-zero factor correlation suggests that College Response and Stigma should not be collapsed into a single score without losing interpretive precision.
- **The simulated-data design strengthens transparency but limits inference.** The workflow is demonstrative and reproducible, but not a substitute for validation on new empirical data.

---

## What This Demonstrates

This project demonstrates several skills relevant to psychometrics, people analytics, and assessment work:

1. Translating psychometric theory into a reproducible analysis workflow
2. Evaluating reliability at both scale and subscale levels
3. Using item analysis to assess convergent and discriminant patterns
4. Comparing exploratory factor-analytic approaches rather than relying on a single method
5. Communicating measurement findings with appropriate limits and caution

---

## Bottom Line

This project works well as a psychometrics portfolio piece because it shows how measurement questions can be handled systematically. It demonstrates not only technical familiarity with reliability and factor analysis, but also the judgment to distinguish between a statistically cleaner interpretation and a less defensible one.
