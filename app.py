import os
os.system("pip install joblib")
import joblib

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("model/random_forest_model.pkl")

# Define the Streamlit UI
st.title("🏋️‍♂️ Personal Fitness Tracker")
st.write("Enter your details to predict calorie burn!")

# User Inputs
duration = st.number_input("Duration of Exercise (min)", min_value=1, max_value=180, value=30)
age = st.number_input("Age (years)", min_value=10, max_value=100, value=25)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

# Exercise Type Selection
exercise_options = ["Boxing", "Cycling", "Dancing", "Hiking", "Jump Rope", 
                    "Pilates", "Rowing", "Running", "Swimming", "Walking", 
                    "Weight Training", "Yoga"]
exercise_selected = st.selectbox("Select Exercise Type", exercise_options)

# Exercise Intensity
intensity = st.radio("Select Exercise Intensity", ["Low", "Medium", "High"])

# Convert Inputs into Model Format
exercise_columns = [f"Exercise_{e}" for e in exercise_options]
exercise_values = [1 if e == exercise_selected else 0 for e in exercise_options]

intensity_columns = ["Intensity_Low", "Intensity_Medium", "Intensity_High"]
intensity_values = [1 if i == intensity else 0 for i in ["Low", "Medium", "High"]]

input_data = [duration, age, weight] + exercise_values + intensity_values

# Load training data column names (to ensure correct feature order)
X_train = pd.read_csv("data/X_train.csv")  # Path to the training dataset
expected_features = list(X_train.columns)


# Convert Inputs into Model Format
exercise_columns = [f"Exercise_{e}" for e in exercise_options]
exercise_values = [1 if e == exercise_selected else 0 for e in exercise_options]

intensity_columns = ["Intensity_Low", "Intensity_Medium", "Intensity_High"]
intensity_values = [1 if i == intensity else 0 for i in ["Low", "Medium", "High"]]

input_data = [duration, age, weight] + exercise_values + intensity_values

# Create a DataFrame with the correct feature order
input_df = pd.DataFrame([input_data], columns=expected_features)  # Use correct feature order

# Predict Calories Burned
if st.button("Predict Calories Burned"):
    prediction = model.predict(input_df)[0]
    st.success(f"🔥 Estimated Calories Burned: {round(prediction, 2)} kcal")

