import pickle
from flask import Flask, request, json, jsonify
import numpy as np

app = Flask(__name__)

# Load the saved model
filename = 'diabetes.sav'
loaded_model = pickle.load(open(filename, 'rb'))

@app.route('/diabetes/v1/predict', methods=['POST'])
def predict():
    try:
        # Get the features from the client
        features = request.json

        # Ensure that the features are converted to numeric values
        glucose = float(features["Glucose"])  # Convert Glucose to float
        bmi = float(features["BMI"])  # Convert BMI to float
        age = float(features["Age"])  # Convert Age to float
        
        # Create the features list for prediction
        features_list = [glucose, bmi, age]

        # Get the prediction class
        prediction = loaded_model.predict([features_list])

        # Get the prediction probabilities
        confidence = loaded_model.predict_proba([features_list])

        # Formulate the response to return to the client
        response = {}
        response['prediction'] = int(prediction[0])
        response['confidence'] = str(round(np.amax(confidence[0]) * 100 , 2))
        
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
