from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.goto(x=-250, y=250)
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game OVER!", move=False, align="center", font = FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(x = -250, y= 250)
        self.write(arg=f"Level : {self.level}", move=False, align = "left", font = FONT)

