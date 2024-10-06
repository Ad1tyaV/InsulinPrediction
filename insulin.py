import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def getModel():
    return joblib.load('./InsulinPredictor.pkl')

model = getModel()

def predict(age,weight,glucose,car,time,e,rate):

    pred = model.predict([np.array([age,weight,glucose,car,e,int(time=='Evening'),int(time=='Morning')])])

    t = round(abs(pred[0])/rate,2)

    return pred,t


age = st.number_input(label="Age",value=0)

weight = st.number_input(label="Weight",value=0)


glucose = st.number_input(label="Glucose",value=0)


car = st.number_input(label="Carbohydrate Intake",value=0)


time= st.selectbox( label='Time of the day', options=['Morning','Afternoon','Evening'])

e = st.number_input(label="Exercise",value=0)

rate = st.number_input(label='Flow Rate', value=0)

submit = st.button(label='Predict')

if submit:

    pred, t = predict(age,weight,glucose,car,time,e,rate)

    message = st.chat_message("ai")
    message.markdown(f'**Insulin Dosage**: {pred[0]} units')
    message.markdown(f'\n\n**Time**: {t} seconds')

