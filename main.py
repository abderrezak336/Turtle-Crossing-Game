import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



scoreboard = Scoreboard()

player = Player()

screen.listen()

segments = []
screen.onkey(player.up, "Up")

carmanager = CarManager()








game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    carmanager.creat_car()
    carmanager.move_car()


    for car in carmanager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False



    if player.ycor() > 280:
        scoreboard.update_scoreboard()
        scoreboard.increas_level()
        carmanager.increas_level()
        player.reset_position()







screen.exitonclick()

























