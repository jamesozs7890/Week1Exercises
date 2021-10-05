import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry('200x200')


def select():
    if var1.get() == 1 & var2.get() == 1:
        label.configure(text="I love cycling and jogging")
    elif var2.get() == 1:
        label.configure(text="I love jogging")
    elif var1.get() == 1:
        label.configure(text="I love cycling")
    elif var1.get() == 0 & var2.get() == 0:
        label.configure(text=" I don't like cycling and jogging")


def opt():
    tkinter.messagebox.showinfo(title='Warning', message=var3.get())

# messagebox.showinfo(title='Warning', message=var3.get())


var1 = IntVar()
var2 = IntVar()
C1 = Checkbutton(text="Cycling", variable=var1, command=select)
C2 = Checkbutton(text="Jogging", variable=var2, command=select)
C1.grid(row=3, column=0)
C2.grid(row=4, column=0)

label = Label(text="")
label.grid(row=5, column=0)

var3 = StringVar()
C3 = Checkbutton(text="Agree?", command=opt, variable=var3, onvalue='Agree', offvalue='Disagree')
C3.deselect()
C3.grid(row=5, column=1)

mainloop()
