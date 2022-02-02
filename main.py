from tkinter import *
import tkinter as tk
import numpy as np
import math
import matplotlib
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import re
import scipy
from scipy.optimize import fmin


def createNewWindow():
    functionWindow = tk.Toplevel(main_calc)
    input_func = StringVar()
    input_constraint_min = StringVar()
    input_constraint_max = StringVar()

    func_min = ''

    input_frame = Frame(functionWindow, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                        highlightthickness=1)
    input_frame.pack(side=TOP)
    function = ''
    input_field1 = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_func, width=50, bg="#eee", bd=0,
                         justify=RIGHT)
    input_field1.grid(row=0, column=0)
    input_field1.pack(ipady=10)

    btns_frame2 = Frame(functionWindow, width=312, height=272.5, bg="grey")
    btns_frame2.pack()

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=functionWindow)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, functionWindow)

    button_drawfx = Button(btns_frame2, image=imgFx, width=310, height=51, bd=0, bg="grey", activebackground="grey",
                           cursor="hand2", command=lambda: [
            btn_drawfx(input_func, canvas, toolbar, fig, functionWindow, function)]).grid(row=2, column=0, columnspan=4,
                                                                                          padx=1, pady=1)

    button_drawfx = Button(btns_frame2, image=imgFx, width=310, height=51, bd=0, bg="grey", activebackground="grey",
                           cursor="hand2", command=lambda: [
            btn_drawfx(input_func, canvas, toolbar, fig, functionWindow, function)]).grid(row=2, column=0, columnspan=4,
                                                                                          padx=1, pady=1)


def createTrigonometryWindow():
    functionWindow = tk.Toplevel(main_calc)
    input_v = StringVar()

    btns_frame_tri = Frame(functionWindow, width=312, height=272.5, bg="grey")
    btns_frame_tri.pack()

    button_sin = Button(btns_frame_tri, image=imgSin, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                        cursor="hand2", command=lambda: sin(input_text)).grid(row=0, column=0, columnspan=1, padx=1,
                                                                              pady=1)

    button_cos = Button(btns_frame_tri, image=imgCos, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                        cursor="hand2", command=lambda: cos(input_text)).grid(row=0, column=1, columnspan=1, padx=1,
                                                                              pady=1)

    button_tg = Button(btns_frame_tri, image=imgTg, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                       cursor="hand2", command=lambda: tg(input_text)).grid(row=1, column=0, columnspan=1, padx=1,
                                                                            pady=1)

    button_ctg = Button(btns_frame_tri, image=imgCtg, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                        cursor="hand2", command=lambda: ctg(input_text)).grid(row=1, column=1, columnspan=1, padx=1,
                                                                              pady=1)


def getNumbers(str):
    array = [int(d) for d in re.findall(r'-?\d+', str)]
    return array


def find_min(input_func, x1):
    function = input_func
    rsplit = ""
    split = ""

    if (';' in str(input_func)):
        split = function.split(";")
    if ('=' in split[1]):
        rsplit = function.split("=")
    else:
        rsplit = split[1]

    numbers = getNumbers(split[1])
    min = numbers[0]
    max = numbers[1]

    print(string2func(split[0]))
    if ('min' in split[1]):
        xmin_local = scipy.optimize.minimize(string2func(split[0]), x0=[(-10.1)], bounds=[(int(min), int(max))])
        opt = float(xmin_local.fun[0])
    if ('max' in split[1]):
        xmin_local = (
            scipy.optimize.minimize((string2func("-(" + split[0] + ")")), x0=[(0.1)], bounds=[(int(min), int(max))]))
        opt = -1 * float(xmin_local.fun[0])

    print('xmin', opt)
    return (opt)
    #    x^2;min(2,3)
    # x^2;max(0,1)


def btn_drawfx(input_func, canvas, toolbar, fig, functionWindow, function):
    function = input_func.get()
    if ("=" in function):
        temp_split = function.split(" =")
        function = temp_split[0]
    function2 = str(function)

    split = function.split(";")
    function1 = split[0]

    try:
        func = string2func(function1)
    except:
        print("Error")
    x = np.arange(-10, 10, .01)
    fig.clear()
    try:
        fig.add_subplot(111).plot(x, func(x))
    except:
        print("ERROR")
    canvas.draw_idle()
    toolbar.update()
    if ('min' in function):
        xmin_local1 = find_min(function, x)
    if ('max' in function):
        xmin_local1 = find_min(function, x)

    try:
        input_func.set(function2 + " = " + str(round(xmin_local1,3)))
    except:
        print("error")

