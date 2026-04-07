# Project 13 - Unsupervised Segmentation

Author: Mintay Misgano, PhD

This project applies multiple unsupervised clustering methods to a credit card applicant dataset in order to identify behavioral segments without relying on approval status as a target. The focus is on comparing clustering structures across methods and interpreting where the results converge.

## What This Project Demonstrates

- Use of multiple clustering algorithms on the same standardized feature set
- Comparison of centroid-based, hierarchical, density-based, and mode-seeking approaches
- Interpretation of segment structure through cross-method convergence
- Practical treatment of noise points and atypical profiles in unsupervised data

## Main Finding

A four-segment structure appears consistently across the clustering methods, with meaningful differences in expenditure, account tenure, spending share, and derogatory reports. The strongest result is not any single algorithm, but the degree of convergence across them.

## Read This Project

- Start with [Clustering_Project_Summary.md](/Users/Taco/Library/CloudStorage/ProtonDrive-Skabone@pm.me-folder/2!!Career/GitHub_Portfolio/13_Clustering_Unsupervised_Segmentation/GitHub_Ready/Clustering_Project_Summary.md) for the short overview.
- Use [Clustering_Project_Report.md](/Users/Taco/Library/CloudStorage/ProtonDrive-Skabone@pm.me-folder/2!!Career/GitHub_Portfolio/13_Clustering_Unsupervised_Segmentation/GitHub_Ready/Clustering_Project_Report.md) for the full write-up.
- See [02_Clustering_Analysis_R.md](/Users/Taco/Library/CloudStorage/ProtonDrive-Skabone@pm.me-folder/2!!Career/GitHub_Portfolio/13_Clustering_Unsupervised_Segmentation/GitHub_Ready/02_Clustering_Analysis_R.md) for the detailed R workflow.

## Data Note

The dataset is a public credit card applicant dataset used here as a clustering case. The project is best interpreted as a methods demonstration in unsupervised segmentation rather than as a production scoring framework.
