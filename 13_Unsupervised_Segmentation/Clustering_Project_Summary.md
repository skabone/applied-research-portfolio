# Unsupervised Segmentation of Credit Card Applicants

This project explores whether meaningful applicant profiles can be recovered without using approval status as a target. Instead of framing the problem as prediction, it treats it as an unsupervised segmentation task and compares what several clustering algorithms recover from the same feature set.

The strongest aspect of the project is methodological comparison. K-means, hierarchical clustering, DBSCAN, and mean shift each impose different assumptions about cluster shape and density. When several of them point toward a similar four-segment structure, that convergence becomes the most persuasive result in the analysis.

The segments differ in interpretable ways across expenditure, income, account activity, derogatory reports, and tenure. DBSCAN also adds a useful wrinkle by identifying a subset of observations as noise, showing that not every applicant profile fits cleanly into a stable segment.

As a portfolio piece, the project demonstrates unsupervised learning, cross-method comparison, and practical interpretation of cluster stability rather than just running a single clustering algorithm and accepting its output at face value.
