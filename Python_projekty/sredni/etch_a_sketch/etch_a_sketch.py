from turtle import Turtle, Screen

jack = Turtle()
screen = Screen()

def move_forward(): # w
    jack.forward(10)

def move_backward():
    jack.backward(10)

def turn_left():
   new_heading = jack.heading()+10
   jack.setheading(new_heading)


# def turn_left():
#     jack.left(90)

def turn_right():
    new_heading = jack.heading()-10
    jack.setheading(new_heading)

# def turn_right():
#     jack.right(90)

def clear():
    jack.clear()
    jack.penup()
    jack.home()
    jack.pendown()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
