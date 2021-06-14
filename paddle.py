import turtle


class Paddle(turtle.Turtle):

    def __init__(self, position, screen):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.position = ()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.showturtle()
        cv = screen.getcanvas()
        self.x = 300
        cv.bind('<Motion>', func=self.set_coordinates)

    def set_coordinates(self, event):
        self.x = event.x

    def run(self):
        self.setposition(self.x - 300, -300)
