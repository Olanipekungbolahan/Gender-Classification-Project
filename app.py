from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from joblib import load

app = Flask(__name__)

# Load the trained RandomForestClassifier model
rf_model = load('best_rf_model.pkl')

# Dummy function to simulate preprocessing and feature engineering
def preprocess_data(input_data):
    # For demonstration, just return the input data as is
    return input_data

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json  # Assuming JSON data is sent
    
    # Preprocess the input data
    processed_data = preprocess_data(input_data)
    
    # Make prediction using the trained model
    prediction = rf_model.predict(processed_data)
    
    # Convert prediction to human-readable format (e.g., class labels)
    # For demonstration, just return the raw prediction as is
    prediction_result = str(prediction)
    
    # Return the prediction result as JSON
    return jsonify({'prediction': prediction_result})

if __name__ == '__main__':
    app.run(debug=True)
