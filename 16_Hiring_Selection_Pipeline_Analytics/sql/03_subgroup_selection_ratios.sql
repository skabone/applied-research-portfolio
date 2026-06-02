-- Subgroup selection ratios at each stage
--
-- This is a descriptive summary intended for screening and discussion.

WITH stage_status AS (
  SELECT
    pe.candidate_id,
    pe.stage,
    MAX(CASE WHEN pe.stage_outcome = 'pass' THEN 1 ELSE 0 END) AS passed
  FROM pipeline_events pe
  GROUP BY pe.candidate_id, pe.stage
),
base AS (
  SELECT
    c.gender_group,
    c.race_ethnicity_group,
    ss.stage,
    ss.passed
  FROM stage_status ss
  JOIN candidates c
    ON c.candidate_id = ss.candidate_id
)
SELECT
  stage,
  gender_group,
  race_ethnicity_group,
  COUNT(*) AS n_total,
  SUM(passed) AS n_passed,
  ROUND(1.0 * SUM(passed) / NULLIF(COUNT(*), 0), 4) AS pass_rate
FROM base
GROUP BY stage, gender_group, race_ethnicity_group
ORDER BY stage, gender_group, race_ethnicity_group;

