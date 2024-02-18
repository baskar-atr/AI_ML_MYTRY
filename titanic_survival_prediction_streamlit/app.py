import streamlit as st
from utils import PrepProcesor, columns
import numpy as np
import pandas as pd

import joblib

model = joblib.load("xgbpipe.joblib")

st.title('Did the survive? :ship:')
PassengerId = st.text_input('Input passenger Id', 123456)
Pclass = st.selectbox('Choose class', [1, 2, 3])
Name = st.text_input('Input Passenger Name', 'John Smith')
Sex = st.selectbox('Select your sex', ['Male', 'Female'])
age = st.slider('Choose your age', 0, 100)
SibSp = st.slider('chose Siblings', 0, 10)
Parch = st.slider('Chose Parch', 0, 2)
Ticket = st.text_input('Input Ticket Number', 12345)
Fare = st.number_input('Input Fare:', 0, 1000)
Cabin = st.text_input('Input Cabin Name', 'C52')
Embarked = st.select_slider('Did teh EMbrak?', ['S', 'C', 'Q'])

#columns = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']


def predict():
    row = np.array([PassengerId, Pclass, Name, Sex, age, SibSp, Parch, Ticket, Fare, Cabin, Embarked])
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)
    if prediction[0] == 1:
        msg = Name +' Survived'
        st.success(msg)
    else:
        msg = Name +' Not Survived'
        st.error(msg)
trigger = st.button('Predict', on_click=predict)
