# import statement
from turtle import Turtle


class Ball(Turtle):
    """Creates a ball"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.08

    def move(self):
        """Moves the ball in a specific direction"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Moves the ball after bouncing from the top or bottom wall"""
        self.y_move *= -1

    def bounce_x(self):
        """Moves the ball after bouncing from the paddle or the top or bottom
        wall"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the ball position after a player misses it"""
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()
