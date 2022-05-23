import tkinter
# from tkinter import *


def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=input1.get())


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=100, pady=100)         # add padding around the entire window

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label["text"] = "New Label Text"     # use this method or
my_label.config(text="New Label Text")    # this method
my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)     # add padding

# button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# entry
input1 = tkinter.Entry(width=10)
print(input1.get())
input1.grid(column=3, row=2)

# button2
button2 = tkinter.Button(text="Button2")
button2.grid(column=2, row=0)

window.mainloop()       # used to keep window open

