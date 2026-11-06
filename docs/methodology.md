# CreditLens Methodology

1. **Data validation:** remove duplicates, inspect missing cells and identify the target.
2. **Feature preparation:** separate numerical and categorical variables and keep the target out of the input matrix.
3. **Leakage control:** the target is never passed to preprocessing or prediction. Preprocessing is fitted inside a scikit-learn Pipeline using only training data.
4. **Model comparison:** Logistic Regression, Random Forest and Gradient Boosting are evaluated on the same stratified hold-out set.
5. **Selection:** F1-score is prioritised, followed by ROC-AUC.
6. **Explainability:** SHAP contributions are calculated for the selected tree model and aggregated back to the original feature names.
7. **Risk dimensions:** five transparent rule-based dimensions complement the ML probability; they are not presented as a replacement for the ML model.
8. **What-if:** changed variables are passed through the same model pipeline and compared with the original prediction.
9. **Monitoring:** each assessment is persisted in SQLite so later assessments can be compared.

## Responsible AI
The project is an academic prototype. Its synthetic demonstration data cannot establish real-world lending performance. Bias, false positives, false negatives, privacy, distribution shift, model drift and human oversight must be addressed before any real deployment.
