# import statements
from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip

# -----------------------------CONSTANTS-------------------------------------- #
FONT = "Cambria"

# ---------------------------- PASSWORD GENERATOR ---------------------------- #


def generate():
    """Generates password"""
    # first deleting any other entry in the entry box and then generating the
    #   password
    password_entry.delete(0, END)
    password = Password()
    generated_password = password.generate()

    # copying password to clipboard
    pyperclip.copy(generated_password)

    # inserting the password in the entry box
    password_entry.insert(0, generated_password)
# ---------------------------- SAVE PASSWORD --------------------------------- #


# saving password to data
def save():
    """Saves the password in 'data.txt' file and produces warning messages if
    all the fields are not filled"""
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()

    # checking if all the fields are entered or not
    if len(password_text) == 0 or len(website_text) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't "
                                                             "leave any empty "
                                                             "fields")
    elif messagebox.askokcancel(title=website_text,
                                message=f"You've entered: "
                                        f"\nEmail: {username_text}\n"
                                        f"Password: {password_text}"
                                        f"\nIs it OK to save?"):
        with open("data.txt", mode="a") as file:
            file.write(f"{website_text} || {username_text} || "
                       f"{password_text}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            username_entry.insert(END, "username@gmail.com")
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# creating window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# creating canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# generate button
generate_button = Button(text="Generate Password", font=FONT, command=generate)
generate_button.grid(column=2, row=3)

# label generation
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

# add button
add_button = Button(text="Add", font=FONT, width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# creating entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(END, "username@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

window.mainloop()
