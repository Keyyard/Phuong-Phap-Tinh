import numpy as np
import matplotlib.pyplot as plt
import math
import PySimpleGUI as sg

def f(x):
    return x**3 + x - 5
layout = [
    [sg.Text("Nhap a: ")],
    [sg.Input(key="a",default_text="1")],
    [sg.Text("Nhap b:")],
    [sg.Input(key="b",default_text="2")],
    #choose between Epsi and Steps
    #[sg.Text("Nhap So Buoc:"),sg.Input(key="steps",default_text="10",size=(30,10),expand_x=True)]
    #[sg.Text("Nhap Epsi:"),sg.Input(key="epsi",default_text="0.00001",size=(30,10),expand_x=True)],
    [sg.Combo(["Epsi","Steps"],key="choose",default_value="Epsi",size=(10,10),enable_events=True)],
    [sg.Text("Nhap Epsi:",visible=True,key="epsi_text"),sg.Input(key="epsi",default_text="0.00001",size=(30,10),expand_x=True,visible=True)],
    [sg.Text("Nhap So Buoc:",visible=False,key="steps_text"),sg.Input(key="steps",default_text="10",size=(30,10),expand_x=True,visible=False)],
    [sg.Button("RUN",key="run")],
    [sg.Text(key="result")],
    [sg.Text(text="by Trinh Minh Hieu - 11222359",justification="right",size=(50,0),font=("Arial",8))]
]
window = sg.Window("PPT: Day Cung",layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    a = round(float(values["a"]),2)
    b = round(float(values["b"]),2)
    if f(a) * f(b) > 0:
        result = "Khong co nghiem trong khoang nay"
        window["result"].update(result)
        continue
    if values["choose"] == "Steps":
        window["steps_text"].update(visible=True)
        window["epsi_text"].update(visible=False)
        window["steps"].update(visible=True)
        window["epsi"].update(visible=False)
        steps = int(values["steps"])
        print (steps)
        if event == "run":
            x = a - (b - a) * f(a) / (f(b) - f(a))
            if f(x) * f(a) < 0:
                for i in range(steps):
                    b = x
                    x = a - (b - a) * f(a) / (f(b) - f(a))
                    #print(a, b, x, f(x))
            else:
                for i in range(steps):
                    a = x
                    x = a - (b - a) * f(a) / (f(b) - f(a))
                    #print(a, b, x, f(x))
                print (x)
                result = "x = " + str(x)
                window["result"].update(result)
    if values["choose"] == "Epsi":
        window["steps_text"].update(visible=False)
        window["epsi_text"].update(visible=True)
        window["steps"].update(visible=False)
        window["epsi"].update(visible=True)
        epsi = float(values["epsi"])
        print (epsi)
        if event == "run":
            x = a - (b - a) * f(a) / (f(b) - f(a))
            if f(x) * f(a) < 0:
                while abs(x - b) > epsi:
                    b = x
                    x = a - (b - a) * f(a) / (f(b) - f(a))
                    #print(a, b, x, f(x))
            else:
                while abs(x - a) > epsi:
                    a = x
                    x = a - (b - a) * f(a) / (f(b) - f(a))
                    #print(a, b, x, f(x))
                print (x)
                result = "x = " + str(x)
                window["result"].update(result)

