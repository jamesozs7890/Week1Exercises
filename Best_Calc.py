from tkinter import *

root = Tk()

root.geometry("500x500")
root.title("Best Calculator")


def calculate():
    num1 = E1.get()
    num2 = E2.get()

    result = str(num1) + str(num2)

    ans.configure(text=result)


def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    ans.configure(text=0)


L1 = Label(text="I am programming!!!")
L2 = Label(text="Hello World!!")
L3 = Label(text="The best calculator")
L4 = Label(text="+")
L5 = Label(text="Result =")
ans = Label(text="0")

E1 = Entry()
E2 = Entry()

B1 = Button(text="Calculate", command=calculate)
B2 = Button(text="Clear", command=clear)

L1.grid(row=1, column=1, sticky="w")
L2.grid(row=2, column=1, sticky="w")
L3.grid(row=3, column=1, sticky="w")

E1.grid(row=4, column=1)
L4.grid(row=4, column=2)
E2.grid(row=4, column=3)
B1.grid(row=4, column=4)
B2.grid(row=4, column=5)

L5.grid(row=5, column=1, sticky="w")
ans.grid(row=5, column=2, sticky="w")

mainloop()