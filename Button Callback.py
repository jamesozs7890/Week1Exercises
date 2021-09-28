from tkinter import*
root = Tk()

root.geometry("500x500")
root.title("Button Callback")


def callback():
    L1.configure(text="Button Clicked")
    print("0")


def reset():
    L1.configure(text="0")
    print("1")


L1 = Label(text="0")
L1.grid(row=0, column=0)

B1 = Button(text="Button", command=callback)
B2 = Button(text="Reset", command=reset)
B1.grid(row=1, column=0)
B2.grid(row=2, column=0)

mainloop()