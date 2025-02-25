
import streamlit as st
import pandas as pd
import numpy as np
import joblib
# Load the trained Random Forest model and scaler
best_rf = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Page Configuration
st.set_page_config(page_title="Motor Speed Predictor", layout="wide", page_icon="⚙️")

# Custom CSS for Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #007BFF;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("⚡ Electric Motor Speed Predictor")
st.markdown("""
### Welcome to the Electric Motor Speed Predictor!  

This tool uses a **Random Forest Regression** model to predict motor speed based on various input parameters.  
Simply enter the values below, and get instant predictions.
""")

# Sidebar Input Section
st.sidebar.header("🔢 Input Parameters")
ambient = st.sidebar.number_input('Ambient Temperature (℃) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")
coolant = st.sidebar.number_input('Coolant Temperature (℃) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")
u_d = st.sidebar.number_input('Voltage d-axis (u_d) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")
u_q = st.sidebar.number_input('Voltage q-axis (u_q) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")
torque = st.sidebar.number_input('Torque (Nm) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")
i_d = st.sidebar.number_input('Current d-axis (i_d) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")
pm = st.sidebar.number_input('Permanent Magnet Temperature (℃) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")
stator_tooth = st.sidebar.number_input('Stator Tooth Temperature (℃) [Range: -3.0 to 2.0]', min_value=-3.0, max_value=2.0, value=0.0, format="%.6f")

# Prepare data for prediction
input_data = pd.DataFrame({
    'ambient': [ambient],
    'coolant': [coolant],
    'u_d': [u_d],
    'u_q': [u_q],
    'torque': [torque],
    'i_d': [i_d],
    'pm': [pm],
    'stator_tooth': [stator_tooth]
})

# Standardize the input data
input_scaled = scaler.transform(input_data)

# Prediction
st.markdown("""
### 🔢 Prediction Result
""")

if st.button('Predict Motor Speed'):
    predicted_speed = best_rf.predict(input_scaled)[0]
    st.success(f"**Predicted Motor Speed:** {predicted_speed:.6f} RPM")
