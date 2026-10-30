import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
st.set_page_config(page_title="FraudShield AI", layout="wide")

# ---------- Load saved objects (cached so they load only once) ----------
@st.cache_resource
def load_assets():
    model = XGBClassifier()
    model.load_model("fraud_model.json")
    scaler = joblib.load("scaler.pkl")
    features = joblib.load("feature_names.pkl")
    explainer = shap.TreeExplainer(model)
    return model, scaler, features, explainer

@st.cache_data
def load_samples():
    return pd.read_csv("sample_transactions.csv")

model, scaler, features, explainer = load_assets()
samples = load_samples()

# ---------- Risk band (same cut-offs as Step 7) ----------
def get_band(p):
    if p < 0.02:
        return "LOW", "Approve"
    elif p < 0.5:
        return "MEDIUM", "Send for manual review"
    return "HIGH", "Block / contact customer"

# ---------- Page ----------
st.title("FraudShield AI")
st.caption("Explainable credit card fraud detection and risk scoring")

st.sidebar.header("Choose a transaction")
show = st.sidebar.radio("Show", ["All", "Fraud only", "Legit only"])
if show == "Fraud only":
    pool = samples[samples["Class"] == 1].reset_index(drop=True)
elif show == "Legit only":
    pool = samples[samples["Class"] == 0].reset_index(drop=True)
else:
    pool = samples

idx = st.sidebar.number_input("Transaction number", 0, len(pool) - 1, 0)
row = pool.iloc[[idx]].copy()
true_label = int(row["Class"].iloc[0])

# Prepare exactly as in training: drop target, scale Amount and Time, same column order
X_row = row.drop(columns=["Class"])
X_row[["Amount", "Time"]] = scaler.transform(X_row[["Amount", "Time"]])
X_row = X_row[features]

# ---------- Predict ----------
proba = model.predict_proba(X_row)[0, 1]
risk = proba * 100
band, action = get_band(proba)

c1, c2, c3 = st.columns(3)
c1.metric("Risk score (0-100)", f"{risk:.1f}")
c2.metric("Risk band", band)
c3.metric("Suggested action", action)

st.write(f"Amount: **{row['Amount'].iloc[0]:.2f}**")
with st.expander("Show actual label (for demo only)"):
    st.write("This transaction was really:", "FRAUD" if true_label == 1 else "LEGIT")

# ---------- Explain ----------
st.subheader("Why this score?")
sv = explainer.shap_values(X_row)[0]
contrib = pd.Series(sv, index=X_row.columns)
top = contrib.reindex(contrib.abs().sort_values(ascending=False).index)[:5]

st.write("**Top 5 factors behind this decision:**")
for feat, val in top.items():
    direction = "toward FRAUD" if val > 0 else "toward LEGIT"
    st.write(f"- **{feat}** = {row[feat].iloc[0]:.2f} pushes the score **{direction}** ({val:+.2f})")

fig, ax = plt.subplots(figsize=(7, 3.5))
t = top[::-1]
ax.barh(t.index, t.values, color=["red" if v > 0 else "dodgerblue" for v in t.values])
ax.axvline(0, color="grey", linewidth=0.8)
ax.set_xlabel("Push toward legit (left) or fraud (right)")
st.pyplot(fig, use_container_width=False)
plt.close(fig)

with st.expander("Detailed SHAP waterfall"):
    plt.figure(figsize=(8, 5))
    shap.plots._waterfall.waterfall_legacy(
        explainer.expected_value, sv, X_row.iloc[0], max_display=10, show=False
    )
    st.pyplot(plt.gcf(), use_container_width=False)
    plt.close("all")

st.caption("Red pushes toward fraud, blue toward legit. V1-V28 are anonymized, so we know which "
           "features matter, not what they mean.")