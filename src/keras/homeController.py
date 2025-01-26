import pandas as pd
import joblib
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# 1. Load the model, scaler, and column names (for prediction)
def load_model_and_scaler():
    model = load_model('model.keras')  # Load the Keras model
    scaler = joblib.load('scaler.pkl')  # Load the saved scaler
    columns = joblib.load('columns.pkl')  # Load the saved column names
    return model, scaler, columns

# 2. Define API route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request (JSON format)
        data = request.get_json()

        # Convert the incoming JSON data to a DataFrame-like structure
        input_data = pd.DataFrame([data])

        # Perform the same preprocessing (feature scaling and encoding) as the training data
        input_data_encoded = pd.get_dummies(input_data, drop_first=True)

        # Ensure that the input data has the same columns as the training data
        # Fill missing columns with 0 (columns that were not in the input)
        input_data_encoded = input_data_encoded.reindex(columns=columns, fill_value=0)

        # Perform feature scaling using the loaded scaler
        input_data_scaled = scaler.transform(input_data_encoded)

        # Get prediction from the model
        prediction = model.predict(input_data_scaled)

        # Return prediction as 'yes' or 'no' based on threshold (0.5)
        result = 'yes' if prediction[0] > 0.5 else 'no'

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Load the model, scaler, and columns
    model, scaler, columns = load_model_and_scaler()

    # Start the Flask API
    app.run(debug=True)
