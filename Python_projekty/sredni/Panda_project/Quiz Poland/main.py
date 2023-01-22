import turtle

screen = turtle.Screen()
screen.title('Miasta Polska --> Quiz')
image = 'poland.gif'

screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title='MIASTA WOJEWÓDZKIE', prompt="Wpisz nazwę miasta wojewódzkiego")



# def get_mouse_click(x , y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)

turtle.mainloop() # --> alternatywa co niżej
# screen.exitonclick()