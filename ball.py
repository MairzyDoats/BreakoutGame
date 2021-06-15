from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.time_sleep = 0.05
        self.speed("fastest")
        self.goto(0, -240)
        self.showturtle()
        self.x_move = random.choice([-10, -8, 8, 10])
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.hideturtle()
        self.goto(0, -240)
        if self.y_move < 0:
            self.y_move *= -1
        self.showturtle()
