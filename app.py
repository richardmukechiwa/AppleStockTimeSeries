import streamlit as st
import numpy as np
import joblib
import tensorflow as tf

# Load model and scaler
model = joblib.load("model.keras")
scaler = joblib.load("scaling.pkl")

st.title("Time Series Forecasting")
st.write("Enter the last 5 closing values to predict the next one.")

# Create 5 inputs
values = []
for i in range(5, 0, -1):
    value = st.number_input(f"Closing Price {i} days ago", step=0.01)
    values.append(value)

if st.button("Predict"):
    try:
        # Convert and scale input
        data_array = np.array(values).reshape(-1, 1)
        scaled_data = scaler.transform(data_array).reshape(1, 5, 1)
        prediction = model.predict(scaled_data)
        final_prediction = scaler.inverse_transform(prediction.reshape(-1, 1))
        st.success(f"Predicted Closing Price: ${final_prediction[0,0]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
