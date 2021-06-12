from turtle import Turtle


class Brick(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.position = ()
        self.color("black")
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.speed("fastest")
        self.goto(position)

