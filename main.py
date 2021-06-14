from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
import time

PADDLE_POSITION = (0, -300)
BALL_POSITION = (0, -240)

screen = Screen()
screen.title("Breakout")
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)

brick_manager = BrickManager()
brick_manager.create_walls()

ball = Ball(BALL_POSITION, screen)
paddle = Paddle(PADDLE_POSITION, screen)

screen.listen()


is_game_on = True

while is_game_on:
    paddle.run()
    time.sleep(0.05)
    ball.move()
    screen.update()
    if (paddle.xcor() + 40) >= ball.xcor() >= (paddle.xcor() - 40) and\
            (paddle.ycor() + 10) >= ball.ycor() > -300:
        ball.bounce_y()
    elif (paddle.xcor() + 40) <= ball.xcor() <= (paddle.xcor() + 40) and (paddle.ycor() + 10) >= ball.ycor() <= -300:
        ball.bounce_x()
    for brick in brick_manager.all_bricks:
        if brick.distance(ball) < 20:
            if not brick.is_intact:
                pass
            else:
                brick.hideturtle()
                brick.is_intact = False
                ball.bounce_y()
    if ball.xcor() >= 290 or ball.xcor() <= - 290:
        ball.bounce_x()
    elif ball.ycor() >= 390:
        ball.bounce_y()
    elif ball.ycor() <= -400:
        is_game_on = False
