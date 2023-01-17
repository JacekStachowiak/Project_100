from turtle import Turtle, Screen

jack = Turtle()

for _ in range(15):
    jack.forward(10)
    jack.penup()
    jack.forward(10)
    jack.pendown()


screen = Screen()
screen.exitonclick()