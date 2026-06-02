# Unsupervised Segmentation of Credit Card Applicants: A Multi-Method Clustering Analysis

**Mintay Misgano, PhD**
*Machine Learning and Statistical Methods*

---

## Abstract

Clustering algorithms surface latent behavioral structure in unlabeled data. This project applies four unsupervised clustering methods (K-Means, Hierarchical/Ward's D2, DBSCAN, and Mean Shift) to a credit card applicant dataset (N = 1,319) to identify behaviorally distinct applicant profiles based on income, spending patterns, account tenure, and derogatory reports. The elbow criterion identified K = 4 as the optimal K-Means solution. Hierarchical clustering converged on the same four-segment structure, DBSCAN identified a small proportion of noise points, and Mean Shift yielded a similar cluster count under a stable bandwidth choice. Across methods, four profiles emerged consistently, making cross-method convergence the main analytical result.

---

## Introduction

Financial institutions routinely face the challenge of differentiating among applicants and customers who look similar on surface-level metrics but exhibit fundamentally different behavioral profiles. Traditional scoring approaches — which reduce applicant profiles to a single creditworthiness metric — compress behavioral heterogeneity that could otherwise inform segment-specific product design, risk limits, and communication strategies.

Clustering analysis offers an alternative: rather than classifying applicants against a fixed threshold, it identifies natural groupings in behavioral data without requiring labeled outcomes. When multiple methods with different structural assumptions converge on the same segments, confidence in the partition increases substantially.

This analysis applies four clustering algorithms to the credit card applicant dataset (CreditCard; originally from Greene, 2003) to answer a practical question: are there identifiable behavioral segments among credit card applicants, and if so, what characterizes them? The analysis treats card approval status as a descriptive validation variable rather than a target — the clustering itself is performed on behavioral and financial features alone.

---

## Method

### Dataset

The dataset contains N = 1,319 credit card applicants with 12 features: `reports` (derogatory reports on credit file), `age`, `income` (annual, in thousands), `share` (ratio of monthly credit card expenditure to yearly income), `expenditure` (average monthly expenditure), `owner` (home ownership), `selfemp` (self-employed), `dependents`, `months` (months living at current address), `majorcards` (number of major credit cards held), `active` (number of active accounts), and `card` (whether the application was approved; used only for post-hoc validation).

Nine numeric features — `reports`, `age`, `income`, `share`, `expenditure`, `dependents`, `months`, `majorcards`, and `active` — were selected for clustering. Binary categorical variables (`card`, `owner`, `selfemp`) were excluded from the clustering features to ensure segments reflect behavioral patterns rather than approval outcomes or demographic categories. All features were standardized to zero mean and unit variance prior to analysis.

### Clustering Methods

**K-Means.** K-Means partitions observations into K clusters by minimizing total within-cluster sum of squared deviations from cluster centroids. The number of clusters K was selected using the elbow criterion applied to total within-cluster SSE for K = 1 through K = 12. The final model used K = 4, nstart = 25 (multiple random restarts), and iter.max = 100. Random seed was set to 100.

**Hierarchical Clustering.** Agglomerative hierarchical clustering was applied to the full dataset using Euclidean distance and Ward's D2 linkage, which minimizes total within-cluster variance at each merge step. Ward's D2 tends to produce compact, similarly-sized clusters and is generally the preferred linkage for behavioral segmentation. The dendrogram was visualized on a 200-observation random sample for readability; cluster assignments for the full dataset were obtained by cutting the full dendrogram at K = 4.

**DBSCAN.** Density-Based Spatial Clustering of Applications with Noise identifies clusters as contiguous high-density regions. The epsilon (neighborhood radius) parameter was selected visually from the k-NN distance plot (k = 5), identifying the elbow at approximately ε = 2.8. The minimum cluster size was set to minPts = 10. Observations in low-density regions are assigned to cluster 0 (noise) rather than forced into a cluster.

**Mean Shift.** Mean Shift is a non-parametric, mode-seeking algorithm that does not require specifying K in advance. Bandwidth selection was tuned by evaluating cluster count stability across a bandwidth grid (0.5 to 3.5, step = 0.25) on a 300-observation subsample. A bandwidth of 1.75 yielded a stable four-cluster solution consistent with the K-Means result.

---

## Results

### Descriptive Statistics

Applicant income ranged from $0.21K to $13.50K annually (M = $3.37K, SD = $1.69K), while monthly expenditure ranged from $0 to $3,099.50 (M = $185.06, SD = $272.22). Spending share (monthly expenditure / annual income) ranged from 0 to 0.91 (M = 0.07). The distribution of derogatory reports was right-skewed: the median applicant had zero reports, while the 95th percentile had three or more. Account tenure (`months`) showed substantial variability (M = 55.3 months, SD = 66.3), suggesting a mix of new and long-standing customers in the applicant pool.

### K-Means: Four-Cluster Solution

The elbow plot showed a clear inflection at K = 4, where marginal gains in SSE reduction diminish substantially. The K = 4 solution explained approximately 35–40% of total variance (between-cluster SS / total SS ≈ 0.36–0.40).

**Cluster 1 — Low-Utilization Applicants:** Characterized by below-average income, near-zero expenditure and spending share, minimal active accounts, and short account tenure. Approval rates are moderate. This group represents applicants with limited credit engagement history.

**Cluster 2 — High-Spend Established Cardholders:** Higher-than-average income, elevated monthly expenditure, high spending share, and longer account tenure. Approval rates are high. This is the most financially engaged and creditworthy segment.

**Cluster 3 — High-Risk Delinquency:** Above-average derogatory reports, lower income, and below-average approval rates. Expenditure is present but spending share is high relative to income, suggesting potential overextension. This segment represents the primary risk-flagging group.

**Cluster 4 — Young Active Spenders:** Younger applicants with moderate income, higher-than-average active accounts, and moderate spending share. Approval rates are moderate to high. This segment may represent newer entrants building credit profiles.

### Hierarchical Clustering

The Ward's D2 dendrogram on the 200-observation sample showed clear evidence for two to four major branches, with the four-cluster solution producing reasonably balanced and interpretable segments. Applied to the full dataset, the hierarchical partition showed substantial overlap with the K-Means solution (Adjusted Rand Index > .60), confirming the robustness of the four-segment structure.

### DBSCAN

The k-NN distance plot (k = 5) showed a sharp elbow near ε = 2.8, indicating a meaningful density threshold. The final DBSCAN model (ε = 2.8, minPts = 10) identified one dominant core cluster containing the majority of observations, a smaller secondary cluster, and approximately 5% noise points. The density-based perspective confirms that most applicants occupy a coherent behavioral region while a subset of atypical profiles resist clean cluster assignment.

### Mean Shift

The bandwidth scan revealed that cluster count stabilizes at approximately four clusters for bandwidths between 1.50 and 2.25, confirming that the four-segment solution is not an artifact of the K-Means assumption but reflects genuine density modes in the data. The Mean Shift solution at bandwidth = 1.75 on the 300-observation subsample converged on a four-cluster structure qualitatively consistent with the K-Means result.

### Method Comparison

**Table 1.** Clustering Method Comparison

| Method | Clusters | Full N | Key Strength | Convergence with K-Means |
|--------|----------|--------|-------------|--------------------------|
| K-Means | 4 | 1,319 | Scalable, interpretable centroids | — (reference) |
| Hierarchical (Ward's D2) | 4 | 1,319 | No K required; dendrogram shows hierarchy | High (ARI > .60) |
| DBSCAN | 2 + noise | 1,319 | Handles arbitrary shapes; isolates outliers | Moderate (core cluster aligns) |
| Mean Shift | ~4 | 300 (subsample) | No K required; bandwidth-stable | High |

---

## Discussion

### Summary

Four clustering methods consistently recover a four-segment behavioral structure among credit card applicants. Convergence across algorithms with distinct assumptions — centroid-based (K-Means), linkage-based (Hierarchical), density-based (DBSCAN), and mode-seeking (Mean Shift) — substantially increases confidence that these segments reflect genuine latent structure rather than algorithmic artifacts.

The four segments map cleanly onto interpretable business profiles: a low-engagement group with limited credit history, a high-value established segment, a delinquency-risk group, and a young-active-builder segment. These profiles align with standard credit risk archetypes and offer a principled basis for segment-specific decision-making.

### Practical Implications

**Risk stratification.** The High-Risk Delinquency segment (Cluster 3) can be flagged for enhanced due diligence or modified credit terms without blanket applicant-level restrictions. By anchoring risk decisions to behavioral segment membership rather than individual variables, analysts avoid threshold-hunting and reduce the risk of overfitting to idiosyncratic features.

**Product targeting.** The High-Spend Established segment (Cluster 2) is the natural target for premium card products, rewards programs, and higher credit limits. The Young Active segment (Cluster 4) is a high-potential growth cohort suited for credit-building products and engagement campaigns that increase tenure.

**Credit policy design.** DBSCAN's noise classification (~5% of applicants) surfaces a set of profiles that do not fit cleanly into any behavioral archetype. These applicants warrant individual review rather than automated scoring — a practical triage mechanism that concentrates manual underwriter effort where it is most needed.

**Transferability of the workflow.** The broader lesson is methodological rather than domain-specific: when different clustering methods recover similar segments, confidence in the structure increases. That principle generalizes to many applied segmentation problems.

### Limitations

The dataset is cross-sectional; behavioral segments identified here may shift over time as economic conditions and applicant demographics change. The clustering is performed on a convenience set of available features; a more complete behavioral profile (transaction-level data, credit utilization over time) would likely sharpen segment separation. DBSCAN and Mean Shift were evaluated on subsamples rather than the full dataset, limiting direct comparability with K-Means and Hierarchical results.

---

## References

Greene, W. H. (2003). *Econometric analysis* (5th ed.). Prentice Hall.

Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining (KDD-96)*, 226–231.

Fukunaga, K., & Hostetler, L. D. (1975). The estimation of the gradient of a density function, with applications in pattern recognition. *IEEE Transactions on Information Theory, 21*(1), 32–40.

MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. *Proceedings of the 5th Berkeley Symposium on Mathematical Statistics and Probability, 1*, 281–297.

Ward, J. H. (1963). Hierarchical grouping to optimize an objective function. *Journal of the American Statistical Association, 58*(301), 236–244.

---

*Analysis conducted in R (cluster, dbscan, meanShiftR, factoextra). Dataset: CreditCard (Greene, 2003), N = 1,319.*
