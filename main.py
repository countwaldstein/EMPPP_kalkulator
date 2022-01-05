from tkinter import *
import tkinter as tk
import numpy as np
import math
import matplotlib
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import  re
import scipy
from scipy.optimize import fmin

def createNewWindow():
    functionWindow = tk.Toplevel(main_calc)
    input_func = StringVar()
    input_constraint_min = StringVar()
    input_constraint_max = StringVar()

    func_min =''

    input_frame = Frame(functionWindow, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    input_frame.pack(side = TOP)
    function = ''
    input_field1 = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_func, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
    input_field1.grid(row = 0, column = 0)
    input_field1.pack(ipady = 10)




    btns_frame2 = Frame(functionWindow, width=312, height=272.5, bg="grey")
    btns_frame2.pack()

    input_frame2 = Frame(functionWindow, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    input_frame2.pack(side = TOP)
    function = ''
    input_field2 = Entry(input_frame2, font = ('arial', 18, 'bold'), textvariable = input_constraint_min, width = 25, bg = "#eee", bd = 0, justify = RIGHT)
    input_field2.grid(row = 0, column = 1)
    input_field2.pack(ipady = 10)

    input_frame3 = Frame(functionWindow, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    input_frame3.pack(side = TOP)
    function = ''
    input_field3 = Entry(input_frame3, font = ('arial', 18, 'bold'), textvariable = input_constraint_max, width = 25, bg = "#eee", bd = 0, justify = RIGHT)
    input_field3.grid(row = 0, column = 1)
    input_field3.pack(ipady = 10)

    btns_frame3 = Frame(functionWindow, width=312, height=272.5, bg="grey")
    btns_frame3.pack()

    input_frame4 = Frame(functionWindow, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    input_frame4.pack(side = TOP)
    function = ''
    input_field4 = Entry(input_frame4, font = ('arial', 18, 'bold'), textvariable = function_min, width = 25, bg = "#eee", bd = 0, justify = RIGHT)
    input_field4.grid(row = 0, column = 1)
    input_field4.pack(ipady = 10)

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=functionWindow)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, functionWindow)




    button_drawfx = Button(btns_frame2, image = imgFx, width = 310, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda:[  btn_drawfx(input_func, canvas, toolbar, fig,  functionWindow, function)]).grid(row = 2, column = 0, columnspan = 4, padx = 1, pady = 1)
    button_find_min = Button(btns_frame3, image = imgFx, width = 310, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda:[ find_min(input_func,input_constraint_min,input_constraint_max)]).grid(row = 2, column = 0, columnspan = 4, padx = 1, pady = 1)





    button_drawfx = Button(btns_frame2, image = imgFx, width = 310, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda:[  btn_drawfx(input_func, canvas, toolbar, fig,  functionWindow, function)]).grid(row = 2, column = 0, columnspan = 4, padx = 1, pady = 1)




def createTrigonometryWindow():
    functionWindow = tk.Toplevel(main_calc)
    input_v = StringVar()

    btns_frame_tri = Frame(functionWindow, width=312, height=272.5, bg="grey")
    btns_frame_tri.pack()

    button_sin = Button(btns_frame_tri, image=imgSin, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                        cursor="hand2", command=lambda: sin(input_text)).grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 1)

    button_cos = Button(btns_frame_tri, image=imgCos, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                        cursor="hand2", command=lambda: cos(input_text)).grid(row = 0, column = 1, columnspan = 1, padx = 1, pady = 1)

    button_tg = Button(btns_frame_tri, image=imgTg, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                        cursor="hand2", command=lambda: tg(input_text)).grid(row=1, column=0, columnspan=1, padx=1,
                                                                                 pady=1)

    button_ctg = Button(btns_frame_tri, image=imgCtg, width=75, height=51, bd=0, bg="grey", activebackground="grey",
                        cursor="hand2", command=lambda: ctg(input_text)).grid(row=1, column=1, columnspan=1, padx=1,
                                                                                 pady=1)

def find_min(input_func,input_constraint_min,input_constraint_max):
    global function_min
    function = input_func.get()
    print(function)
    func = string2func(function)
    print(input_constraint_min.get(), input_constraint_max.get())
    xmin_local = scipy.optimize.fminbound(func, int(input_constraint_min.get()), int(input_constraint_max.get()))
    print( xmin_local)
    function_min.set(str(xmin_local))

    print(function_min)

def factorial(input_v):
    global expression
    v = input_v.get()
    n = scipy.math.factorial(int(v))
    input_text.set(str(n))
    expression = str(n)
    return ''

def square(input_v):
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
    r = 1/math.tan(math.radians(float(v)))
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

def btn_drawfx(input_func, canvas, toolbar, fig,  functionWindow, function):

    function = input_func.get()
    print(function)
    func = string2func(function)
    x = np.arange(-10, 10, .01)
    fig.clear()
    fig.add_subplot(111).plot(x, func(x))
    canvas.draw_idle()
    toolbar.update()


replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
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
main_calc.geometry("316x537")
main_calc.resizable(0, 0)
main_calc.title("Calc")
function_min = StringVar()


input_text = StringVar()
input_frame = Frame(main_calc, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(main_calc, width = 312, height = 323.5, bg = "grey")
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
#imgPi = PhotoImage(file="images/ButtonPi.png")
#imgE = PhotoImage(file="images/ButtonE.png")
#imgFactorial = PhotoImage(file="images/ButtonFactorial.png")
#imgSquare = PhotoImage(file="images/ButtonSquare.png")

clear = Button(btns_frame, image = imgClear, width = 233, height = 53, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, image = imgDivision, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

button_one = Button(btns_frame, image = img1, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("1")).grid(row = 1, column = 0,  padx = 1, pady = 1)
button_two = Button(btns_frame, image = img2, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("2")).grid(row = 1, column = 1,  padx = 1, pady = 1)
button_three = Button(btns_frame, image = img3, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("3")).grid(row = 1, column = 2, padx = 1, pady = 1)
button_plus = Button(btns_frame, image = imgPlus, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 1, column = 3, padx = 1, pady = 1)

button_four = Button(btns_frame, image = img4, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("4")).grid(row = 2, column = 0,  padx = 1, pady = 1)
button_five = Button(btns_frame, image = img5, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("5")).grid(row = 2, column = 1, padx = 1, pady = 1)
button_six = Button(btns_frame, image = img6, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("6")).grid(row = 2, column = 2,  padx = 1, pady = 1)
button_minus = Button(btns_frame, image = imgMinus, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3,  padx = 1, pady = 1)

button_seven = Button(btns_frame, image = img7, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("7")).grid(row = 3, column = 0,  padx = 1, pady = 1)
button_eight = Button(btns_frame, image = img8, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("8")).grid(row = 3, column = 1, padx = 1, pady = 1)
button_nine = Button(btns_frame, image = img9, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("9")).grid(row = 3, column = 2,  padx = 1, pady = 1)
button_multiply = Button(btns_frame, image = imgMulti, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 3, column = 3,  padx = 1, pady = 1)

button_zero = Button(btns_frame, image = img0, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("0")).grid(row = 4, column = 0,  padx = 1, pady = 1)
button_dot = Button(btns_frame, image = imgDot, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 1,  padx = 1, pady = 1)
button_exp = Button(btns_frame, image = imgExpo, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("**")).grid(row = 4, column = 2,  padx = 1, pady = 1)
button_modulo = Button(btns_frame, image = imgMod, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click("%")).grid(row = 4, column = 3,  padx = 1, pady = 1)

button_pi = Button(btns_frame, image = imgMod, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click(math.pi)).grid(row = 5, column = 0,  padx = 1, pady = 1)

button_e = Button(btns_frame, image = imgMod, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click(math.e)).grid(row = 5, column = 1,  padx = 1, pady = 1)

button_factorial = Button(btns_frame, image = imgMod, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click(factorial(input_text))).grid(row = 5, column = 2,  padx = 1, pady = 1)

button_square = Button(btns_frame, image = imgMod, width = 75, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_click(square(input_text))).grid(row = 5, column = 3,  padx = 1, pady = 1)

buttonTrigonometry = tk.Button(btns_frame, image = imgTrigonometry, width = 152, height = 53, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2",
              text="Create trigonometry window",
              command=createTrigonometryWindow).grid(row = 6, column = 0, columnspan = 2, padx = 1, pady = 1)

#buttonEmpty_Now = tk.Button(btns_frame, image = imgFx, width = 150, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2",
#             text="...",
#              command=btn_click("1")).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)

button_equals = Button(btns_frame, image = imgEqual, width = 310, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_equal()).grid(row = 7, column = 0, columnspan = 4, padx = 1, pady = 1)

buttonExample = tk.Button(btns_frame, image = imgFx, width = 310, height = 51, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2",
              text="Create new window",
              command=createNewWindow).grid(row = 8, column = 0, columnspan = 4, padx = 1, pady = 1)





main_calc.mainloop()
