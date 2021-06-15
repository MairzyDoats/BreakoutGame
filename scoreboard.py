from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 280)
        self.level = 1
        self.points = 000
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 280)
        self.write(arg=f"❤{self.lives}", align="right", font=("Bebas Neue", 40, "normal"))
        self.goto(100, 280)
        self.write(arg=f"{self.points}", align="right", font=("Bebas Neue", 40, "normal"))

    def update_lives(self, lives):
        self.lives = lives
        self.update_scoreboard()

    def update_points(self, points):
        self.points += points
        self.update_scoreboard()

    def game_over_screen(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Bebas Neue", 40, "normal"))
