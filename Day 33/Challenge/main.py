# import statements
from tkinter import *
import requests
import math

# constants
FONT_SIZES = [35, 25, 20, 15, 10]
FONT = "Cambria"


def cal_font_size(quote):
    """Handles the font size of the quotes"""

    # calculating quote length then finding the correct size
    quote_length = len(quote)
    size_category = math.floor(quote_length / 50)
    font_size = FONT_SIZES[size_category]
    return font_size


def get_quote():
    """Writes the quote on the canvas image from the API"""
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    # getting data in json format
    data = response.json()
    # calculating font size
    size = cal_font_size(data["quote"])
    canvas.itemconfig(quote_text, text=data["quote"], font=(FONT, size, "bold"))


# creating window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# creating canvas with image
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE",
                                width=250, font=(FONT, 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

# creating button
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
