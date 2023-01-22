import turtle
import pandas as pd


screen = turtle.Screen()

screen.title('U.S.A Quiz')
screen.setup(height=500, width=750)
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_state = data.state.to_list()

list_states = []

while len(list_states) < 50:

    answer_state = screen.textinput(title=f'{len(list_states)}/50 States Correct',
                                    prompt="What's another state's name?").title()

    if answer_state in all_state:
        list_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        t.goto(x, y)
        t.write(answer_state)
        # t.write(state_data.state.item())    # bez śmieci



screen.mainloop()
# screen.exitonclick()
