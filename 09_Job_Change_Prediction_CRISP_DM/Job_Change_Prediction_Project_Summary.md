# Job Change Prediction with CRISP-DM

This project uses a public Kaggle dataset to model which data science trainees are likely to look for a new job. The analysis is organized with the CRISP-DM framework so the work reads as a complete data-mining pipeline rather than just a sequence of modeling steps.

The workflow covers business framing, data understanding, data preparation, model comparison, and evaluation. Several classification models are trained on the same processed dataset, which makes it easier to compare their performance directly and to see why a metric such as ROC-AUC matters when the target class is imbalanced.

Gradient boosting performed best in this project, with random forest close behind. The most informative features were tied to local labor-market conditions and experience-related variables, which is a useful reminder that predictive patterns often reflect broader structural context rather than only individual traits.

As a portfolio piece, this project demonstrates CRISP-DM workflow design, tabular feature engineering, model comparison, and evaluation discipline on a realistic public classification dataset.
