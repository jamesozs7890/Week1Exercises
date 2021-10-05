from tkinter import*

root = Tk()
root.geometry("300x300")


def select():
    selection = 'You selected the option: ' + str(var.get())
    label.config(text=selection)


var = IntVar()

R1 = Radiobutton(text='Option 1', variable=var, value= 1, command=select)
R1.grid(row=0,column=0)

R2 = Radiobutton(text='Option 2', variable=var, value= 2, command=select)
R2.grid(row=1,column=0)

R3 = Radiobutton(text='Option 2', variable=var, value= 3, command=select)
R3.grid(row=2,column=0)

label = Label()
label.grid(row=3, column=0)

mainloop()
