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
window.geometry("316x384")
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

button_equals = Button(btns_frame, image = imgEqual, width = 310, height = 50, bd = 0, bg = "grey", activebackground = "grey", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 0, columnspan = 4, padx = 1, pady = 1)



window.mainloop()
