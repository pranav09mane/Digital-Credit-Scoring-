import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and features 
rf = joblib.load("credit_model.pkl")
features = joblib.load("features.pkl")

# Scoring function 
def get_credit_score(student_data, model, features, classes):
    student_df = pd.DataFrame([student_data], columns=features)
    probs = model.predict_proba(student_df)[0]

    # Map risk buckets to base scores
    base_scores = {"High Risk": 300, "Medium Risk": 575, "Low Risk": 850}
    credit_score = sum(probs[i] * base_scores[c] for i, c in enumerate(classes))
    credit_score = float(round(credit_score, 1))

    risk_bucket = model.predict(student_df)[0]

    return {
        "Risk_Bucket": risk_bucket,
        "Credit_Score": credit_score
    }

# Streamlit UI 
st.title("🎓 Digital Credit Scoring for Students")
st.markdown("Enter student details and click **Get Credit Score**.")

# Inputs
age = st.number_input("Age", min_value=16, max_value=60, value=21)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
family_income = st.number_input("Family Income (INR)", min_value=0, max_value=10000000, value=600000, step=1000)
has_loan = st.selectbox("Has Loan?", ["No", "Yes"])
has_loan = 1 if has_loan == "Yes" else 0
savings = st.selectbox("Savings Pattern (0=None,1=Occasional,2=Regular)", [0,1,2], index=1)
subs = st.slider("Subscriptions Count", 0, 10, 2)
food = st.number_input("Food Spend (INR)", min_value=0, max_value=100000, value=1500, step=100)
expenses = st.number_input("Monthly Expenses (INR)", min_value=0, max_value=500000, value=8000, step=100)
internship = st.selectbox("Has Internship?", ["No","Yes"])
internship = 1 if internship == "Yes" else 0
scholarship = st.selectbox("Has Scholarship?", ["No", "Yes"])
scholarship = 1 if scholarship == "Yes" else 0

# Button and Result
if st.button("Get Credit Score"):
    student = {
        "Age": age,
        "CGPA": cgpa,
        "Family_Income_Clean": family_income,
        "Has_Loan": has_loan,
        "Savings_Score": savings,
        "Subscriptions_Count": subs,
        "Food_Spend": food,
        "Monthly_Expenses": expenses,
        "Has_Internship": internship,
        "Has_Scholarship": scholarship
    }

    result = get_credit_score(student, rf, features, rf.classes_)
    st.subheader("📊 Result")
    st.metric("Credit Score (300–850)", result["Credit_Score"])
    st.write("**Risk Bucket:**", result["Risk_Bucket"])
