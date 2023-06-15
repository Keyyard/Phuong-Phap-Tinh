import numpy as np
import matplotlib.pyplot as plt
import math
import PySimpleGUI as sg

layout = [
    [sg.Text("Nhap it nhat 2 gia tri x: ")],
    [sg.Input(key="x")],
    [sg.Text("Nhap it nhat 2 gia tri y: ")],
    [sg.Input(key="y")],
    [sg.Button("RUN",key="run")],
    [sg.Text("a = ",key="a")],
    [sg.Text("b = ",key="b")],
    [sg.Text("c = ",key="c")],
    [sg.Text("y = ",key="y_result")],
    [sg.Text(text="by Trinh Minh Hieu - 11222359",justification="right",size=(50,0),font=("Arial",8))]

]

window = sg.Window("PPT: Binh Phuong Toi Thieu",layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "stop":
        break
    if event == "run":
        x_data = np.array([float(x) for x in values["x"].split()])
        y_data = np.array([float(x) for x in values["y"].split()])
        A = np.vstack([x_data**2, x_data, np.ones(len(x_data))]).T
        a, b, c = np.linalg.lstsq(A, y_data, rcond=None)[0]
        a = round(a,4)
        b = round(b,4)
        c= round(c,4)
        y_result = "y = {c} + {b}x + {a}x**2".format(c=c,b=b,a=a)
        window["a"].update("a = " + str(a))
        window["b"].update("b = " + str(b))
        window["c"].update("c = " + str(c))
        window["y_result"].update(y_result)