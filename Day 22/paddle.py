# import statement
from turtle import Turtle


class Paddle(Turtle):
    """Creates paddles to play game"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Paddle moves up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Paddle moves down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
