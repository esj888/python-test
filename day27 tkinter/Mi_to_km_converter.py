import tkinter


def button_clicked():
    print("I got clicked")
    km_converted = int(input1.get()) * 1.609344
    km_num_label.config(text=round(km_converted, 2))


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

# label
mi_label = tkinter.Label(text="Miles", font=("Arial", 14))
mi_label.grid(column=2, row=0)
equal_label = tkinter.Label(text="is equal to", font=("Arial", 14))
equal_label.grid(column=0, row=1)
km_num_label = tkinter.Label(text="0", font=("Arial", 14, "bold"))
km_num_label.grid(column=1, row=1)
km_label = tkinter.Label(text="Km", font=("Arial", 14))
km_label.grid(column=2, row=1)

# button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

# entry
input1 = tkinter.Entry(width=10)
print(input1.get())
input1.grid(column=1, row=0)

window.mainloop()       # used to keep window open