def two_x(input_v):
    global expression
    v = input_v.get()
    n = 2 ** (float(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def ten_x(input_v):
    global expression
    v = input_v.get()
    n = 10 ** (float(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def floor(input_v):
    global expression
    v = input_v.get()
    n = math.floor(float(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def ceil(input_v):
    global expression
    v = input_v.get()
    n = math.ceil(float(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def log10(input_v):
    global expression
    v = input_v.get()
    n = math.log10(float(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def ln(input_v):
    global expression
    v = input_v.get()
    n = math.log(float(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def factorial(input_v):
    global expression
    v = input_v.get()
    n = scipy.math.factorial(int(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def square_root(input_v):
    global expression
    v = input_v.get()
    n = math.sqrt(float(v))
    input_text.set(str(n))
    expression = str(n)
    return ''


def sin(input_v):
    global expression
    v = input_v.get()
    r = math.sin(math.radians(float(v)))
    input_text.set(str(r))
    expression = str(r)


def cos(input_v):
    global expression
    v = input_v.get()
    r = math.cos(math.radians(float(v)))
    input_text.set(str(r))
    expression = str(r)


def tg(input_v):
    global expression
    v = input_v.get()
    r = math.tan(math.radians(float(v)))
    input_text.set(str(r))
    expression = str(r)


def ctg(input_v):
    global expression
    v = input_v.get()
    r = 1 / math.tan(math.radians(float(v)))
    input_text.set(str(r))
    expression = str(r)


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set("")


def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)

    except:
        input_text.set("Invalid syntax")
        result = ""
    expression = result


replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
]


def string2func(string):
    ''' evaluates the string and returns a function of x '''
    # find all words and check if all are allowed:

    for word in re.findall('[a-zA-Z_]+', string):
        if word not in allowed_words:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func


expression = ""

main_calc = Tk()
main_calc.geometry("316x606")
main_calc.resizable(0, 0)
main_calc.title("Calc")
function_min = StringVar()

input_text = StringVar()
input_frame = Frame(main_calc, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(main_calc, width=312, height=323.5, bg="grey")
btns_frame.pack()

img0 = PhotoImage(file="images/Button0.png")
img1 = PhotoImage(file="images/Button1.png")
img2 = PhotoImage(file="images/Button2.png")
img3 = PhotoImage(file="images/Button3.png")
img4 = PhotoImage(file="images/Button4.png")
img5 = PhotoImage(file="images/Button5.png")
img6 = PhotoImage(file="images/Button6.png")
img7 = PhotoImage(file="images/Button7.png")
img8 = PhotoImage(file="images/Button8.png")
img9 = PhotoImage(file="images/Button9.png")
imgDot = PhotoImage(file="images/ButtonDot.png")
imgPlus = PhotoImage(file="images/ButtonPlus.png")
imgMinus = PhotoImage(file="images/ButtonMinus.png")
imgMulti = PhotoImage(file="images/ButtonMulti.png")
imgDivision = PhotoImage(file="images/ButtonDivision.png")
imgExpo = PhotoImage(file="images/ButtonExpo.png")
imgMod = PhotoImage(file="images/ButtonMod.png")
imgClear = PhotoImage(file="images/ButtonClear.png")
imgEqual = PhotoImage(file="images/ButtonEqual.png")
imgFx = PhotoImage(file="images/ButtonFx.png")
imgTrigonometry = PhotoImage(file="images/ButtonTrigonometry.png")
imgSin = PhotoImage(file="images/ButtonSin.png")
imgCos = PhotoImage(file="images/ButtonCos.png")
imgTg = PhotoImage(file="images/ButtonTg.png")
imgCtg = PhotoImage(file="images/ButtonCtg.png")
imgPi = PhotoImage(file="images/ButtonPi.png")
imgE = PhotoImage(file="images/ButtonE.png")
imgFactorial = PhotoImage(file="images/ButtonFactorial.png")
imgSquare_root = PhotoImage(file="images/ButtonSquareRoot.png")
imgLog10 = PhotoImage(file="images/ButtonLog10.png")
imgLn = PhotoImage(file="images/ButtonLn.png")
imgFloor = PhotoImage(file="images/Floor.png")
imgCeil = PhotoImage(file="images/Ceil.png")
imgTwo_x = PhotoImage(file="images/Two_x.png")
imgTen_x = PhotoImage(file="images/Ten_x.png")

clear = Button(btns_frame, image=imgClear, width=233, height=53, bd=0, bg="grey", activebackground="grey",
               cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, image=imgDivision, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

button_one = Button(btns_frame, image=img1, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                    cursor="hand2", command=lambda: btn_click("1")).grid(row=1, column=0, padx=1, pady=1)
button_two = Button(btns_frame, image=img2, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                    cursor="hand2", command=lambda: btn_click("2")).grid(row=1, column=1, padx=1, pady=1)
button_three = Button(btns_frame, image=img3, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click("3")).grid(row=1, column=2, padx=1, pady=1)
button_plus = Button(btns_frame, image=imgPlus, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                     cursor="hand2", command=lambda: btn_click("+")).grid(row=1, column=3, padx=1, pady=1)

button_four = Button(btns_frame, image=img4, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                     cursor="hand2", command=lambda: btn_click("4")).grid(row=2, column=0, padx=1, pady=1)
button_five = Button(btns_frame, image=img5, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                     cursor="hand2", command=lambda: btn_click("5")).grid(row=2, column=1, padx=1, pady=1)
button_six = Button(btns_frame, image=img6, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                    cursor="hand2", command=lambda: btn_click("6")).grid(row=2, column=2, padx=1, pady=1)
button_minus = Button(btns_frame, image=imgMinus, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

button_seven = Button(btns_frame, image=img7, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click("7")).grid(row=3, column=0, padx=1, pady=1)
button_eight = Button(btns_frame, image=img8, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click("8")).grid(row=3, column=1, padx=1, pady=1)
button_nine = Button(btns_frame, image=img9, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                     cursor="hand2", command=lambda: btn_click("9")).grid(row=3, column=2, padx=1, pady=1)
button_multiply = Button(btns_frame, image=imgMulti, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                         cursor="hand2", command=lambda: btn_click("*")).grid(row=3, column=3, padx=1, pady=1)

button_zero = Button(btns_frame, image=img0, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                     cursor="hand2", command=lambda: btn_click("0")).grid(row=4, column=0, padx=1, pady=1)
button_dot = Button(btns_frame, image=imgDot, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                    cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=1, padx=1, pady=1)
button_exp = Button(btns_frame, image=imgExpo, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                    cursor="hand2", command=lambda: btn_click("**")).grid(row=4, column=2, padx=1, pady=1)
button_modulo = Button(btns_frame, image=imgMod, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                       cursor="hand2", command=lambda: btn_click("%")).grid(row=4, column=3, padx=1, pady=1)

button_pi = Button(btns_frame, image=imgPi, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                   cursor="hand2", command=lambda: btn_click(math.pi)).grid(row=5, column=0, padx=1, pady=1)

button_e = Button(btns_frame, image=imgE, width=75, height=51, bd=0, bg="grey", activebackground="grey", cursor="hand2",
                  command=lambda: btn_click(math.e)).grid(row=5, column=1, padx=1, pady=1)

button_factorial = Button(btns_frame, image=imgFactorial, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                          cursor="hand2", command=lambda: btn_click(factorial(input_text))).grid(row=5, column=2,
                                                                                                 padx=1, pady=1)

button_square_root = Button(btns_frame, image=imgSquare_root, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                       cursor="hand2", command=lambda: btn_click(square_root(input_text))).grid(row=5, column=3, padx=1,
                                                                                           pady=1)

button_two_x = Button(btns_frame, image=imgTwo_x, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click(two_x(input_text))).grid(row=6, column=0, padx=1,
                                                                                         pady=1)
button_ten_x = Button(btns_frame, image=imgTen_x, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click(ten_x(input_text))).grid(row=6, column=1, padx=1,
                                                                                         pady=1)
button_floor = Button(btns_frame, image=imgFloor, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click(floor(input_text))).grid(row=6, column=2, padx=1,
                                                                                         pady=1)
button_ceil = Button(btns_frame, image=imgCeil, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                     cursor="hand2", command=lambda: btn_click(ceil(input_text))).grid(row=6, column=3, padx=1, pady=1)

buttonTrigonometry = tk.Button(btns_frame, image=imgTrigonometry, width=152, height=53, bd=0, bg="grey",
                               activebackground="grey", cursor="hand2",
                               text="Create trigonometry window",
                               command=createTrigonometryWindow).grid(row=7, column=0, columnspan=2, padx=1, pady=1)

button_log10 = Button(btns_frame, image=imgLog10, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                      cursor="hand2", command=lambda: btn_click(log10(input_text))).grid(row=7, column=2, padx=1,
                                                                                         pady=1)

button_ln = Button(btns_frame, image=imgLn, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                   cursor="hand2", command=lambda: btn_click(ln(input_text))).grid(row=7, column=3, padx=1, pady=1)

button_equals = Button(btns_frame, image=imgEqual, width=310, height=51, bd=0, bg="grey", activebackground="grey",
                       cursor="hand2", command=lambda: btn_equal()).grid(row=8, column=0, columnspan=4, padx=1, pady=1)

buttonExample = tk.Button(btns_frame, image=imgFx, width=310, height=51, bd=0, bg="grey", activebackground="grey",
                          cursor="hand2",
                          text="Create new window",
                          command=createNewWindow).grid(row=9, column=0, columnspan=4, padx=1, pady=1)

main_calc.mainloop()
