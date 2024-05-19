# import statement
from tkinter import *


def converter():
    """Converts Miles to Km"""
    result = float(num_miles.get()) * 1.609
    answer_label.config(text=round(result, 2))


# creating window
window = Tk()
window.title("Miles to Km Converter")
window.geometry("330x150")
window.config(padx=20, pady=20)

# creating input label
input_label = Label(text="Enter the number", font="Cambria")
input_label.grid(column=0, row=0)
input_label.config(padx=10, pady=10)

# entry/input
num_miles = Entry(width=10)
num_miles.insert(END, string="0")
num_miles.grid(column=1, row=0)

# creating miles label
miles_label = Label(text="Miles", font="Cambria")
miles_label.grid(column=3, row=0)
miles_label.config(padx=10, pady=10)

# creating equals to label
equal_label = Label(text="is equal to", font="Cambria")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

# creating answer label
answer_label = Label(text="0", font="Arial")
answer_label.grid(column=1, row=1)
answer_label.config(padx=10, pady=10)

# creating km label
km_label = Label(text="Km", font="Cambria")
km_label.grid(column=3, row=1)
km_label.config(padx=10, pady=10)

# creating button to calculate
calculate_button = Button(text="Calculate", command=converter, font="Cambria")
calculate_button.grid(column=1, row=2)

window.mainloop()
