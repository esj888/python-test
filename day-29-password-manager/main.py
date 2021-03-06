# uses Tkinter Entry widget

from tkinter import *
from tkinter import messagebox
import random
# import random import choice, randint, shuffle
import pyperclip


# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #    password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #    password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #    password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")  # debug
    password_box.insert(0, password)
    pyperclip.copy(password)                # copy password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    print(website_box.get())      # debug
    print(email_box.get())        # debug
    print(password_box.get())     # debug
    pw_rec = ''.join([website_box.get(), ' | ', email_box.get(), ' | ', password_box.get(), '\n'])
    print(pw_rec)     # debug

    if len(website_box.get()) == 0 or len(password_box.get()) == 0:
        messagebox.showerror(title='error1', message="Don't leave any fields empty!")
        error1 = True
    else:
        error1 = False

    if not error1:
        save_okay = messagebox.askokcancel(title=website_box.get(),
                                           message=f"These are the details entered: \nEmail: {email_box.get()}"
                                                   f""f"\nPassword: {password_box.get()} \nIs it okay to save?")
        if save_okay:
            pw_file = open("my_pass.txt", "a")
            pw_file.write(pw_rec)
            pw_file.close()

            website_box.delete(0, 'end')
            email_box.delete(0, 'end')
            password_box.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

# background image
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)   # use grid system or use pack
# canvas.pack()

# labels, boxes, and buttons
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_box = Entry(width=35)
website_box.focus()
website_box.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_box = Entry(width=35)
email_box.grid(row=2, column=1, columnspan=2)
email_box.insert(0, 'email@gmail.com')

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_box = Entry(width=17)
password_box.grid(row=3, column=1)
password_btn = Button(text="Generate Password", command=gen_pass)
password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=30, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
