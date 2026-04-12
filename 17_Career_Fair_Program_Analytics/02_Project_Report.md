# Career Fair Program Analytics — Project Report (First Pass)

## 1) Questions this analysis supports

1. What does participation look like (employers, reps, check-ins)?
2. What industries and employment types were represented?
3. How did students and employers rate the event experience?
4. What does the feedback suggest changing for the next cycle?

## 2) Data sources (private inputs → public outputs)

Private inputs (not published):

- Career fair registration export (contains employer + registrant contact fields)
- Student survey export (row-level responses)
- Employer survey export (row-level responses + open-ended comments)

Public outputs (published):

- Aggregated counts and distributions in `data/`
- Narrative snapshot in `docs/Results_Snapshot.md`

## 3) Methods

### Surveys

- Likert items are summarized as counts and % per response option.
- Key headline metric per item: **% Agree/Strongly Agree**.
- Yes/No items are summarized as % Yes.
- Open-ended items are excluded from the public dataset in this first pass.

### Registration export

- Contact fields are excluded.
- The analysis produces event-level totals and distributions (industry mix, employment types, target school years).
- Multi-value fields are split on commas and summarized as frequency tables.

## 4) Limitations

- Survey responses represent respondents only; results are descriptive.
- “Registration rows” may not perfectly map to unique employers if the export structure varies by event.
- Without linking to downstream outcomes (applications, interviews), results support event improvement rather than ROI estimation.

