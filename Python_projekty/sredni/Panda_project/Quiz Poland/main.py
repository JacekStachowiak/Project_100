import turtle

screen = turtle.Screen()
screen.title('Zamki Polska  Quiz')
image = 'zamki.gif'

screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name?")
def get_mouse_click(x , y):
    print(x, y)

turtle.onscreenclick(get_mouse_click)

turtle.mainloop() # --> alternatywa co niżej
# screen.exitonclick()