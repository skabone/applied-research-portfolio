# U.S. Data Scientist Market Analysis (2021)

What did the 2021 U.S. data-science hiring market actually reward — which roles, skills, and locations carried the highest pay, and where did demand concentrate? This project answers that by analyzing 742 public job postings across salary, geography, employer profile, degree, and tool requirements, then translating the patterns into workforce- and talent-planning signals.

The analysis recomputes every reported figure from a public feature extract and rebuilds the visuals as a reproducible Python pipeline, so the evidence can be inspected directly from the repository.

![Median advertised salary by role group: ML Engineer $124K and Data Scientist $114K lead; Analyst roles trail at $62K](docs/figures/fig01-salary-by-role.png)

*Pay scaled sharply with role type. ML Engineer (median $124K, n=22) and Data Scientist ($114K, n=313) postings led the market, while Analyst roles ($62K, n=109) sat roughly $50K lower — a gap that widens further with seniority and degree requirements.*

## What the data showed

- **A small core stack dominated demand.** Python (52.8%), Excel (52.3%), and SQL (51.2%) each appeared in about half of postings, while specialized tools such as Flink (1.3%) and Google Analytics (1.9%) were negligible.
- **Skill bundles differed by role.** Analyst postings clustered on Excel (74%) and SQL (72%); Data Scientist and ML Engineer postings led on Python (77% and 82%) and the deep-learning libraries (TensorFlow, scikit-learn, PyTorch) that were essentially absent from analyst roles.
- **Demand concentrated geographically.** California (152 postings, median $121K), Massachusetts (103), and New York (72) led on volume, with California also highest on pay.
- **Pay rose with credentials and level.** PhD-required roles paid a median $120K vs. $89K where no degree was specified; senior roles paid $122K vs. $88K for unspecified-level postings.

## Where to go next

| File | What it is |
|------|------------|
| [`01_Project_Summary.md`](01_Project_Summary.md) | Two-to-three-minute, plain-language overview of the question, findings, and what they mean. |
| [`02_Project_Report.md`](02_Project_Report.md) | Full write-up: data, methods, metric definitions, figure-by-figure evidence, limitations, and references. |
| [`03_Analysis_Notebook.ipynb`](03_Analysis_Notebook.ipynb) | Executed analysis with all numbers and figures rendered inline. |
| [`04_Source_Code.py`](04_Source_Code.py) | Annotated script that reproduces every statistic and figure. |
| [`data/`](data) | Public analysis extract and its data note. |

## Data note

This project uses a public feature-level extract derived from a Kaggle dataset of Glassdoor job postings. Raw job descriptions, company names, headquarters, competitors, and any contact-bearing posting text are excluded from the repository. Salary ranges and company attributes are best read as directional 2021 labor-market signals rather than authoritative compensation benchmarks. The original cleaning was done in RapidMiner and Jamovi and the dashboards built in Power BI; the published pipeline reproduces that work in Python.
