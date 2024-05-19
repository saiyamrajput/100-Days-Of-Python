# import statement
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Cambria"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    """Resets the timer"""
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", font=(FONT_NAME, 30), bg=GREEN, fg=RED)
    check_mark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    """Starts the timer"""
    global reps
    reps += 1
    # taking note of work, short break and long break time
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    # checking for proper work, short, or long time
    if reps % 2 != 0:
        title_label.config(text="Work Time", font=(FONT_NAME, 30), bg=GREEN,
                           fg=RED)
        count_down(work_sec)
    elif reps % 8 == 0:
        title_label.config(text="Long Break", font=(FONT_NAME, 30), bg=GREEN,
                           fg=YELLOW)
        count_down(long_sec)
    else:
        title_label.config(text="Short Break", font=(FONT_NAME, 30), bg=GREEN,
                           fg=PINK)
        count_down(short_sec)


# ---------------------------- COUNTDOWN MECHANISM -------------------------- #
def count_down(count):
    """Counts down the timer"""
    global timer
    # calculating minutes and seconds
    minute = math.floor(count / 60)
    sec = count % 60

    # adjusting sec and minute
    if minute < 10:
        minute = f"0{minute}"
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        global reps

        # adding checkmarks
        checkmarks = ""
        for i in range(math.floor(reps/2)):
            checkmarks += "✔️"
        # configuring checkmark label
        check_mark_label.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #


# creating window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=GREEN)

# creating canvas
canvas = Canvas(width=205, height=224, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_png)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# creating title label
title_label = Label(text="Timer", font=(FONT_NAME, 30), bg=GREEN, fg=RED)
title_label.grid(column=1, row=0)

# creating start button
start_button = Button(text="Start", font=FONT_NAME, bg=PINK, command=start)
start_button.grid(column=0, row=2)

# creating reset button
reset_button = Button(text="Reset", font=FONT_NAME, bg=PINK, command=reset)
reset_button.grid(column=2, row=2)

# checkmark label
check_mark_label = Label(fg="black", bg=GREEN)
check_mark_label.grid(column=1, row=3)

window.mainloop()
