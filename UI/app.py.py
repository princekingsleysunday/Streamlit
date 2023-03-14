# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 02:31:06 2023

@author: Kingsley
"""

#importing dependencies
import numpy as np
import pandas as pd
from joblib import load
import streamlit as st

# loading in the data(The dumped model)
model = load('../model/RF_model.joblib')


#Backend
def predictions(sepallength, sepalwidth, petallength, petalwidth):
    prediction = model.predict(np.array([[sepallength, sepalwidth, petallength, petalwidth]]))
    
    return prediction



# fuction to create the UI
def main():
    st.title('Iris flower model')
    
    
    

    sepallenth = st.text_input('Enter sepal length: ')
    sepalwidth = st.text_input('Enter sepal width: ')
    petallenth = st.text_input('Enter petal length: ')
    petalwidth = st.text_input('Enter petal width: ')
    
    
    button = st.button('predict')
    
    
    
    
    
if __name__ == '__main__':
    main()