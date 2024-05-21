# import statements
from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
import json

# -----------------------------CONSTANTS-------------------------------------- #
FONT = "Cambria"

# -----------------------------SEARCH WEBSITES-------------------------------- #


def search_website():
    """Finds already saved password and username associated with the
    website"""
    website_text = website_entry.get()

    if len(website_text) == 0:
        messagebox.showwarning(title="Error", message="The entry field "
                                                      "is empty")
        return
    # handling error
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File found")
    else:
        # checking if website is in data.json or not
        if website_text in data:
            username_text = data[website_text]["Email"]
            password_text = data[website_text]["Password"]
            messagebox.showinfo(title=website_text,
                                message=f"Email: {username_text}\n"
                                        f"Password: {password_text}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for "
                                                       f"{website_text} exists")

# -----------------------------CLEAR ENTRIES---------------------------------- #


def clear():
    """Clears Website and Password entry"""
    website_entry.delete(0, END)
    password_entry.delete(0, END)

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
    """Saves the password in 'data.json' file and produces warning messages if
    all the fields are not filled"""
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()

    data_dict = {
        website_text: {
            "Email": username_text,
            "Password": password_text
        }
    }
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
        try:
            with open("data.json", mode="r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                # writing new data if file not exists
                json.dump(data_dict, file, indent=4)
        else:
            # updating the data with new data_dict
            data.update(data_dict)
            with open("data.json", mode="w") as file:
                # writing new data if file not exists
                json.dump(data, file, indent=4)
        finally:
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

# clear button
clear_button = Button(text="Clear", font=FONT, command=clear, width=13)
clear_button.grid(column=2, row=2)

# search button
search_button = Button(text="Search Website", font=FONT, width=13,
                       command=search_website)
search_button.grid(column=2, row=1)

# creating entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2)
username_entry.insert(END, "username@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky="W")

window.mainloop()
