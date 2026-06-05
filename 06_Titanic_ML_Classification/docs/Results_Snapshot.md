# Results Snapshot

This snapshot is produced by `04_Source_Code.py` from the public Kaggle Titanic files in `data/`.

## Data Profile

- Training rows: 891
- Test rows: 418
- Observed survivors in training data: 342 of 891 (38.4%)
- Observed non-survivors in training data: 549 of 891 (61.6%)
- Age missingness in training data: 19.9%
- Cabin missingness in training data: 77.1%

## Model Comparison

| Model | Accuracy mean | Accuracy SD | Balanced accuracy mean |
|:--|--:|--:|--:|
| Gradient Boosting | 0.838 | 0.026 | 0.818 |
| Random Forest | 0.832 | 0.004 | 0.813 |
| Hard-Voting Ensemble | 0.829 | 0.015 | 0.816 |
| Logistic Regression | 0.828 | 0.014 | 0.815 |
| Gaussian Naive Bayes | 0.807 | 0.011 | 0.811 |
| Decision Tree | 0.800 | 0.018 | 0.775 |

## Ensemble Diagnostics

- Best cross-validated model by accuracy: Gradient Boosting (0.838)
- Hard-voting ensemble out-of-fold precision for survived: 0.788
- Hard-voting ensemble out-of-fold recall for survived: 0.760
- Hard-voting ensemble out-of-fold balanced accuracy: 0.816
- Confusion matrix counts, observed rows by predicted columns [[0, 1], [0, 1]]: [[479, 70], [82, 260]]
- Final test-set predicted survival rate: 40.4%
- Best recorded Kaggle public leaderboard score: 0.79186

## Top Random Forest Predictors

| Rank | Feature | Importance |
|--:|:--|--:|
| 1 | Title_Mr | 0.181 |
| 2 | Sex_female | 0.161 |
| 3 | Sex_male | 0.120 |
| 4 | FareLog | 0.068 |
| 5 | Title_Miss | 0.051 |
| 6 | Pclass_3 | 0.047 |
| 7 | Title_Mrs | 0.044 |
| 8 | Age | 0.042 |
| 9 | FamilySize | 0.037 |
| 10 | HasCabin | 0.035 |

## Figures

- `docs/figures/fig01-survival-by-sex-class.png`
- `docs/figures/fig02-missingness-profile.png`
- `docs/figures/fig03-submission-history.png`
- `docs/figures/fig04-cross-validated-model-comparison.png`
- `docs/figures/fig05-feature-importance.png`
- `docs/figures/fig06-confusion-matrix.png`
