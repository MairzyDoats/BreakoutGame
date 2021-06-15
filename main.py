from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
from scoreboard import Scoreboard
import time

PADDLE_POSITION = (0, -300)
PADDLE_WIDTH = 50
PADDLE_HEIGHT = 20

BRICK_WIDTH = 50
BRICK_HEIGHT = 30


screen = Screen()
screen.title("Breakout")
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)

brick_manager = BrickManager()

ball = Ball()
paddle = Paddle(PADDLE_POSITION, screen)

scoreboard = Scoreboard()

screen.listen()

new_game = True

while new_game:
    is_game_on = True
    level = 1
    score = 0
    lives = 3
    brick_manager.create_walls(level)
    destroyed_bricks = []
    speed_factor = 0.03

    while is_game_on:
        paddle.run()
        time.sleep(speed_factor)
        ball.move()
        screen.update()
        if (paddle.xcor() + PADDLE_WIDTH) >= ball.xcor() >= (paddle.xcor() - PADDLE_WIDTH) and \
                (paddle.ycor() + PADDLE_HEIGHT) >= ball.ycor() > -300 and ball.y_move < 0:
            ball.bounce_y()
        elif (paddle.xcor() + PADDLE_WIDTH) <= ball.xcor() <= (paddle.xcor() + PADDLE_WIDTH) and \
                (paddle.ycor() + PADDLE_HEIGHT) >= ball.ycor() <= -300 and ball.ycor() >= -310:
            ball.bounce_x()
        for brick in brick_manager.all_bricks:
            if not brick.is_intact:
                pass
            elif (brick.ycor() + BRICK_HEIGHT) >= ball.ycor() >= (brick.ycor() - BRICK_HEIGHT) and \
                    (brick.xcor() + BRICK_WIDTH) >= ball.xcor() >= (brick.xcor() - BRICK_WIDTH):
                if brick.xcor() + BRICK_WIDTH == ball.xcor() and brick.ycor() + BRICK_HEIGHT == brick.ycor() or \
                        brick.xcor() - BRICK_WIDTH == ball.xcor() and brick.ycor() + BRICK_WIDTH == brick.ycor():
                    ball.bounce_y()
                elif brick.xcor() + BRICK_WIDTH == ball.xcor() or brick.xcor() - BRICK_WIDTH == ball.xcor():
                    ball.bounce_x()
                else:
                    ball.bounce_y()
                brick.hideturtle()
                brick.is_intact = False
                destroyed_bricks.append(brick)
                scoreboard.update_points(20)
        if ball.xcor() >= 290 or ball.xcor() <= - 290:
            ball.bounce_x()
        elif ball.ycor() >= 390:
            if ball.y_move < 0:
                pass
            else:
                ball.bounce_y()
        elif ball.ycor() <= -400:
            lives -= 1
            scoreboard.update_lives(lives)
            if lives == 0:
                for brick in brick_manager.all_bricks:
                    brick.hideturtle()
                brick_manager.all_bricks = []
                scoreboard.game_over_screen()
                is_game_on = False
            ball.reset()
            screen.update()
            time.sleep(1)

        if len(destroyed_bricks) == len(brick_manager.all_bricks):
            if level >= 4:
                level = 1
                if speed_factor > 0.01:
                    speed_factor -= 0.01
            else:
                level += 1
                speed_factor -= 0.002
            brick_manager.create_walls(level)
            scoreboard.update_points(300)
            ball.reset()
            screen.update()
            time.sleep(1)
