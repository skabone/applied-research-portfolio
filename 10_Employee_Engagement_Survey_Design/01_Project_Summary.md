# Employee Engagement Pulse Survey — Project Summary

Most organizations only learn that engagement has slipped after good people have already left. By then the data shows up as attrition, not as something leadership could have acted on. This project builds the instrument that closes that gap: a short, repeatable quarterly survey that measures employee engagement carefully enough to trust, and reports it quickly enough to act on.

The survey is built on the Utrecht Work Engagement Scale, a long-established measure that treats engagement not as a single "are you happy?" question but as three distinct things: **Vigor** (energy and resilience at work), **Dedication** (finding the work meaningful and worth caring about), and **Absorption** (getting genuinely lost in the work). Measuring all three separately means a low score points to *what* is wrong, not just *that* something is wrong.

![Instrument blueprint: one engagement construct measured through three subscales of five items each](docs/figures/instrument-blueprint-1.png)

The design covers the full survey lifecycle, not just the question list: which employees to sample and how many, how to administer it while protecting anonymity, how to score it, and — critically — how to validate it before trusting the numbers. That last piece is what separates a real measurement instrument from a questionnaire. Before any results are believed, the survey is checked for reliability (do the five items in a subscale actually hang together?), and the design specifies a clear pass mark: a reliability coefficient of at least 0.70.

To show how the finished instrument behaves in practice, the project includes a worked reporting demonstration on simulated data. It walks through exactly what leadership would see each quarter — overall trends, a department-by-department breakdown, and an item-level drill-down for any group that scores low.

![Illustrative department comparison: Customer Support (3.32) and Sales (3.34) fall well below Management (4.24), flagging where to look first](docs/figures/department-comparison-1.png)

In the demonstration, two departments — Customer Support (3.32 out of 5) and Sales (3.34) — fall far enough below the rest (Management sits at 4.24) that they would be automatically flagged for an item-level review rather than waiting for a manager to notice. That is the core value of the design: it turns a vague sense of "morale feels off" into a specific, traceable signal about *which group* and *which aspect of engagement* needs attention.

**Bottom line:** this is a measurement-design piece. It shows how to build a survey that produces decision-grade data — defensible enough to act on, fast enough to matter — and how to prove the instrument is trustworthy before a single decision is made on it.

For the full design specification, sampling rationale, scoring rules, and validation plan, see [02_Project_Report.md](./02_Project_Report.md). The scoring and reporting pipeline is implemented end-to-end in [03_Reporting_Demonstration.ipynb](./03_Reporting_Demonstration.ipynb).

*Originated as graduate coursework in survey design and development.*
