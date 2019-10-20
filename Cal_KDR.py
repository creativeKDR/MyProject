import tkinter
from tkinter import *

root = tkinter.Tk()
root.geometry("320x250")
root.resizable(0, 0)
root.title("Calculator by KDR")

eqn = StringVar()
exp = ""

exp_field = Entry(root, textvariable=eqn)
exp_field.grid(columnspan=10, ipadx=100)

Button7 = Button(root, text="7", command=lambda: num(7), height=3, width=10).grid(row=2, column=0)
Button8 = Button(root, text="8", command=lambda: num(8), height=3, width=10).grid(row=2, column=1)
Button9 = Button(root, text="9", command=lambda: num(9), height=3, width=10).grid(row=2, column=2)
Button4 = Button(root, text="4", command=lambda: num(4), height=3, width=10).grid(row=3, column=0)
Button5 = Button(root, text="5", command=lambda: num(5), height=3, width=10).grid(row=3, column=1)
Button6 = Button(root, text="6", command=lambda: num(6), height=3, width=10).grid(row=3, column=2)
Button0 = Button(root, text="0", command=lambda: num(0), height=3, width=10).grid(row=5, column=1)
Button1 = Button(root, text="1", command=lambda: num(1), height=3, width=10).grid(row=4, column=0)
Button2 = Button(root, text="2", command=lambda: num(2), height=3, width=10).grid(row=4, column=1)
Button3 = Button(root, text="3", command=lambda: num(3), height=3, width=10).grid(row=4, column=2)

ButtonAdd = Button(root, text="+", command=lambda: num("+"), height=3, width=10).grid(row=2, column=3)
ButtonSub = Button(root, text="-", command=lambda: num("-"), height=3, width=10).grid(row=3, column=3)
ButtonMul = Button(root, text="*", command=lambda: num("*"), height=3, width=10).grid(row=4, column=3)
ButtonDiv = Button(root, text="/", command=lambda: num("/"), height=3, width=10).grid(row=5, column=3)

ButtonClr = Button(root, text="Clear", command=lambda: Clr(), height=3, width=10).grid(row=5, column=0)
ButtonEql = Button(root, text="=", command=lambda: Eql(), height=3, width=10).grid(row=5, column=2)


def num(number):
    global exp
    exp = exp + str(number)
    eqn.set(exp)


def Clr():
    global exp
    exp = ""
    eqn.set("")


def Eql():
    global exp
    try:
        total = str(eval(exp))
        eqn.set(total)
        exp = ""

    except:
        eqn.set(" error ")
        exp = ""


root.mainloop()
