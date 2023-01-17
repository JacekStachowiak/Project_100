from turtle import Turtle, Screen

jack = Turtle()
jack.shape('turtle')
jack.color('red')
jack.pencolor('red')
jack.pensize(5)

for _ in range(4):
    jack.forward(100)
    jack.left(90)

# jack.forward(100)
# jack.left(90)
# jack.forward(100)
# jack.left(90)
# jack.forward(100)
# jack.left(90)


screen = Screen()
screen.exitonclick()