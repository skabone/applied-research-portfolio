-- Adverse impact screen (4/5ths rule)
--
-- This is a preliminary screen, not a full legal/validation conclusion.
-- It compares each subgroup's pass rate to the highest pass rate observed
-- within the same stage and grouping dimension.

WITH stage_status AS (
  SELECT
    pe.candidate_id,
    pe.stage,
    MAX(CASE WHEN pe.stage_outcome = 'pass' THEN 1 ELSE 0 END) AS passed
  FROM pipeline_events pe
  GROUP BY pe.candidate_id, pe.stage
),
gender_rates AS (
  SELECT
    ss.stage,
    c.gender_group AS group_name,
    COUNT(*) AS n_total,
    SUM(ss.passed) AS n_passed,
    1.0 * SUM(ss.passed) / NULLIF(COUNT(*), 0) AS pass_rate
  FROM stage_status ss
  JOIN candidates c
    ON c.candidate_id = ss.candidate_id
  GROUP BY ss.stage, c.gender_group
),
gender_max AS (
  SELECT stage, MAX(pass_rate) AS max_pass_rate
  FROM gender_rates
  GROUP BY stage
),
race_rates AS (
  SELECT
    ss.stage,
    c.race_ethnicity_group AS group_name,
    COUNT(*) AS n_total,
    SUM(ss.passed) AS n_passed,
    1.0 * SUM(ss.passed) / NULLIF(COUNT(*), 0) AS pass_rate
  FROM stage_status ss
  JOIN candidates c
    ON c.candidate_id = ss.candidate_id
  GROUP BY ss.stage, c.race_ethnicity_group
),
race_max AS (
  SELECT stage, MAX(pass_rate) AS max_pass_rate
  FROM race_rates
  GROUP BY stage
)
SELECT
  'gender_group' AS dimension,
  gr.stage,
  gr.group_name,
  gr.n_total,
  gr.n_passed,
  ROUND(gr.pass_rate, 4) AS pass_rate,
  ROUND(gr.pass_rate / NULLIF(gm.max_pass_rate, 0), 4) AS impact_ratio,
  CASE
    WHEN (gr.pass_rate / NULLIF(gm.max_pass_rate, 0)) < 0.8 THEN 1
    ELSE 0
  END AS flagged_under_4_5ths
FROM gender_rates gr
JOIN gender_max gm
  ON gm.stage = gr.stage

UNION ALL

SELECT
  'race_ethnicity_group' AS dimension,
  rr.stage,
  rr.group_name,
  rr.n_total,
  rr.n_passed,
  ROUND(rr.pass_rate, 4) AS pass_rate,
  ROUND(rr.pass_rate / NULLIF(rm.max_pass_rate, 0), 4) AS impact_ratio,
  CASE
    WHEN (rr.pass_rate / NULLIF(rm.max_pass_rate, 0)) < 0.8 THEN 1
    ELSE 0
  END AS flagged_under_4_5ths
FROM race_rates rr
JOIN race_max rm
  ON rm.stage = rr.stage

ORDER BY 1, 2, 3;
