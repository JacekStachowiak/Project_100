from turtle import Turtle, Screen
import random

jack = Turtle()

colors = ['red', 'green', 'orange', 'blue', 'black', 'brown']
def figury(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        jack.forward(100)
        jack.left(angle)


for side in range(1,11):
    jack.color(random.choice(colors))
    figury(side)


screen = Screen()
screen.exitonclick()

