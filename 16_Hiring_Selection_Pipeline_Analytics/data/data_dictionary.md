# Data Dictionary (Planned)

This data dictionary describes the synthetic tables used in the project.

## `candidates`

- `candidate_id`: Unique candidate identifier (synthetic)
- `requisition_id`: Role opening identifier (synthetic)
- `job_family`: Job family (e.g., Engineering, Operations, Corporate)
- `location`: Location grouping (e.g., Seattle, Remote, Other)
- `source_channel`: Candidate source channel (e.g., Referral, Job board, Campus)
- `application_date`: Date of application (synthetic)

### Demographic fields (synthetic)

These fields exist only to demonstrate fairness/adverse impact screening logic.

- `gender_group`: e.g., `Women`, `Men`, `Nonbinary/Other`, `Unknown`
- `race_ethnicity_group`: high-level grouping (synthetic)

## `assessments`

- `candidate_id`
- `assessment_type`: e.g., `cognitive`, `personality`, `work_sample`, `structured_interview`
- `assessment_date`
- `raw_score`
- `standard_score`
- `passed_flag`

## `pipeline_events`

Event-level table to compute funnel metrics.

- `candidate_id`
- `stage`: e.g., `applied`, `screen`, `assessment`, `interview`, `offer`, `hire`
- `stage_date`
- `stage_outcome`: e.g., `pass`, `fail`, `withdrawn`

## `outcomes` (optional)

Early outcomes table (synthetic) to show how selection predictors could relate to early success.

- `candidate_id`
- `month3_retained_flag`
- `early_performance_rating` (synthetic scale)

