# import statement
from turtle import Turtle

# setting position
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# setting distance and turning angles
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake Class creates snake, and controls its movements"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates Snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds new segment to snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extending snake size"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Helps Snake to move"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Helps snake to move up"""
        if self.head.heading() != "s":
            self.head.setheading(UP)

    def down(self):
        """Helps snake to move down"""
        if self.head.heading() != "w":
            self.head.setheading(DOWN)

    def left(self):
        """Helps snake to move left"""
        if self.head.heading() != "d":
            self.head.setheading(LEFT)

    def right(self):
        """Helps snake to move right"""
        if self.head.heading() != "a":
            self.head.setheading(RIGHT)

    def reset(self):
        """Resets the game"""
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
