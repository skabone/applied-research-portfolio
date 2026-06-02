# Project 09 - Job Change Prediction with CRISP-DM

Author: Mintay Misgano, PhD

This project applies the CRISP-DM framework to a public Kaggle dataset on job-change intent among data science trainees. The package is organized as a compact end-to-end classification workflow, from business framing and data preparation through model comparison and evaluation.

## What This Project Demonstrates

- Use of CRISP-DM as a structured workflow for an applied machine learning project
- Cleaning and feature engineering for a moderately large tabular dataset
- Comparison of multiple classification models under a shared cross-validation setup
- Use of ROC-AUC alongside accuracy for an imbalanced binary outcome

## Main Results

- Gradient boosting produced the strongest overall model performance in this workflow.
- Ensemble methods outperformed simpler single-model baselines.
- City development index, experience, and company-related features were among the strongest predictors.
- ROC-AUC was a more informative success metric than accuracy alone because the positive class was the minority class.

## Read This Project

- Start with `Job_Change_Prediction_Project_Summary.md` for the short overview.
- Use `Job_Change_Prediction_Project_Report.md` for the fuller CRISP-DM write-up.
- Open `Job_Change_Prediction_Data_Mining.ipynb` for a GitHub-rendered notebook version of the workflow.
- Use `Job_Change_Prediction_Data_Mining.py` if you prefer the script version.

## Project Files

| File | Role |
|------|------|
| `Job_Change_Prediction_Project_Summary.md` | Short interpretive overview of the project |
| `Job_Change_Prediction_Project_Report.md` | Full CRISP-DM write-up |
| `Job_Change_Prediction_Data_Mining.ipynb` | GitHub-rendered notebook companion for the workflow |
| `Job_Change_Prediction_Data_Mining.py` | Script version of the workflow |

## Data Note

The project uses Kaggle's HR Analytics: Job Change of Data Scientists dataset. It is best read as a benchmark-style applied data-mining project that demonstrates workflow, feature preparation, and model evaluation rather than a production deployment claim.
