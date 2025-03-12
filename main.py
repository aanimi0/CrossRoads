import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.title("CrossRoads")
screen.setup(width=600, height=600)
screen.tracer(0)
game_speed = 0.1

random_y = random.randint(-290,290)

player = Player(STARTING_POSITION)
car = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.turn_nord, "Up")
screen.onkey(player.turn_east, "Left")
screen.onkey(player.turn_west, "Right")
screen.onkey(player.move, "space")

game_is_on = True

while game_is_on:

    car.create_car()
    car.car_move()

    for vehicle in car.all_cars:
        difference = player.distance(vehicle.pos())
        if difference < 21:
            scoreboard.game_over()
            game_is_on = False

        if player.ycor() > 280:
            scoreboard.update_score()
            player.next_level()
            game_speed *= 0.5

    time.sleep(game_speed)
    screen.update()


screen.exitonclick()