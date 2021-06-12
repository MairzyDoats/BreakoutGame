from turtle import Screen
from paddle import Paddle
from brick import Brick


class Main:
    def __init__(self):

        screen = Screen()
        screen.title("Breakout")
        screen.setup(width=600, height=800)
        screen.bgcolor("black")
        cv = screen.getcanvas()
        self.p = Paddle((0, -300))
        self.x = 300
        cv.bind('<Motion>', func=self.set_coordinates)
        self.run()

    def set_coordinates(self, event):
        self.x = event.x

    def run(self):
        while True:
            self.p.setposition(self.x-300, -300)


def create_wall():
    x = -250
    y = 300
    for i in range(34):
        position = (x, y)
        color = "Green"
        Brick(position, color)
        x = x + 30
        if i == 16:
            x = -250
            y = y - 20


create_wall()


m = Main()

