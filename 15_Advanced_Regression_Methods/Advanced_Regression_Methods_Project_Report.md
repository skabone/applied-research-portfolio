# Advanced Regression Methods: Poisson, Negative Binomial, Ordinal, Truncated, and Tobit Models

**Author:** Mintay Misgano, PhD
**Tools:** R, MASS, AER, truncreg, tidyverse, ggplot2
**Year:** 2026

---

## Abstract

This project presents a comparative demonstration of several regression models used when ordinary linear regression is not appropriate. The collection includes Poisson regression, negative binomial regression, ordinal logistic regression, truncated regression, and Tobit regression. Each model is paired with a dataset whose outcome structure motivates its use, allowing the project to function as a practical reference for advanced regression model selection.

---

## 1. Project Context

Ordinary least squares regression assumes a continuous, normally distributed, and unbounded outcome. Many real datasets violate those assumptions. Count outcomes, ranked categories, truncated samples, and censored variables each require specialized models if the estimates are to remain interpretable and statistically appropriate.

This project was assembled as a methods collection to show how regression analysis changes once the form of the dependent variable changes.

---

## 2. Methods Included

### 2.1 Poisson Regression

Used for non-negative count outcomes when the mean and variance are approximately aligned.

### 2.2 Negative Binomial Regression

Used for count data when overdispersion is present and the Poisson variance assumption is too restrictive.

### 2.3 Ordinal Logistic Regression

Used when the outcome is ordered but not interval-scaled, such as ranked perception categories.

### 2.4 Truncated Regression

Used when only a restricted portion of the continuous outcome distribution is observed because of sample selection.

### 2.5 Tobit Regression

Used when the outcome is censored at a boundary and many observations pile up at the limit.

---

## 3. Comparative Value of the Collection

The main value of the collection is comparative model choice. Rather than showing five unrelated procedures, it organizes them around a common question: what should change in the regression model when the outcome variable changes?

Several pairings are especially instructive:

- Poisson versus negative binomial regression shows how overdispersion changes count modeling.
- Truncated versus Tobit regression shows the difference between data omitted by sampling design and data censored at an observable boundary.
- Ordinal regression shows why ranked response categories should not be treated as ordinary continuous outcomes.

---

## 4. Interpretation

This collection demonstrates that advanced regression is largely about matching model form to data structure. The most important skill on display is not memorizing formulas, but recognizing when the default linear model would produce biased, inefficient, or conceptually misleading estimates.

Because the project uses several separate datasets and outcome types, it is best interpreted as a methods reference and demonstration of model-selection reasoning rather than as a single domain-specific research study.

---

## 5. Conclusion

This project demonstrates breadth across advanced regression methods in R and shows how specialized models can be organized into one coherent workflow. As a portfolio piece, it highlights statistical judgment, model-selection discipline, and fluency with regression techniques beyond standard OLS.
