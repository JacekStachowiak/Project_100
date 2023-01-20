from turtle import Screen
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard

h = 600
w = 800

screen = Screen()
screen.setup(height=h, width=w)
screen.bgcolor('black')
screen.title('Pong')

r_paddle = Paddle()
l_paddle = Paddle()
r_paddle.create_paddles((h-250), 0)
l_paddle.create_paddles((-h+250), 0)

ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard((-w/2)+300, (h/2)-120, (w/2)-300, (h/2)-120)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor() > ((h/2)-20) or ball.ycor() < ((-h/2)+20):
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > ((w/2)-80) or ball.distance(l_paddle) < 50 and ball.xcor() < ((-w/2)+80):
        ball.bounce_x()
    # detect r_paddle misses
    if ball.xcor() > ((w/2)-20):
        ball.reset_position()
        scoreboard.l_point((-w/2)+300, (h/2)-120, (w/2)-300, (h/2)-120)
    # detect l_paddle misses
    if ball.xcor() < ((-w/2)+20):
        ball.reset_position()
        scoreboard.r_point((-w/2)+300, (h/2)-120, (w/2)-300, (h/2)-120)

screen.exitonclick()
