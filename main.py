from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

is_game_continue = True
while is_game_continue:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 :
        ball.bounce_x(r_paddle.towards(ball))

    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x(l_paddle.towards(ball))

    # Detect R paddle misses
    if ball.xcor() > 400:
        ball.reset_position(-1, -1)
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -400:
        ball.reset_position(1, 1)
        scoreboard.r_point()

screen.exitonclick()
