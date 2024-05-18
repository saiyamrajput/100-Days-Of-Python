# import statements
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# creating screen and setting screen size, color and title of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# creating objects snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# game_is_over checks if it is over or not
game_is_over = False


def stop():
    """Game stops"""
    global game_is_over
    game_is_over = True
    scoreboard.game_over()


while not game_is_over:
    screen.update()

    # checking if user wants to stop the game or not
    screen.onkey(stop, "q")

    time.sleep(0.1)

    # moving snake
    snake.move()

    # Detecting collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecting collision with wall.
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280
            or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detecting collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# exit screen on click
screen.exitonclick()
