import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and encoder
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Page title
st.title("🛌 Sleep Disorder Prediction")
st.markdown("Predict the type of sleep disorder based on lifestyle and health inputs.")

# Input form
with st.form("prediction_form"):
    st.subheader("Input Features")
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 18, 80, 30)
    occupation = st.selectbox("Occupation", ["Nurse", "Doctor", "Engineer", "Lawyer", "Teacher", "Accountant", "Salesperson", "Scientist"])
    sleep_duration = st.slider("Sleep Duration (hours)", 3.0, 10.0, 7.0)
    quality_of_sleep = st.slider("Quality of Sleep (1-10)", 1, 10, 5)
    physical_activity = st.slider("Physical Activity Level", 0, 10, 3)
    stress_level = st.slider("Stress Level", 1, 10, 5)
    heart_rate = st.slider("Heart Rate", 50, 120, 70)
    daily_steps = st.number_input("Daily Steps", value=4000)
    bmi_category = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
    stress_category = st.selectbox("Stress Category", ["Low", "Medium", "High", "Very High"])
    bp_category = st.selectbox("Blood Pressure Category", ["Normal", "High", "Very High"])
    blood_pressure = st.selectbox("Blood Pressure (Raw)", ["120/80", "130/85", "140/90", "150/95"])
    systolic_bp = st.slider("Systolic Blood Pressure", 90, 180, 120)

    submitted = st.form_submit_button("Predict")

# Encode input and predict
if submitted:
    # Create DataFrame
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,
        "Sleep_Duration": sleep_duration,
        "Quality_of_Sleep": quality_of_sleep,
        "Physical_Activity_Level": physical_activity,
        "Stress_Level": stress_level,
        "BMI_Category": bmi_category,
        "Blood_Pressure": blood_pressure, 
        "Heart_Rate": heart_rate,
        "Daily_Steps": daily_steps,
        "Stress_Category": stress_category,
        "Systolic_BP": systolic_bp,
        "BP_Category": bp_category
       
       
    }])
    
    # The model already includes preprocessing (encoding + scaling)
    # So we can directly pass the raw input DataFrame

    # Predict
    prediction = model.predict(input_df)
    predicted_label = label_encoder.inverse_transform(prediction)[0]

    st.success(f"Predicted Sleep Disorder: **{predicted_label}**")
