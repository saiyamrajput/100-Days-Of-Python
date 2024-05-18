# Get coordinates from the screen wherever the mouse clicks
# def get_mouse_click_cor(x, y):
#     """Prints coordinates from the screen"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

# import statements
import turtle
import pandas

# creating screen, screen title
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# reading data
data = pandas.read_csv("50_states.csv")

# creating states list
states = data.state.to_list()

# stores users guess if the guess is right
guess = []

# checking if length is less than 50 or not
while len(guess) < 50:

    # asking users guess
    answer = screen.textinput(title=f"{len(guess)}/50 States Correct",
                              prompt="What's another state's name?").title()

    # checking if user want to exit or not
    if answer == "Exit":
        missed = []

        # checking missed states
        for i in states:
            if i not in guess:
                missed.append(i)
        # creating states to learn csv file
        csv_file = pandas.DataFrame(missed)
        csv_file.to_csv("states_to_learn.csv")
        break

    # checking is users guess is right or wrong
    if answer in states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        guess.append(answer)
