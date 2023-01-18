from turtle import Turtle, Screen

jack = Turtle()
screen = Screen()

def move_forward():
    jack.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_forward)  # bez nawiasów gdy przekazujemy do innej funkcji
screen.exitonclick()


