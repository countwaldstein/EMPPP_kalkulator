from tkinter import *

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

    result = str(eval(expression))
    input_text.set(result)
    expression = result
expression = ""

window = Tk()
window.geometry("312x324")
window.resizable(0, 0)
window.title("Calc")

input_text = StringVar()
input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

clear = Button(btns_frame, text = "Clear", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

button_one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("1")).grid(row = 1, column = 0,  padx = 1, pady = 1)
button_two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("2")).grid(row = 1, column = 1,  padx = 1, pady = 1)
button_three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("3")).grid(row = 1, column = 2, padx = 1, pady = 1)
button_plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 1, column = 3, padx = 1, pady = 1)

button_four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("4")).grid(row = 2, column = 0,  padx = 1, pady = 1)
button_five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("5")).grid(row = 2, column = 1, padx = 1, pady = 1)
button_six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("6")).grid(row = 2, column = 2,  padx = 1, pady = 1)
button_minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3,  padx = 1, pady = 1)

button_equals = Button(btns_frame, text = "=", fg = "black", width = 43, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 3, column = 0, columnspan = 4, padx = 1, pady = 1)

# button_fx = Button(btns_frame, text = "f(x)=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("f(x)=")).grid(row = 3, column = 0,  padx = 1, pady = 1)
# button_x = Button(btns_frame, text = "x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("x")).grid(row = 3, column = 1,  padx = 1, pady = 1)
# button_2 = Button(btns_frame, text = "^2", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("²")).grid(row = 3, column = 2,  padx = 1, pady = 1)
# button_3 = Button(btns_frame, text = "^3", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("³")).grid(row = 3, column = 3,  padx = 1, pady = 1)



window.mainloop()