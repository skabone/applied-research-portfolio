# Metrics Spec

## Purpose

Define the core hiring-pipeline metrics used in this package so the analysis can be interpreted consistently across stakeholders.

## Unit of analysis

- Candidate-level and stage-event-level synthetic records

## Core metrics

| Metric | Definition | Grain | Why it matters |
|---|---|---|---|
| `applied_count` | Count of unique candidates with an application event | Pipeline / subgroup | Starting volume for the funnel |
| `assessed_count` | Count of unique candidates who reached assessment | Pipeline / subgroup | Shows movement into formal evaluation |
| `hired_count` | Count of unique candidates with a hire outcome | Pipeline / subgroup | Final conversion outcome |
| `stage_conversion_rate` | Candidates advancing to next stage divided by candidates at prior stage | Stage / subgroup | Identifies pipeline friction points |
| `selection_ratio` | Candidates selected at a stage divided by candidates considered at that stage | Stage / subgroup | Core denominator for subgroup comparisons |
| `adverse_impact_ratio` | Selection ratio for subgroup divided by highest observed comparison-group selection ratio | Stage / subgroup | Screening flag for deeper fairness review |

## Guardrails

- Use minimum-n rules before interpreting subgroup ratios.
- Treat adverse impact screens as a review trigger, not as a stand-alone decision rule.
- Pair metric review with documentation on cut scores, job-relatedness, and assessment purpose.

