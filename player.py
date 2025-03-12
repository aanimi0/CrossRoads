from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

NORD = 90
WEST = 0
EAST = 180
SOUTH = 270


class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(position)
        self.setheading(NORD)

    def next_level(self):
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def turn_nord(self):
        self.setheading(NORD)

    def turn_east(self):
        self.setheading(EAST)

    def turn_west(self):
        self.setheading(WEST)