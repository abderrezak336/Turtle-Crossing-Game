from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-120, 250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-120, 250)
        self.write(f"Level : {self.level}", align="right", font=FONT)



    def increas_level(self):
        self.level += 1
        self.update_scoreboard()



    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 50, "normal"))
