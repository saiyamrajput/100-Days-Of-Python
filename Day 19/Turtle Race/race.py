# import statement
from turtle import Turtle, Screen
import random

t = Turtle()
t.hideturtle()
t.penup()


def display_text(text):
    """Displays text on screen"""
    t.clear()
    t.hideturtle()
    t.home()
    t.pencolor("black")
    t.write(text, align="center", font=("Arial", 16, "normal"))


# over checks whether race is over or not or race has started or not
over = True

# creating screen for display
screen = Screen()

# setting screen size
screen.setup(width=500, height=400)

# asking use to input his bet on which turtle will win
bet = screen.textinput(title="Make your bet",
                       prompt="Which turtle will win the race? "
                              "Enter the color name: ")

# setting colours for 6 turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# setting turtle positions
y_value = [-100, -60, -20, 20, 60, 100]

# stores all the turtles
turtles = []

# creating 6 turtles
for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()

    # giving each turtle specific color
    t.color(colors[i])

    # setting turtle in different start positions
    t.goto(x=-230, y=y_value[i])
    turtles.append(t)

# checking if user inputted their bet or not
if bet:
    over = False

# starting the race
while not over:
    # turtles racing
    for turtle in turtles:
        # 230 is 250 - half the width of the turtle.

        # checking turtle coordinates to see which turtle won
        if turtle.xcor() > 230:
            won = turtle.pencolor()
            # checking if the turtle on which user placed bet won or not
            if won == bet:
                display_text(f"You've won! The {won} turtle is the winner!")
            else:
                display_text(f"You've lost! The {won} turtle is the winner!")
            over = True

        # making each turtle move at a random speed/distance.
        dist = random.randint(0, 10)
        turtle.forward(dist)

# exit screen on click
screen.exitonclick()
