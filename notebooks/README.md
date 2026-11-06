# Notebook guide

The executable training pipeline is maintained in `src/` so the application can be reproduced without depending on notebook state. The four requested notebook slots can be created from this workflow:

1. `01_data_analysis.ipynb` — inspect shape, missing values, duplicates and class balance.
2. `02_feature_engineering.ipynb` — document the feature representation and engineered risk ratios if the authorised dataset provides the required source variables.
3. `03_model_training.ipynb` — compare Logistic Regression, Random Forest and Gradient Boosting.
4. `04_model_evaluation.ipynb` — calculate held-out metrics and inspect confusion matrices/ROC curves.

The project intentionally keeps the production pipeline in Python modules rather than embedding critical logic only in notebooks.
