import turtle
from turtle import Turtle, Screen
import random

jack = Turtle()
turtle.colormode(255)

# colors = ["red", "green", "orange", "blue", "black", "brown", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# listę kolorów mozemy zastapić losowymi RGB od 0 do 255

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

directions = [0, 90, 180, 270]
jack.pensize(15)
jack.speed('fast')    # jack.speed(10)   # 0-fastest, 10-fast, 6-normal, 3-slow, 1-slowest

for _ in range(200):
    jack.color(random_color())  # zamiast --> jack.color(random.choice(colors))
    jack.forward(25)
    jack.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
