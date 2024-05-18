# import statements
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# creating screen and setting its size, background color and title
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# creating left and right paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# creating ball and scoreboard object
ball = Ball()
scoreboard = Scoreboard()

# setting keyboard keys for the movement of paddles
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# game is over checks if game ended or not
game_is_over = False


def stop_game():
    """Stops the game"""
    global game_is_over
    game_is_over = True


while not game_is_over:

    # updating screen
    time.sleep(ball.move_speed)
    screen.update()

    # checking if user wants to stop the game or not
    screen.onkey(stop_game, "q")

    # moving the ball
    time.sleep(ball.move_speed)
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detecting right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detecting left paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
