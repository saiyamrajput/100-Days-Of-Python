# import statements
from turtle import Turtle
import random

# constants for car colors, starting speed and new speed increment after
#   leveling up
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Creates cars"""

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates car"""
        # car_creation checks if new car is created or not if random number
        #   generated is 1
        car_creation = random.randint(1, 6)
        if car_creation == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            car.goto(300, y_position)
            self.cars.append(car)

    def move_car(self):
        """Moves car in backward direction"""
        for i in self.cars:
            i.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        """Increases car speed after leveling up"""
        self.speed += MOVE_INCREMENT
