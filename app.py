from flask import Flask, request, jsonify,render_template, url_for
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

app = Flask(__name__)

# Load the trained LSTM model
#model = joblib.load('model.keras')
model = tf.keras.models.load_model('model.keras')  # Load Keras model correctly

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
        input_data = np.array(data).reshape(1, 5, 1)  # Ensure the correct shape

        # Make prediction
        prediction = model.predict(input_data)
        
        # Inverse transform the prediction
        scaled_pred = scaler.inverse_transform(prediction.reshape(-1, 1))

        return jsonify({'prediction': float(scaled_pred[0, 0])})
    except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/predict',methods = ['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    
    data    = np.array(data).reshape(-1, 1)
    final_input= scaler.transform(np.array(data).reshape(1, 5, 1))
    print(final_input)
    prediction= model.predict(final_input)
    
    final_predition = scaler.inverse_transform(prediction.reshape(-1,   1))
    

if __name__=="__main__":
    app.run(debug=True)