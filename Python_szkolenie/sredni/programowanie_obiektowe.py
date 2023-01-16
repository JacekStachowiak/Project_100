from turtle import Turtle, Screen
from prettytable import PrettyTable

# wcześniej programowanie proceduralne
# teraz obiektowe
# atrybuty --> zmienne
# metody --> funkcje

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
#my_screen.exitonclick()

# tabela
table = PrettyTable()
table.add_column('Pokemon Name',['Pikatchu', 'Squatrie', 'Charmander'],'l') # do lewej
table.add_column('Type',['Electric', 'Fire', 'Water'],'r') # do prawej

# align - l(left), c(centre), r(right)
table.align = 'l'
table.align = 'r'
table.align = 'c'

print(table)
