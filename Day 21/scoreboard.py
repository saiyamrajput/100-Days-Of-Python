# import statement
from turtle import Turtle


class Scoreboard(Turtle):
    """Checks and updates the scoreboard accordingly"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the score"""
        self.write(f"Score: {self.score}", align="center",
                   font=("Courier", 24, "normal"))

    def game_over(self):
        """Checks if game is over or not"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 24, "normal"))

    def increase_score(self):
        """Increases the score after food is eaten by the snake"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
