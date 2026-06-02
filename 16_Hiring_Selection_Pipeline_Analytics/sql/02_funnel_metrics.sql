-- Funnel metrics by stage
--
-- Assumes data loaded into SQLite tables from `01_schema.sql`.

WITH stage_counts AS (
  SELECT
    stage,
    COUNT(DISTINCT candidate_id) AS candidates
  FROM pipeline_events
  WHERE stage_outcome IN ('pass', 'fail', 'withdrawn')
  GROUP BY stage
),
ordered AS (
  SELECT 'applied' AS stage, 1 AS stage_order UNION ALL
  SELECT 'screen', 2 UNION ALL
  SELECT 'assessment', 3 UNION ALL
  SELECT 'interview', 4 UNION ALL
  SELECT 'offer', 5 UNION ALL
  SELECT 'hire', 6
)
SELECT
  o.stage_order,
  o.stage,
  COALESCE(sc.candidates, 0) AS candidates
FROM ordered o
LEFT JOIN stage_counts sc
  ON sc.stage = o.stage
ORDER BY o.stage_order;

