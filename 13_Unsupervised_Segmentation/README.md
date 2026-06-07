# Project 13 — Unsupervised Segmentation of Credit Card Applicants

**Mintay Misgano, PhD**

A four-segment behavioral structure emerges consistently across K-Means, Hierarchical (Ward's D2), DBSCAN, and Mean Shift clustering — four methods with structurally different assumptions applied to the same standardized feature set. Cross-method convergence (K-Means / Hierarchical ARI > 0.60; Mean Shift stable across bandwidth 1.50–2.25) is the primary result: it distinguishes genuine latent structure from algorithmic artifact.

![K-Means four-cluster solution on the two leading principal component dimensions. Cluster 2 (high-spend established) and Cluster 3 (delinquency-risk) are the most spatially separated — high-income/high-expenditure applicants cluster in the upper-right while high-report/low-income applicants concentrate in the lower region. The remaining two segments overlap in PCA space but differ in account tenure and active account counts.](docs/figures/kmeans-viz-1.png)

## Project Files

- **[01_Project_Summary.md](./01_Project_Summary.md)** — Plain-language overview of the approach, findings, and practical implications. Start here for a quick read.
- **[02_Project_Report.md](./02_Project_Report.md)** — Full technical write-up: method definitions, metric definitions (within-cluster SSE, ARI, ε, bandwidth), figure walkthroughs with exact values, and APA 7 references.
- **[02_Clustering_Analysis_R.md](./02_Clustering_Analysis_R.md)** — Rendered R workflow with all code, executed output, and inline figures for each analysis step.
- **[04_Source_Analysis.Rmd](./04_Source_Analysis.Rmd)** — R Markdown source file for the workflow.

## Data Note

The dataset is a public credit card applicant dataset (CreditCard; Greene, 2003, N = 1,319). Nine behavioral and financial features were used for clustering; approval status was excluded from the clustering features and used only for post-hoc validation.
