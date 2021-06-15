from turtle import Turtle

COLORS = ["Green", "Yellow", "Red", "Purple"]


class BrickManager:

    def __init__(self):
        self.all_bricks = []

    def create_walls(self, level):
        color_index = 0
        x = -250
        y = 250
        for wall in range(level):
            for i in range(14):
                new_brick = Turtle()
                new_brick.shapesize(stretch_wid=2, stretch_len=4)
                new_brick.penup()
                new_brick.hideturtle()
                new_brick.shape("square")
                new_brick.color("black")
                new_brick.fillcolor(COLORS[color_index])
                new_brick.speed("fastest")
                new_brick.goto((x, y))
                new_brick.showturtle()
                new_brick.is_intact = True
                self.all_bricks.append(new_brick)
                x = x + 80
                if i == 6:
                    x = -250
                    y -= 40
            x = -250
            y -= 60
            color_index += 1
