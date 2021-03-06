# uses Tkinter Entry widget

from tkinter import *
from tkinter import messagebox
import random
# import random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"


# ---------------------------- Search password ------------------------------- #
def find_password():
    website = website_box.get()
    print("find password function")
    try:
        with open("my_pass.json", "r") as pw_file:
            data_dict = json.load(pw_file)
    except FileNotFoundError:
        print("file doesn't exist.")
        messagebox.showerror(title='error 888', message="File doesn't exist.")
    else:
        print(data_dict)                     # dictionary contains website and email, password.
        # for sites in data.keys():
        #    print(sites)
        if website in data_dict:
            print(website, " found")
            email = data_dict[website]["email"]
            pass1 = data_dict[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email} \npassword: {pass1}")
        else:
            print(website, " not found!!")
            messagebox.showinfo(title='not found', message="Website not found.")


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
    website = website_box.get()
    email = email_box.get()
    password = password_box.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website_box.get()) == 0 or len(password_box.get()) == 0:
        messagebox.showerror(title='error1', message="Don't leave any fields empty!")
        error1 = True
    else:
        error1 = False

    if not error1:
        try:
            with open("my_pass.json", "r") as pw_file:       # checks to see if file exists
                # read old data
                data = json.load(pw_file)
                # print(f"data is {type(data)}")   # debug - type is 'dict'
                # update old data with new data.  you do not want to append.
                data.update(new_data)
        except FileNotFoundError:
            with open("my_pass.json", "w") as pw_file:
                json.dump(new_data, pw_file, indent=4)  # write to json file
        else:
            with open("my_pass.json", "w") as pw_file:
                # save updated data
                json.dump(data, pw_file, indent=4)             # write to json file
        finally:
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
password_box = Entry(width=35)
password_box.grid(row=3, column=1, columnspan=2)
password_btn = Button(text="Generate Password", command=gen_pass)
password_btn.grid(row=3, column=3)

add_btn = Button(text="Add", width=30, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(row=1, column=3)

window.mainloop()
