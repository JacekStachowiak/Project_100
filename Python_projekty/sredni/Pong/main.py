from turtle import Screen
from ball import Ball
from paddles import Paddle
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=800, width=1400)
screen.bgcolor('black')
screen.title('Pong')

r_paddle = Paddle()
l_paddle = Paddle()

r_paddle.create_paddles(650, 0)
l_paddle.create_paddles(-650, 0)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()
    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
