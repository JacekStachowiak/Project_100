import random

name_wprowadzone = input('Podaj imiona, rozdzielone . i spacja ')
names = name_wprowadzone.split(', ') 
print(names)    # ['Jack', 'Ela', 'Darek', 'Ewa', 'Kamil']
ilosc_pozycji = len(names)
print(ilosc_pozycji)
losowe_imie = random.randint(0,ilosc_pozycji-1)
imie = names[losowe_imie]
print(f'Dziś płaci {imie}')

# opcja z random.choice
name_wprowadzone2 = input('Podaj imiona, rozdzielone . i spacja ')
names2 = name_wprowadzone.split(', ') 

imie2 = random.choice(names2)
print(f'Dziś płaci {imie2}')    

# zadanie 2

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]

position = input('Where do you want to put the treasure? ')
horizontal = int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal-1] = 'X'
print(f'{row1}\n{row2}\n{row3}')


