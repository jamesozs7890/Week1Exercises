from tkinter import *

root = Tk()
root.geometry('200x200')


def enter():
    L1.configure(text="Hello World")


def select():
    selection = "Check:"+str(var1.get()+var2.get())
    label.config(text=selection)


Space = Label(text="              ")
Space.grid(row=0, column=0)

F1 = LabelFrame(text="Setting", padx=10, pady=10)
F1.grid(row=1, column=1)

B1 = Button(F1, text="Enter", command=enter)
B1.grid(row=0, column=0)

L1 = Label(F1, text='')
L1.grid(row=1, column=0)

var1 = IntVar()
var2 = IntVar()
C1 = Checkbutton(F1, text="I love coffee", variable=var1, command=select)
C2 = Checkbutton(F1, text="I love milk", variable=var2, command=select)
C1.grid(row=3, column=0)
C2.grid(row=4, column=0)

label = Label(F1, text="Check: 0")
label.grid(row=5, column=0)

mainloop()