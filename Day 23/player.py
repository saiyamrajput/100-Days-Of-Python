# import statement
from turtle import Turtle

# setting player starting position, move distance and finish line coordinates
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Creates Player"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.start()
        self.setheading(90)

    def move_up(self):
        """Moves the player in upward direction"""
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        """Returns true if player finished the level otherwise false"""
        # checking if player reached the finish line or not
        if self.ycor() > 280:
            return True
        else:
            return False

    def start(self):
        """Moves player to starting position"""
        self.goto(STARTING_POSITION)
