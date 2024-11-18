import pickle
from flask import Flask, request, jsonify, render_template_string
import numpy as np

app = Flask(__name__)

#---the filename of the saved model---
filename = 'diabetes.sav'

#---load the saved model---
loaded_model = pickle.load(open(filename, 'rb'))

# HTML template for the form
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Diabetes Prediction</title>
</head>
<body>
    <h1>Diabetes Prediction</h1>
    <form action="/diabetes/v1/predict_form" method="post">
        <label for="BMI">BMI:</label>
        <input type="text" id="BMI" name="BMI" required><br><br>
        <label for="Age">Age:</label>
        <input type="text" id="Age" name="Age" required><br><br>
        <label for="Glucose">Glucose:</label>
        <input type="text" id="Glucose" name="Glucose" required><br><br>
        <button type="submit">Predict</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    # Render the HTML form
    return HTML_FORM

@app.route('/diabetes/v1/predict_form', methods=['POST'])
def predict_form():
    try:
        # Get form data from the user
        BMI = request.form.get("BMI")
        Age = request.form.get("Age")
        Glucose = request.form.get("Glucose")

        # Convert inputs to float
        features_list = [float(Glucose), float(BMI), float(Age)]

        # Make predictions using the model
        prediction = loaded_model.predict([features_list])
        confidence = loaded_model.predict_proba([features_list])

        # Prepare the response
        response = f"""
        <h1>Prediction Results</h1>
        <p><strong>Prediction:</strong> {"Diabetic" if prediction[0] == 1 else "Not Diabetic"}</p>
        <p><strong>Confidence:</strong> {round(np.amax(confidence[0]) * 100, 2)}%</p>
        <br>
        <a href="/">Go back to the form</a>
        """
        return response

    except ValueError:
        return "<h1>Error: Please enter valid numeric values for BMI, Age, and Glucose</h1><br><a href='/'>Go back to the form</a>", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
