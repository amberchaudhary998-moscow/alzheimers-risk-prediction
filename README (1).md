# 🧠 Alzheimer's Disease Risk Prediction Using Machine Learning

### Machine Learning + Explainable AI

A machine learning project for predicting dementia status using demographic, cognitive, and brain-related measurements from OASIS patient metadata.

> ⚠️ **Disclaimer:** This project is intended for research and educational purposes only. It is not a medical diagnostic system and should not be used for clinical decision-making.

---

## 📌 Project Overview

Alzheimer's disease and other forms of dementia are major neurological conditions that can affect memory, cognition, and daily functioning.

This project explores the use of machine learning to classify patients into:

- **NonDemented**
- **Demented**

The project uses clinical, demographic, cognitive, and anatomical features and compares multiple machine learning algorithms before selecting the final model.

The project also incorporates **SHAP (SHapley Additive exPlanations)** to provide model interpretability.

---

## 🎯 Objectives

- Build a machine learning model for dementia status classification.
- Compare multiple machine learning algorithms.
- Handle missing clinical data using preprocessing pipelines.
- Evaluate model performance using multiple classification metrics.
- Validate the selected model using 5-fold cross-validation.
- Evaluate performance on an independent test dataset.
- Use SHAP for model explainability.
- Deploy the trained model as an interactive Streamlit web application.

---

## 📊 Dataset

The project uses OASIS patient metadata.

### Features

The final model uses the following features:

| Feature | Description |
|---|---|
| Age | Patient age |
| M/F | Patient gender |
| Educ | Years of education |
| SES | Socioeconomic status |
| MMSE | Mini-Mental State Examination score |
| eTIV | Estimated Total Intracranial Volume |
| nWBV | Normalized Whole Brain Volume |
| ASF | Atlas Scaling Factor |

### Target

The original dataset contained multiple dementia-related classes:

- NonDemented
- VeryMildDemented
- MildDemented
- ModerateDemented

For this project, these were converted into a binary classification problem:

```text
NonDemented → 0
All dementia classes → 1                 Predicted
                 NonDemented  Demented

Actual NonDemented     196       19
Actual Demented         6       23alzheimers-risk-prediction/
│
├── alzheimers_xgboost_model.pkl
├── app.py
├── README.md
└── requirements.txtpip install -r requirements.txtstreamlit run app.pyOASIS Patient Metadata
        ↓
Data Cleaning
        ↓
Feature Selection
        ↓
Missing Value Handling
        ↓
Feature Encoding & Scaling
        ↓
Train / Validation Split
        ↓
Model Comparison
        ↓
XGBoost Selection
        ↓
5-Fold Cross-Validation
        ↓
Independent Test Evaluation
        ↓
SHAP Explainability
        ↓
Final Model Training
        ↓
Streamlit Deployment
### One important correction

Notice I changed the wording around **“risk”** and **“probability.”** Your model predicts the **dementia class**, so we shouldn't present its 64.1% output as a medically validated “64.1% risk of Alzheimer's.”

That's a much safer and more professional way to present the project in a portfolio.

**Do this one step first:** replace the README with the above, commit the changes, and tell me when it's done. Then we'll do the next README improvement: **:contentReference[oaicite:0]{index=0}.**
> 
