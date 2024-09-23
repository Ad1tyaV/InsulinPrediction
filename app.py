import ttkbootstrap as ttk
import tkinter as tk
from tkinter import Tk
import numpy as np
import joblib

model = joblib.load('./InsulinPredictor.pkl')

daytime = {'Morning':0,'Evening':1}

def predict():

    pred = model.predict([np.array([int(age.get()),int(weight.get()),int(glucose.get()),int(car.get()),int(time.get()=='Morning'),int(time.get()=='Evening'),int(e.get())])])
    insulin.config(text=round(abs(pred[0]),2))
    insulin.update()

    flow.config(text=round(abs(pred[0])/int(rate.get()),2))
    flow.update()

root = ttk.Window(title="News Headline Tagger")

root.geometry('640x640')

age_frame = ttk.Labelframe(root, text='Age')
age_frame.place(x=50, y=100)
age = ttk.Entry(age_frame, font=('Helvetica', 14), width=10)
age.pack(padx=5, pady=5)

weight_frame = ttk.Labelframe(root, text='Weight')
weight_frame.place(x=250, y=100)
weight = ttk.Entry(weight_frame, font=('Helvetica', 14), width=10)
weight.pack(padx=5, pady=5)

glucose_frame = ttk.Labelframe(root, text='Glucose level')
glucose_frame.place(x=50, y=200)
glucose = ttk.Entry(glucose_frame, font=('Helvetica', 14), width=10)
glucose.pack(padx=5, pady=5)

car_frame = ttk.Labelframe(root, text='Carbohydrate intake')
car_frame.place(x=250, y=200)
car = ttk.Entry(car_frame, font=('Helvetica', 14), width=10)
car.pack(padx=5, pady=5)

time_frame = ttk.Labelframe(root, text='Time of the day')
time_frame.place(x=50, y=300)
time= ttk.Combobox(time_frame, font=('Helvetica', 14), width=10, values=['Morning','Afternoon','Evening'])
time.pack(padx=5, pady=5)

e_frame = ttk.Labelframe(root, text='Exercise')
e_frame.place(x=250, y=300)
e = ttk.Entry(e_frame, font=('Helvetica', 14), width=10)
e.pack(padx=5, pady=5)

rate_frame = ttk.Labelframe(root, text='Flow rate')
rate_frame.place(x=50, y=400)
rate = ttk.Entry(rate_frame, font=('Helvetica', 14), width=10)
rate.pack(padx=5, pady=5)

submit = ttk.Button(text="Predict", style='primary', command=predict)
submit.place(x=250, y=400)

insulin_frame = ttk.Labelframe(root, text='Insulin Dosage')
insulin_frame.place(x=50, y=500)
insulin = ttk.Label(insulin_frame, font=('Helvetica', 24), width=10)
insulin.pack(padx=5, pady=5)

flow_frame = ttk.Labelframe(root, text='Time')
flow_frame.place(x=250, y=500)
flow = ttk.Label(flow_frame, font=('Helvetica', 24), width=10)
flow.pack(padx=5, pady=5)

root.mainloop()