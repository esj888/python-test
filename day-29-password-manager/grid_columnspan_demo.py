from tkinter import *

window = Tk()

w = Label(text="Website", width=10, height=5)
w.grid(column=0, row=1)

r = Label(text="test", bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)


window.mainloop()
