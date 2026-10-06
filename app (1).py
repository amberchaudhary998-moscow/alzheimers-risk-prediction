import sklearn
import streamlit as st

st.write("Scikit-learn version:", sklearn.__version__)
import streamlit as st
import sklearn
import xgboost
import joblib
import pandas as pd

st.write("Python environment check")
st.write("scikit-learn:", sklearn.__version__)
st.write("XGBoost:", xgboost.__version__)
st.write("joblib:", joblib.__version__)
st.write("pandas:", pd.__version__)
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("alzheimers_xgboost_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Alzheimer's Risk Prediction",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 Alzheimer's Disease Risk Prediction")
st.write(
    "Enter the patient's demographic, cognitive, and anatomical information "
    "to obtain a machine-learning-based dementia risk prediction."
)

st.divider()

# Patient inputs
st.subheader("Patient Information")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=70
)

gender = st.selectbox(
    "Gender",
    options=["F", "M"]
)

educ = st.number_input(
    "Education (years)",
    min_value=0,
    max_value=30,
    value=14
)

ses = st.number_input(
    "Socioeconomic Status (SES)",
    min_value=1,
    max_value=5,
    value=2
)

mmse = st.number_input(
    "MMSE Score",
    min_value=0.0,
    max_value=30.0,
    value=28.0
)

etiv = st.number_input(
    "Estimated Total Intracranial Volume (eTIV)",
    min_value=500.0,
    max_value=3000.0,
    value=1500.0
)

nwbv = st.number_input(
    "Normalized Whole Brain Volume (nWBV)",
    min_value=0.1,
    max_value=1.0,
    value=0.72
)

asf = st.number_input(
    "Atlas Scaling Factor (ASF)",
    min_value=0.5,
    max_value=2.0,
    value=1.17
)

st.divider()

# Prediction
if st.button("🔍 Predict Dementia Risk", use_container_width=True):

    patient_data = pd.DataFrame([{
        "Age": age,
        "M/F": gender,
        "Educ": educ,
        "SES": ses,
        "MMSE": mmse,
        "eTIV": etiv,
        "nWBV": nwbv,
        "ASF": asf
    }])

    prediction = model.predict(patient_data)[0]
    probability = model.predict_proba(patient_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Model Prediction: Demented")
    else:
        st.success("✅ Model Prediction: NonDemented")

    st.metric(
        "Estimated Dementia Probability",
        f"{probability * 100:.2f}%"
    )

    st.progress(float(probability))

    st.caption(
        "This is a research/educational machine-learning prediction "
        "and is not a medical diagnosis."
    )

