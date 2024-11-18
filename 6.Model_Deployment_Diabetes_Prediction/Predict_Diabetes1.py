import json
import requests

def predict_diabetes():
    # Get user inputs
    try:
        BMI = float(input("BMI? "))
        Age = float(input("Age? "))
        Glucose = float(input("Glucose? "))
    except ValueError:
        print("Please enter numeric values for BMI, Age, and Glucose.")
        return

    # Prepare the data to send
    data = {"BMI": BMI, "Age": Age, "Glucose": Glucose}
    url = 'http://127.0.0.1:5000/diabetes/v1/predict'

    # Send the POST request with the data
    response = requests.post(url, json=data)

    # Parse the response
    if response.status_code == 200:
        result = response.json()
        print("Prediction: " + ("Diabetic" if result["prediction"] == 1 else "Not Diabetic"))
        print("Confidence: " + result["confidence"] + "%")
    else:
        try:
            error_message = response.json().get("error", "Unknown error")
            print("Error: " + error_message)
        except json.JSONDecodeError:
            print("Error: Unable to parse response from the server.")

if __name__ == "__main__":
    predict_diabetes()
