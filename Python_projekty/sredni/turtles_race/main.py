from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=550, height=400)
screen.bgcolor('black')
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter color: ')
colors = ['red','yellow', 'orange', 'blue', 'green', 'purple']
y_position = [-80, -50, -20, 10, 40, 70]
all_turtles = []

meta = Turtle()
meta.pencolor('red')
meta.pensize(5)
meta.penup()
meta.goto(x=230, y=150)
meta.pendown()
meta.goto(x=230, y=-150)
meta.hideturtle()


for t_index in range(0, 6):
    new_turtles = Turtle(shape='turtle')
    new_turtles.shapesize(stretch_len=1, stretch_wid=1)
    new_turtles.color(colors[t_index])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_position[t_index])
    all_turtles.append(new_turtles)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f'You have won !!! {wining_color} is the winner')
            else:
                print(f'You have lost !!! {wining_color} is the winner !!!')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()