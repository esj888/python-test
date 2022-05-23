import tkinter
# from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

# my_label["text"] = "New Label Text"     # use this method or
my_label.config(text="New Label Text")    # this method


# button


def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=input1.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# entry
input1 = tkinter.Entry(width=10)
input1.pack()
print(input1.get())

window.mainloop()       # used to keep window open

