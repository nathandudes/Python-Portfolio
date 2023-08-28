from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please check for empty fields")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"Details entered: \nEmail: {email} \nPassword: {password} \n Okay to save?")

        if is_okay:
            with open("pw.txt", mode="a") as file:
                completed_file = f"Website: {website} | Email: {email} | Password: {password}\n"
                file.write(completed_file)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website:", font=(FONT_NAME, 10))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(column=0, row=3)

blank_label = Label()
blank_label.grid(column=1, row=4)

# ENTRIES
website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "nathandelongyt@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

# BUTTONS
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=25, command=save)
add_button.grid(column=1, row=5)

window.mainloop()
