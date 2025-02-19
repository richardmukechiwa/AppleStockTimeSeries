from flask import Flask, request, jsonify, render_template, url_for
import numpy as np
import joblib
import tensorflow as tf
#from keras.models import load_model

app = Flask(__name__)

# Load the trained LSTM model correctly
#3from tensorflow.keras.models import load_model
model     = joblib.load("model.keras")


# Load the scaler
scaler = joblib.load('scaling.pkl')

@app.route('/')
def home():
    return render_template('home.html')

# Define API route for prediction
@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json['X']
        
        # Ensure correct shape for LSTM (1, 5, 1)
        input_data = np.array(data).reshape(1, 5, 1)
        
        # Make prediction
        prediction = model.predict(input_data)

        # Inverse transform the prediction to get the actual scale
        scaled_pred = scaler.inverse_transform(np.array(prediction).reshape(-1, 1))

        return jsonify({'prediction': float(scaled_pred[0, 0])})
    
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = [float(x) for x in request.form.values()]
        
        # Convert to NumPy array and reshape properly
        data = np.array(data).reshape(-1, 1)
        
        # Scale the input data
        scaled_data = scaler.transform(data).reshape(1, 5, 1)

        # Predict using the LSTM model
        prediction = model.predict(scaled_data)

        # Convert prediction back to original scale
        final_prediction = scaler.inverse_transform(prediction.reshape(-1, 1))

        return render_template('home.html', prediction_text=f"The Closing Stock Value is ${final_prediction[0, 0]:.2f}")
    
    except Exception as e:
        return render_template('home.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
