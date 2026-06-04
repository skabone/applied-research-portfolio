# When OLS Fails: Advanced Regression for Non-Standard Outcomes

Ordinary least squares regression fails silently on a common class of outcomes — counts, ranked categories, truncated samples, and censored measurements — producing biased estimates that understate the strength of real relationships. This project demonstrates five models that correct for each violation: Poisson, negative binomial, ordinal logistic, truncated, and Tobit regression. Each model is applied to a dataset whose outcome structure makes OLS inappropriate, and results are compared directly to OLS to show what the misspecification costs.

**Key finding:** Applying Tobit rather than OLS to a censored outcome with 56% zero reports more than doubled the estimated effect of marriage happiness on affair propensity (Tobit β = −1.11 vs OLS β = −0.53). Similarly, ordinal logistic regression revealed that US respondents were 85.5% more likely than Australians to perceive inadequate government poverty effort — a country-level pattern that a linear scale model would have suppressed.

![Tobit vs OLS predicted affairs by marriage rating — Tobit recovers a slope nearly twice as steep because OLS is attenuated by censoring at zero](docs/figures/fig07-tobit-predicted.png)

## Read This Project

- **[01_Project_Summary.md](./01_Project_Summary.md)** — Recruiter-facing overview: what was found, why it matters, key figures. Readable in under 3 minutes.
- **[02_Project_Report.md](./02_Project_Report.md)** — PhD-level write-up: full method definitions, APA 7 citations, model comparison tables, figure walkthroughs, and recommendations.
- **[03_Analysis.ipynb](./03_Analysis.ipynb)** — Executed, GitHub-viewable notebook: every model, table, and figure produced inline. **[04_Analysis.py](./04_Analysis.py)** is the annotated source script that generates the data, figures, and console output.

## Datasets

| Dataset | N | Source |
|---|---|---|
| Academic awards | 200 | UCLA IDRE (public) |
| World Values Survey extract | 5,381 | World Values Survey (public) |
| Academic scores | 178 | UCLA IDRE (public) |
| Illustrative affairs | 601 | Synthetic, modelled on Fair (1978) |

## Methods at a Glance

| Model | Outcome Structure | Dataset |
|---|---|---|
| Poisson regression | Count (non-negative integer) | Awards |
| Negative binomial | Overdispersed count | Awards |
| Ordinal logistic | Ordered categories | Poverty perception |
| Truncated regression | Continuous, sample range restricted | Academic scores |
| Tobit regression | Censored at boundary | Extramarital affairs |
