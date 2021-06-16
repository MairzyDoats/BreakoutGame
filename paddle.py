import turtle


class Paddle(turtle.Turtle):

    def __init__(self, screen):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.goto(0, -300)
        self.showturtle()
        cv = screen.getcanvas()
        self.x = 300
        cv.bind('<Motion>', func=self.set_coordinates)

    def set_coordinates(self, event):
        self.x = event.x
        if self.x > 540:
            self.x = 540
        elif self.x < 50:
            self.x = 50

    def run(self):
        self.setposition(self.x - 300, -300)

