# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:29:30 2023

@author: Admin
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Admin/Pictures/MASTERS/ARTIFICIAL INTELLIGENCE\FINAL PROJECT/trained_model.sav', 'rb'))

#Creating a function for prediction
def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    # Giving the title
    st.title('DiabetesPrediction Web Application for Kenyatta National Hospital')
       
        # Getting the Input Data from the user
        
Pregnancies = st.text_input('Enter The Number of Pregnancies')
Glucose = st.text_input('Glucose level')
BloodPressure = st.text_input('Enter Blood Pressure Levels')
SkinThickness = st.text_input('Enter Skin Thickness Level')
Insulin = st.text_input('Enter Insulin Level')
BMI = st.text_input('Enter BMI')
DiabetesPedigreeFunction = st.text_input(' Diabetes Pedigree Level')
Age = st.text_input('Age of the person')

#Code for prediction
diagnosis=''
#Creating a button for prediction
if st.button('Diabetes Test Results'):
    diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
if __name__ == 'main':
    main()

            
    