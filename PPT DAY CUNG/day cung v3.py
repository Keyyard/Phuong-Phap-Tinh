import PySimpleGUI as sg

def secant_method(equation, x0, x1, epsilon=None, num_steps=None):
 
    #def f(x):
        #return eval(equation, {'x': x}) #sử dụng hàm eval để tính toán giá trị của hàm f(x) với x thay thế bằng x giá trị truyền vào
    
    f = lambda x: eval(equation, {'x': x})  #sử dụng hàm lambda để viết gọn hàm f(x)

    x_values = [] 

    if epsilon is not None: #nếu epsilon được chọn
        while True:
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            x_values.append(x2)
            if abs(x2 - x1) < epsilon:
                return x2
            x0, x1 = x1, x2

    if num_steps is not None: #nếu số bước được chọn
        for _ in range(num_steps):
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            x_values.append(x2)
            x0, x1 = x1, x2

        return x_values

layout = [
    [sg.Text('Phương trình:'), sg.InputText(key='equation', size=(30, 1),expand_x=True)],
    [sg.Text('Giá trị ban đầu x0:'), sg.InputText(key='x0', size=(6, 1))],
    [sg.Text('Giá trị ban đầu x1:'), sg.InputText(key='x1', size=(6, 1))],
    [sg.Text('Lựa chọn:'), sg.Combo(['Epsilon', 'Số bước'], default_value='Epsilon', key='option')],
    [sg.Text('Nhập Epsilon/Số bước:', key='param_text'), sg.InputText(key='param_value',size=(15, 1))],
    [sg.Button('Tính')],
    [sg.Output(size=(50, 10))],
    [sg.Text(text="by Trinh Minh Hieu - 11222359",justification="right",size=(50,0),expand_x=True,font=("Arial",8))]
]

window = sg.Window('Phương pháp dây cung', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Tính': 
        equation = values['equation']
        x0 = float(values['x0'])
        x1 = float(values['x1'])
        option = values['option']
        param_value = float(values['param_value']) if values['param_value'] else None #parametter value = giá trị của epsilon hoặc số bước
        epsilon = param_value if option == 'Epsilon' else None #epsilon = giá trị của epsilon nếu lựa chọn là epsilon
        num_steps = int(param_value) if option == 'Số bước' else None #num_steps = giá trị của số bước nếu lựa chọn là số bước

        results = secant_method(equation, x0, x1, epsilon, num_steps)
        if num_steps is not None: #nếu số bước được chọn
            print ("===========================")
            for i, x in enumerate(results): #enumerate kiểu range() nhưng dạng map/dict trong python, ở đây là (0, x0), (1, x1), (2, x2)
                print(f'Bước {i+1}: x = {x}')
            print ("===========================")
        else: #nếu epsilon được chọn
            print ("===========================")
            print(f'x = {results}') #in ra kết quả cuối
            print ("===========================")

window.close()
