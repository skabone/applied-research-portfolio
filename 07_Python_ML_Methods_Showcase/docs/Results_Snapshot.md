# Results Snapshot

Metric summary for Project 07: College Institutional Profile Modeling.

## Dataset

- `N = 777` U.S. colleges and universities
- Private institutions: `565` (`72.7%`)
- Public institutions: `212` (`27.3%`)

## Verified Results

| Analysis | Key result | Interpretation |
|---|---|---|
| Graduation-rate regression | `R-squared = 0.487`; `RMSE = 10.98` graduation-rate points | Selected institutional features explain nearly half of holdout graduation-rate variance, but prediction error is still too large for high-stakes ranking. |
| Classifier comparison | SVM accuracy `0.937`; logistic regression accuracy `0.936`; random forest accuracy `0.929`; decision tree accuracy `0.901` | Private/public status is highly predictable, and the simpler logistic model is almost tied with the nonlinear SVM. |
| Random forest importance | Out-of-state tuition `0.279`, enrollment `0.193`, acceptances `0.110` | The classification signal is driven mainly by cost, scale, and admissions-volume variables. |
| k-means clustering | `ARI = -0.023` against private/public status | Unsupervised clusters do not naturally reproduce the private/public label. |
| Gaussian mixture model | `ARI = 0.289`; `AIC = 11544.8`; `BIC = 12154.7` | GMM aligns better than k-means but still only moderately tracks private/public status. |
| PCA | PC1 + PC2 explain `69.0%`; six components needed for at least `90%` variance | The feature space can be visualized in two dimensions, but substantial information remains outside the first two components. |

## Generated Figures

| Figure | File |
|---|---|
| Institution type balance | `docs/figures/fig01-institution-type-balance.png` |
| Graduation-rate regression coefficients | `docs/figures/fig02-graduation-regression-coefficients.png` |
| Classification model comparison | `docs/figures/fig03-classification-model-comparison.png` |
| Random forest feature importance | `docs/figures/fig04-random-forest-feature-importance.png` |
| PCA profile map | `docs/figures/fig05-pca-profile-map.png` |
| PCA variance explained | `docs/figures/fig06-pca-variance-explained.png` |
