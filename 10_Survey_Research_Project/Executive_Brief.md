# Employee Engagement Survey Design — Executive Brief
**Domain:** Survey Research & Design / I-O Psychology / People Analytics | **Analyst:** Mintay Misgano | **Year:** 2023

---

## The Business Problem

Employee engagement is one of the strongest predictors of organizational performance — and one of the most poorly measured constructs in HR practice. Gallup (2023) estimates that low engagement costs the global economy $8.8 trillion annually; North American organizations have seen engagement decline for two consecutive years. Yet most organizations either don't measure engagement at all, use a single-item proxy ("How likely are you to recommend us as an employer?"), or deploy commercial surveys without understanding what they're actually measuring. This project designs a rigorous, theoretically grounded, quarterly Employee Engagement Pulse Survey from scratch — covering every stage of the survey lifecycle from research design through item development, sampling, administration, and analysis planning.

---

## Approach

- Grounded the instrument in the **Utrecht Work Engagement Scale (UWES)** (Schaufeli et al., 2002) — the most extensively validated multi-dimensional engagement measure in organizational psychology, with reliability data across 30+ countries and industries
- Designed a **20-item quarterly pulse survey** (15 engagement items across three UWES dimensions + 5 demographic items) for 10–15 minute completion on a 5-point Likert scale
- Specified an **item ordering strategy** based on cognitive load research (Sudman et al., 1996): Vigor (most generic) → Dedication (bridge concept) → Absorption (most cognitively demanding); demographics moved to end of survey
- Developed a complete **stratified random sampling strategy** ensuring proportional department representation with n ≥ 30 per stratum for reliable subgroup estimates
- Documented the full methodological rationale — design decisions, limitation acknowledgments (survey fatigue, social desirability bias, non-response bias), anonymization protocols, and a recommended analysis sequence (reliability checks → descriptives → ANOVA → regression → attrition linkage)
- Connected this design to the **psychometric validation workflow** demonstrated in Project 05 (scale validation) — specifying the pilot testing, item analysis, EFA, and CFA steps required before any new instrument enters full organizational use

---

## Key Design Decisions

- **Pulse over comprehensive:** 20 items quarterly beats 50-item annual surveys — higher response rates, faster insight cycles, time-sensitive data for intervention before attrition escalates
- **UWES foundation over proprietary tools:** The UWES is open-access, has published benchmark norms, and has been validated across 30+ countries — allowing cross-organizational comparisons that proprietary commercial instruments cannot support
- **Demographics at the end:** Moving demographic items to after engagement items reduces stereotype threat effects and preserves high-quality engagement responses at the start
- **Three-subscale scoring over a composite:** Reporting Vigor, Dedication, and Absorption scores separately — not just a total score — enables targeted interventions (a team low on Vigor needs different action than a team low on Dedication)
- **Anonymous, not confidential:** Survey uses full anonymization (no respondent IDs linked to data) rather than confidentiality (organization knows who responded) — the stronger protection that maximizes honest responding on sensitive workplace climate items

---

## Recommendations

1. **Pilot the instrument before organizational rollout.** Run the 15-item engagement battery with a 100+ person pilot sample; compute Cronbach's alpha (target ≥ .75 per subscale) and corrected item-total correlations (target ≥ .40) before full deployment. If internal consistency is insufficient, an exploratory factor analysis will identify which items are underperforming.
2. **Connect survey scores to HRIS data.** Linking anonymized engagement scores to tenure cohort, department, manager, and subsequent attrition creates a predictive dataset. A logistic regression or Cox survival model predicting voluntary departure from prior-quarter engagement scores is the most direct ROI demonstration for executive sponsors.
3. **Close the feedback loop every quarter.** Survey fatigue is driven not by survey frequency but by the perception that responses disappear into a void. Sharing results within 30 days of survey close and communicating specific changes made in response to the data is the single strongest driver of sustained participation rates.

---

## Impact

A well-designed engagement survey is the measurement infrastructure that makes all downstream people analytics work possible. Without reliable, valid engagement data collected systematically over time, organizations cannot identify at-risk subgroups before attrition peaks, cannot evaluate whether retention interventions are working, and cannot connect leadership practices to employee experience outcomes. This project demonstrates the end-to-end survey design competency — from theoretical grounding and item construction through sampling, administration, and analysis planning — that is prerequisite to any serious organizational measurement effort.

---

*Design by Mintay Misgano | Framework: UWES (Schaufeli et al., 2002) | Course: Survey Design and Development, SPU (Summer 2023) | N = 20 items, quarterly administration*
