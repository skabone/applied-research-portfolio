# Measurement Invariance Testing of the AMS

The Ableist Microaggressions Scale is meant to measure disability-related microaggressions, but group comparisons are only meaningful if the scale works the same way across groups. This analysis asks whether mild and severe disability-severity groups can be compared fairly, or whether the items behave differently enough that raw mean differences could be misleading.

The analysis uses measurement invariance testing, which checks whether a scale keeps the same structure and item behavior across groups. First, it tests whether the same four-factor structure appears in both groups. Then it tests whether item loadings are comparable, meaning each item relates to its construct with similar strength. Finally, it tests whether item intercepts are comparable, meaning groups endorse items at the same expected level when their underlying construct level is equal.

![Item mean profiles by disability severity group](docs/figures/fig03-item-mean-profiles.png)

The visible group differences are large enough to matter: the Severe group scores higher on every item, and the biggest factor-level gaps appear in Denial of Personhood (+0.845 on the 0-5 item scale) and Otherization (+0.711). Measurement invariance testing separates that surface pattern from the deeper measurement question: are these comparable scores, or are the items partly shifting by group?

The answer is mixed. Weak invariance is supported: constraining factor loadings barely changes fit (Delta CFI = -.001), so the items generally relate to their intended constructs in comparable ways. Strong invariance is not supported: constraining item intercepts creates a large fit decline (Delta CFI = -.092), which means item baselines differ across groups.

The practical implication is that raw observed mean comparisons should be treated cautiously. The scale can support construct-structure and loading-level comparisons across the two groups, but direct mean comparisons need partial invariance modeling, latent-score methods, or item-level follow-up before they should be interpreted as group differences in the construct itself.
