# import statement
from turtle import Turtle

# text font
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Creates Scoreboard"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-280, 245)
        self.update()

    def update(self):
        """Updates Scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase(self):
        """Increases the level number"""
        self.level += 1
        self.update()

    def game_over(self):
        """Displays game over"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)