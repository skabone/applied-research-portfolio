-- Hiring & Selection Pipeline Analytics (synthetic) - SQLite schema

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS outcomes;
DROP TABLE IF EXISTS pipeline_events;
DROP TABLE IF EXISTS assessments;
DROP TABLE IF EXISTS candidates;

CREATE TABLE candidates (
  candidate_id TEXT PRIMARY KEY,
  requisition_id TEXT NOT NULL,
  job_family TEXT NOT NULL,
  location TEXT NOT NULL,
  source_channel TEXT NOT NULL,
  application_date TEXT NOT NULL, -- ISO8601 date

  -- synthetic demographic fields (for fairness screening demos only)
  gender_group TEXT NOT NULL,
  race_ethnicity_group TEXT NOT NULL
);

CREATE TABLE assessments (
  assessment_id TEXT PRIMARY KEY,
  candidate_id TEXT NOT NULL,
  assessment_type TEXT NOT NULL,
  assessment_date TEXT NOT NULL, -- ISO8601 date
  raw_score REAL NOT NULL,
  standard_score REAL NOT NULL,
  passed_flag INTEGER NOT NULL CHECK (passed_flag IN (0, 1)),
  FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);

CREATE TABLE pipeline_events (
  event_id TEXT PRIMARY KEY,
  candidate_id TEXT NOT NULL,
  stage TEXT NOT NULL, -- applied, screen, assessment, interview, offer, hire
  stage_date TEXT NOT NULL, -- ISO8601 date
  stage_outcome TEXT NOT NULL, -- pass, fail, withdrawn
  FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);

CREATE TABLE outcomes (
  candidate_id TEXT PRIMARY KEY,
  month3_retained_flag INTEGER NOT NULL CHECK (month3_retained_flag IN (0, 1)),
  early_performance_rating REAL NOT NULL,
  FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);

