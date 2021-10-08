from tkinter import*
root = Tk()
root.geometry('600x600')


photo = PhotoImage(file=r"c:\dataset\wm.gif")
photo = photo.zoom(1)
L1 = Label(image=photo)
L1.grid(row=0, column=1)


mainloop()
