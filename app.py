import joblib
from flask import Flask, request, app, jsonify, url_for, render_template
import tensorflow
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

app=Flask(__name__)

## Load model
model = joblib.load('model.keras')
scaler = joblib.load('scaling.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data = request.json['X']
    print(data)
    print(np.array(data).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data[:5]()))).reshape(1,-1)
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ =="__main__":
    app.run(debug=True)
    
    


