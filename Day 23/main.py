# import statements
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# creating screen and setting screen size and background color
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)

# creating player object
player = Player()

# setting keyboard keys for the movement of turtle
screen.listen()
screen.onkey(player.move_up, "w")

# creating car manager object
car = CarManager()

# creating scoreboard object
scoreboard = Scoreboard()

# game_is_over checks if game is over or not
game_is_over = False
while not game_is_over:
    # updating screen
    time.sleep(0.1)
    screen.update()

    # creating car
    car.create_car()
    car.move_car()

    # detecting collision with car
    for i in car.cars:
        # checking if player collided or not
        if i.distance(player) < 20:
            game_is_over = True
            scoreboard.game_over()

    # if player reached the finish line then going back to starting position
    if player.finish_line():
        player.start()
        car.increase_speed()
        scoreboard.increase()

screen.exitonclick()
