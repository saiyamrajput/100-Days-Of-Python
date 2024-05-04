# import statement
from turtle import Turtle, Screen

# creating object t turtle and screen
t = Turtle()
screen = Screen()


def forward():
    """Turtle Moves forward"""
    t.forward(5)


def left():
    """Rotates to left direction"""
    direction = t.heading() + 5
    t.setheading(direction)


def right():
    """Rotates to right direction"""
    direction = t.heading() - 5
    t.setheading(direction)


def backward():
    """Turtle moves backward"""
    t.backward(5)


def clear():
    """Clears the screen and Turtle returns to the centre of the screen
    that is to the original start position"""
    t.clear()
    t.penup()
    t.home()
    t.pendown()


# setting keyboard commands so that user can draw
screen.listen()
screen.onkeypress(forward, "w")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(backward, "s")
screen.onkey(clear, "c")

# exit on click
screen.exitonclick()
