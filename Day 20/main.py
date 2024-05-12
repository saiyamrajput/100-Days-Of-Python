# import statements
from turtle import Screen
from snake import Snake
import time

# creating screen and setting screen size, color and title of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# creating objects snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# game_is_over checks if is over or not
game_is_over = False
while not game_is_over:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_over = True

# exit screen on click
screen.exitonclick()
