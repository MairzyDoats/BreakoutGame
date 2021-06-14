from turtle import Turtle

COLORS = ["Green", "Yellow", "Red", "Purple"]
NUMBER_OF_WALLS = 3


class BrickManager:

    def __init__(self):
        self.all_bricks = []

    def create_walls(self):
        color_index = 0
        x = -250
        y = 300
        for wall in range(NUMBER_OF_WALLS):
            for i in range(26):
                new_brick = Turtle()
                new_brick.shapesize(stretch_wid=1, stretch_len=2)
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
                x = x + 40
                if i == 12:
                    x = -250
                    y -= 20
            x = -250
            y -= 40
            color_index += 1
        print(self.all_bricks)
