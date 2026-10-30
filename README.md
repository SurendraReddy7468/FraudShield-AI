# FraudShield AI
Explainable credit card fraud detection and risk scoring system.

## What it does
Predicts whether a credit card transaction is fraudulent, assigns a 0-100 risk score,
and explains the decision with SHAP. Shown in an interactive Streamlit dashboard.

## Dataset
Kaggle "Credit Card Fraud Detection" (mlg-ulb): 284,807 transactions over 2 days,
492 frauds (0.17%). Features V1-V28 are PCA-anonymized, plus Time, Amount, Class.
The CSV is not included (150 MB). Download it from Kaggle.

## Method
1. EDA: class imbalance, Amount, Time, feature distributions
2. Stratified 80/20 split, RobustScaler on Amount and Time (fit on train only)
3. Imbalance handling compared: SMOTE (train only) vs class weights vs none
4. Models: Logistic Regression, Random Forest, XGBoost
5. Evaluation with Precision, Recall, F1, ROC-AUC, PR-AUC (98 frauds in test set)
6. SHAP for explainability
7. Risk score = model probability x 100, grouped into Low / Medium / High bands

## Key results (test set)
| Model | Precision | Recall | F1 | PR-AUC |
|---|---|---|---|---|
| LogReg + SMOTE | 0.059 | 0.918 | 0.111 | 0.725 |
| RandomForest + SMOTE | 0.845 | 0.837 | 0.841 | 0.870 |
| XGBoost + SMOTE | 0.737 | 0.857 | 0.793 | 0.871 |
| XGBoost + scale_pos_weight (final) | 0.893 | 0.847 | 0.869 | 0.885 |

SMOTE was implemented and compared, but class weighting performed as well or better,
so XGBoost with scale_pos_weight is the deployed model.

## Run the app
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd app
python -m streamlit run app.py
```
Tested with Python 3.12.

## Limitations
- Only 98 frauds in the test set, so small differences between models are not reliable.
- The cut-off was explored on the test set, so scores are slightly optimistic.
- Some frauds look like normal transactions and are missed.
- The risk score is a ranking, not a true probability (scale_pos_weight inflates probabilities).
- V1-V28 are anonymized, so features can be ranked but not interpreted.

## Tech stack
Python, Pandas, NumPy, Scikit-learn, XGBoost, imbalanced-learn, SHAP, Matplotlib, Seaborn, Streamlit