import turtle


class Paddle(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.position = ()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.goto(position)

