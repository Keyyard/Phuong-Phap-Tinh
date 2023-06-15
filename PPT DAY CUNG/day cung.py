import numpy as np
import matplotlib.pyplot as plt
import math
import PySimpleGUI as sg

def f(x):
    return x**3 + x - 5
layout = [
    [sg.Text("Nhap a: ")],
    [sg.Input(key="a")],
    [sg.Text("Nhap b:")],
    [sg.Input(key="b")],
    [sg.Text("Nhap Epsi:"),sg.Input(key="epsi",default_text="0.00001",size=(30,10),expand_x=True)],
    [sg.Button("RUN",key="run")],
    [sg.Text(key="result")],
    [sg.Text(text="by Trinh Minh Hieu - 11222359",justification="right",size=(50,0),font=("Arial",8))]
]
window = sg.Window("PPT: Day Cung",layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "run":
        a = round(float(values["a"]),2)
        b = round(float(values["b"]),2)
        if f(a) * f(b) > 0:
            result = "Khong co nghiem trong khoang nay"
            window["result"].update(result)
            continue
        epsi = float(values["epsi"])
        print (epsi)
        print (a,b)
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

