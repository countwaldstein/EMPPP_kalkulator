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

    try:
        result = str(eval(expression))
        input_text.set(result)

    except:
        input_text.set("Invalid syntax")
        result = ""
    expression = result

expression = ""



window = Tk()
window.geometry("312x380")
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

button_seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("7")).grid(row = 3, column = 0,  padx = 1, pady = 1)
button_eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("8")).grid(row = 3, column = 1, padx = 1, pady = 1)
button_nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("9")).grid(row = 3, column = 2,  padx = 1, pady = 1)
button_multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 3, column = 3,  padx = 1, pady = 1)

button_zero = Button(btns_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("0")).grid(row = 4, column = 0,  padx = 1, pady = 1)
button_dot = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 1,  padx = 1, pady = 1)
button_exp = Button(btns_frame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("**")).grid(row = 4, column = 2,  padx = 1, pady = 1)
button_modulo = Button(btns_frame, text = "mod", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("%")).grid(row = 4, column = 3,  padx = 1, pady = 1)

button_equals = Button(btns_frame, text = "=", fg = "black", width = 43, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 0, columnspan = 4, padx = 1, pady = 1)



window.mainloop()
