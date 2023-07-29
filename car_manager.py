from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT









    def creat_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.goto(320, random.randrange(-280, 300))
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars[::3]:
            car.backward(self.car_speed)


    def increas_level(self):
        self.car_speed += 10



















