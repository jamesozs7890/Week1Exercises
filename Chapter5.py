from tkinter import *
root = Tk()

root.geometry("500x500")
root.title("Python GUI")


def obt():
    text = E1.get()
    L2.configure(text=text)


L1 = Label(text="Enter a text:")
L2 = Label(text="0")
E1 = Entry()
B1 = Button(text="Enter", command=obt)

L1.grid(row=0, column=0)
L2.grid(row=3, column=1)
E1.grid(row=0, column=1)
B1.grid(row=1, column=1)

mainloop()
