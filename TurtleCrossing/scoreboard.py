from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-215, 250)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align='center', font=FONT)


