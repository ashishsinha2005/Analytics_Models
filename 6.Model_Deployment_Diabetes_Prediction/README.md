
# Diabetes-Prediction-With-Deployment

This project focuses on predicting diabetes using machine learning techniques. The model predicts whether a person is diabetic or non-diabetic based on various input features. The project includes both Flask and Streamlit implementations for different deployment options.







## Clone and Run the Project
Follow these steps to clone and run the project locally:

## 1. Clone the Repository
git clone https://github.com/ashishsinha2005/Analytics_Models/tree/master/6.Model_Deployment_Diabetes_Prediction.git

## Explanation of the process
A good way to deploy your machine learning model is to build a REST 
(REpresentational State Transfer) API, so that the model is accessible by others who 
may not be familiar with how machine learning works. Using REST, you can 
build multi-platform front-end applications (such as iOS, Android, Windows, 
and so forth) and pass the data to the model for processing. The result can then 
be returned back to the application.

## 1. Run the Model 
- run the Jupyter source file- Models91
- It contains all the steps mentioned in "Steps in Model Building"

## Model Explanation
predict the likelihood of a person being diagnosed with diabetes based on several diagnostic measurements of 
that person
 Its features consist of the following:
- Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration after 2 hours in an oral glucose tolerance test
- BloodPressure: Diastolic blood pressure (mm Hg)
- SkinThickness: Triceps skin fold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age (years)
- Outcome: 0 (non-diabetic) or 1 (diabetic)

## Steps in Model Building
-  Loading the Data
-  Cleaning the Data
- Examining the Correlation Between the Features
- Plotting the Correlation Between Features
- Evaluating the Algorithms
- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machines
- Selecting the Best Performing Algorithm
- Training and Saving the Model
- Deploying the Model

## Deploying the Model
- Install Flask apppython app.py
- Create create a text file named REST_API.py

## Testing the Model
Run python REST_API.py to check Flask App up and Running

## Creating the Client Application to Use the Model
Run with full code
python REST_API.py
run the application in Terminal and give input

## To get Output in URL
use following code
- python REST_API1.py (no need to run Predict_Diabetes1.py)
- Open your browser: Navigate to the URL: and enter your server address and give input and Run

  ![Image Alt](https://github.com/ashishsinha2005/Analytics_Models/blob/7b2b3db5f17cffb3b3f33a5d8375dc125e952d83/6.Model_Deployment_Diabetes_Prediction/Diab3.jpg)



## Feedback

If you have any feedback, please reach out to me at ashishsep2011@gmail.com

