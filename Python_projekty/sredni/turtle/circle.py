import turtle
from turtle import Turtle, Screen
import random

jack = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

jack.speed('fastest')

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        jack.color(random_color())
        jack.circle(100)
        jack.setheading(jack.heading() + size_of_gap)
        jack.circle(100)

spirograph(5)

screen = Screen()
screen.exitonclick()