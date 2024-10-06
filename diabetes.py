import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def get_model():

    return joblib.load('diabetes.pkl')

model = get_model()

preg = st.number_input(label='Pregnancies',value=0)
glucose = st.number_input(label='Glucose',value=0)
bp = st.number_input(label='Blood Pressure',value=0)
skin_thick = st.number_input(label='Skin Thickness',value=0)
insulin = st.number_input(label='Insulin',value=0)
bmi = st.number_input(label='BMI',value=0.0,step=0.1)
age = st.number_input(label='Age',value=0)

btn = st.button(label='Predict')

if btn:

    pred = model.predict([np.array([preg,glucose,bp,skin_thick,insulin,bmi,age])])
    if(pred[0] == 1):
        st.write('Diabetic')
    else:
        st.write('Not Diabetic')