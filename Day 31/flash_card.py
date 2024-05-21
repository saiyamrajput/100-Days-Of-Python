# import statements
from tkinter import *
import random
import pandas

# ------------------------------CONSTANTS------------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Cambria", 40, "italic")
WORD_FONT = ("Cambria", 60, "bold")
data_dict = {}
card = {}
timer = NONE

# handling error while reading data and converting it to dictionary
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# ---------------------------SAVING WORDS TO LEARN---------------------------- #


def is_known():
    """Checks if the word is known by the user or not and then remove it from
    file 'words_to_learn.csv"""
    data_dict.remove(card)
    new_data_dict = pandas.DataFrame(data_dict)
    new_data_dict.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------LANGUAGE CHANGE---------------------------------- #


def change_language():
    """Flips the card"""
    global timer
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_name, text="English", fill="black",
                      font=LANGUAGE_FONT)
    canvas.itemconfig(language_word, text=card["English"], fill="black",
                      font=WORD_FONT)
    window.after_cancel(timer)

# ---------------------------NEW FLASH CARD----------------------------------- #


def next_card():
    """Displays next flash card"""
    global card, timer
    window.after_cancel(timer)
    card = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language_name, text="French", font=LANGUAGE_FONT)
    canvas.itemconfig(language_word, text=card["French"], font=WORD_FONT)
    timer = window.after(5000, change_language)

# ------------------------------UI SETUP-------------------------------------- #


def start_button_pressed():
    """Removes the start button once it is pressed"""
    next_card()
    start_button.destroy()


# creating window
window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# creating canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
language_name = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
language_word = canvas.create_text(400, 263, text="\tWord\n\n"
                                                  "Click on "
                                                  "            button to "
                                                  "begin",
                                   font=("Cambria", 25, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# creating buttons
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0,
                      command=is_known)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0,
                      command=next_card)
wrong_button.grid(column=0, row=1)

# creating start button
start_button = Button(text="Start", highlightthickness=0, bg=BACKGROUND_COLOR,
                      font=("Cambria", 20, "bold"),
                      command=start_button_pressed)
start_button.place(x=303, y=275)

window.mainloop()
