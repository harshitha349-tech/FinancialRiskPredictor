# CreditLens Viva Questions and Answers

1. **What is credit risk?** The possibility that a borrower will fail to meet agreed repayment obligations.
2. **What is the target in CreditLens?** A binary class representing good versus bad credit outcome in the demonstration dataset.
3. **Why is this supervised learning?** Historical examples contain an outcome label, so the model learns a mapping from applicant features to that label.
4. **Why classification?** The target is categorical rather than a continuous amount.
5. **Why not use accuracy alone?** Accuracy can hide poor minority-class detection when classes are imbalanced.
6. **What is precision?** Among cases predicted as risky, the proportion that are actually risky.
7. **What is recall?** Among actually risky cases, the proportion correctly identified.
8. **What is F1-score?** The harmonic mean of precision and recall.
9. **What is ROC-AUC?** A threshold-independent measure of how well the model ranks positive and negative cases.
10. **Why stratified splitting?** It keeps class proportions similar in train and test sets.
11. **What is data leakage?** Information from outside the allowed training process incorrectly enters model training.
12. **How is leakage reduced here?** Preprocessing is inside a Pipeline and is fitted only on the training split.
13. **Why one-hot encode categories?** Most scikit-learn classifiers need numeric inputs, so categorical levels are represented numerically.
14. **Why scale numerical features?** Scaling makes feature magnitudes more comparable, especially for Logistic Regression.
15. **Why compare three models?** It gives a defensible basis for model selection instead of assuming one algorithm is best.
16. **Why was Gradient Boosting selected?** In this run it achieved the strongest F1/ROC-AUC combination on the hold-out set.
17. **What is SHAP?** A feature-attribution method that estimates how features contribute to a model output.
18. **Why explain predictions?** A risk score is easier to review when the important contributing factors are visible.
19. **What is the What-if Simulator?** It changes supported applicant variables and reruns the same trained model pipeline.
20. **Does the simulator fake results?** No. It sends modified values through the prediction pipeline.
21. **What is the CreditLens Risk Score?** A transparent composite score that combines model default risk with five documented risk dimensions.
22. **What are the five dimensions?** Default Risk, Repayment Capacity, Financial Stress, Credit Stability and Debt Exposure.
23. **Does CreditLens approve loans?** No. It provides decision-support information and a recommendation for human review.
24. **Why use SQLite?** It is simple, local and requires no separate database server for a college demonstration.
25. **What is monitoring?** Reassessing an applicant over time and detecting meaningful changes in estimated risk.
26. **What is an early warning?** A message triggered when the latest risk score deteriorates materially compared with the previous assessment.
27. **What is model drift?** A change in data or relationships that causes a previously useful model to become less reliable.
28. **What is class imbalance?** A situation where one target class has substantially more observations than another.
29. **How can imbalance be handled?** Class weights, resampling, threshold tuning and appropriate evaluation metrics are common approaches.
30. **Why use class_weight in Logistic Regression and Random Forest?** To give greater learning importance to the minority class without duplicating rows.
31. **Why is recall important for risky borrowers?** Missing a genuinely risky borrower can be costly, so the ability to identify risky cases matters.
32. **Why can false positives still matter?** Incorrectly flagging a safer borrower can create unnecessary manual review or unfair outcomes.
33. **What is the biggest dataset limitation here?** The included demonstration data is synthetic and cannot establish real-world lending performance.
34. **What would you change for production?** Use authorised representative data, calibration, fairness testing, secure storage, authentication, monitoring and governance.
35. **What is the novelty?** Integration of multi-dimensional risk scoring, explainability, what-if simulation, recommendations and monitoring in one academic platform.
36. **Did you invent a new algorithm?** No. The novelty is in the integrated decision-support workflow.
37. **Why is human oversight required?** ML predictions can be wrong, biased, unstable under distribution shift, and inappropriate as the sole basis for consequential decisions.
38. **Why not include protected attributes?** They can introduce legal, ethical and fairness risks and are not needed for this academic prototype.
39. **What is the role of FastAPI?** It exposes validated prediction, simulation, monitoring and model-information endpoints.
40. **What is the role of React?** It provides the interactive dashboard and presents model results in an understandable interface.
