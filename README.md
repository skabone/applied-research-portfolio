# People Analytics and Applied Research Portfolio

**Mintay Misgano, PhD**
People analytics, psychometrics, survey research, applied statistics, and machine learning.

These applied research projects translate organizational questions into evidence: workforce outcomes, assessment quality, survey measurement, statistical modeling, and program evaluation. The strongest projects combine clear problem framing, reproducible workflows, visual evidence, and deeper technical reports.

## Navigation

- [Resume (PDF)](./resume/Mintay_Misgano_PhD_Resume.pdf)
- [LinkedIn](https://www.linkedin.com/in/mmisgano/)
- [Project Catalog](./docs/project-catalog.md)
- [Methods Map](./docs/methods-map.md)
- [Reading Guide](./docs/reading-guide.md)
- [Changelog](./CHANGELOG.md)

## Featured Work

### Consulting Bid Accuracy Analysis

[![Estimated bill compared with final invoice](./02_Consulting_Bid_Accuracy_Analysis/docs/figures/eda-bill-vs-invoice-1.png)](./02_Consulting_Bid_Accuracy_Analysis)

A real consulting engagement is represented with a synthetic, anonymized public dataset. The analysis compares project bids with final invoices and finds that estimation error is more relational than structural: consultant and client-account effects explain more variance than broad service categories.

### Employee Engagement Pulse Survey Design

[![Quarterly engagement trend by subscale](./10_Employee_Engagement_Survey_Design/docs/figures/quarterly-trend-1.png)](./10_Employee_Engagement_Survey_Design)

This design project builds a quarterly engagement instrument around Vigor, Dedication, and Absorption, then specifies how the instrument should be scored, validated, and reported before any organization acts on the results.

### Advanced Regression For Non-Standard Outcomes

[![Tobit predicted affairs by marriage rating](./15_Advanced_Regression_Methods/docs/figures/fig07-tobit-predicted.png)](./15_Advanced_Regression_Methods)

Counts, ordered categories, truncated samples, and censored outcomes violate ordinary least squares assumptions in different ways. This project compares Poisson, negative binomial, ordinal logistic, truncated, and Tobit models against simpler linear alternatives.

### R Statistical Methods: Survival Analysis

[![Cox model forest plot](./08_R_Statistical_Methods_Showcase/docs/figures/cox-forest-1.png)](./08_R_Statistical_Methods_Showcase)

The survival-analysis workflow evaluates time-to-event outcomes with Kaplan-Meier curves, Cox proportional hazards modeling, proportional-hazards checks, and clear interpretation of effect sizes and assumptions.

### Career Fair Program Analytics

[![Student experience indicators](./17_Career_Fair_Program_Analytics/docs/figures/student-experience-1.png)](./17_Career_Fair_Program_Analytics)

This program-evaluation project analyzes student and employer feedback to identify where career fair preparation, event design, and follow-up support can improve participant experience.

### Titanic Passenger Survival Classification

[![Cross-validated model comparison](./06_Titanic_ML_Classification/docs/figures/fig04-cross-validated-model-comparison.png)](./06_Titanic_ML_Classification)

The Titanic benchmark is rebuilt as a disciplined tabular classification workflow with project-local data, training-set-only preprocessing, six model comparisons, and an executed notebook.

## Projects By Theme

| Theme | Projects |
|---|---|
| People analytics and workforce research | [IBM HR Attrition](./01_IBM_HR_Attrition_Analysis), [Consulting Bid Accuracy](./02_Consulting_Bid_Accuracy_Analysis), [Data Scientist Market Analysis](./03_Data_Scientist_Market_Analysis), [Job Change Prediction](./09_Job_Change_Prediction_CRISP_DM), [Hiring Selection Pipeline Analytics](./16_Hiring_Selection_Pipeline_Analytics), [Career Fair Program Analytics](./17_Career_Fair_Program_Analytics) |
| Psychometrics and measurement | [Psychometrics Scale Validation](./05_Psychometrics_Scale_Validation_R), [Confirmatory Factor Analysis](./11_CFA_Confirmatory_Factor_Analysis), [Measurement Invariance](./12_Measurement_Invariance), [Employee Engagement Survey Design](./10_Employee_Engagement_Survey_Design) |
| Machine learning and data mining | [Titanic Classification](./06_Titanic_ML_Classification), [Python ML Methods](./07_Python_ML_Methods_Showcase), [Unsupervised Segmentation](./13_Unsupervised_Segmentation) |
| Public policy and labor-market analysis | [US Broadband Access](./04_US_Broadband_Access_Analysis), [Data Scientist Market Analysis](./03_Data_Scientist_Market_Analysis) |
| Statistical methods | [R Statistical Methods](./08_R_Statistical_Methods_Showcase), [ANOVA Methods](./14_ANOVA_Methods_Showcase), [Advanced Regression Methods](./15_Advanced_Regression_Methods) |

## How Projects Are Organized

Most polished projects follow this structure:

| File | Role |
|---|---|
| `README.md` | Entry point with the problem, key finding, and navigation. |
| `01_Project_Summary.md` | Concise findings-first overview. |
| `02_Project_Report.md` | Full technical report with methods, results, limitations, and references. |
| `03_*` | Rendered workflow or executed notebook. |
| `04_*` | Source workflow when useful. |
| `docs/figures/` | Stable figure exports used in the README, summary, and report. |

For Python-based projects, install the shared public-analysis dependencies with:

```bash
python -m pip install -r requirements.txt
```

R-based projects list package requirements in the relevant `.Rmd` or analysis file.

## Data And Confidentiality

Public benchmark, simulated, synthetic, and anonymized datasets are labeled inside each project. NDA-related work is represented only through synthetic or generalized artifacts. Protected source records, contacts, and private context notes are excluded from this repository.
