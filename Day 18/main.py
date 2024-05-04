# import statement
from image_color import rgb_colors
import random
import turtle as t


def start_value():
    """Sets the turtle position for start"""
    # setting colormode to 255, speed to fastest, and hiding the turtle arrow
    t.colormode(255)
    t.speed("fastest")
    t.hideturtle()

    # lifting the pen up so that no movement lines are visible
    t.penup()

    # setting head position to adjust the image in proper format in screen
    t.setheading(225)
    t.forward(300)
    t.setheading(0)


# setting maximum dots to 100 to fit in the given screen size
number_of_dots = 100


def next_row():
    """Moves turtle position to next row to continue printing the painting"""
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)


start_value()

# printing the painting
for i in range(1, number_of_dots + 1):
    # generating random colour for the dots
    color = (random.choice(rgb_colors))

    # setting dot size and its colour
    t.dot(20, color)

    # distance between each dot is 50 pixels
    t.forward(50)

    # checking if the line has 10 dots then moving to next row
    if i % 10 == 0 and i != 100:
        next_row()

# creating screen to exit on click
screen = t.Screen()
screen.exitonclick()
