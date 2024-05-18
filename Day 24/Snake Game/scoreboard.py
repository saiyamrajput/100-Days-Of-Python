# import statement
from turtle import Turtle


class Scoreboard(Turtle):
    """Checks and updates the scoreboard accordingly"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the score"""
        self.clear()
        self.write(f"Score: {self.score}    ||  Highscore: {self.highscore}",
                   align="center", font=("Courier", 20, "normal"))

    def reset(self):
        """Updates the highscore and """
        if self.score > self.highscore:
            self.highscore = self.score

        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases the score after food is eaten by the snake"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 20, "normal"))
