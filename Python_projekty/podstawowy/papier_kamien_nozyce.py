# 0 - Rock, 1 - Paper, 2 - Scissors
import random

rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lista_comp = [rock, paper, scissors]
ilosc_pozycji = len(lista_comp)
comp_losowe = random.randint(0,ilosc_pozycji-1) 

gracz = int(input('Wybierz jeden z trzech symboli: rock - 0, paper - 1 lub scissors - 2.\n'))

if gracz == 0 and comp_losowe == 0:
    print(f'Wybrałeś rock {rock}  {rock} Komputer wybrał rock')
    print('')
    print('*** REMIS ***')    
if gracz == 0 and comp_losowe == 1:
    print(f'Wybrałeś rock {rock}  {paper} Komputer wybrał rock')
    print('')
    print('***PREZGRAŁEŚ***')
if gracz == 0 and comp_losowe == 2:
    print(f'Wybrałeś rock {rock}  {scissors} Komputer wybrał rock')
    print('')
    print('***WYGRAŁEŚ*** !!!')

if gracz == 1 and comp_losowe == 1:
    print(f'Wybrałeś paper {paper}  {paper} Komputer wybrał paper')
    print('')
    print('***REMIS***') 
if gracz == 1 and comp_losowe == 0: 
    print(f'Wybrałeś paper {paper}  {rock} Komputer wybrał rock ')
    print('')
    print('***WYGRAŁEŚ*** !!!')
if gracz == 1 and comp_losowe == 2: 
    print(f'Wybrałeś paper {paper}  {scissors} Komputer wybrał scissors ')
    print('')
    print('***PREZGRAŁEŚ***')

if gracz == 2 and comp_losowe == 2:
    print(f'Wybrałeś scissors {scissors}  {scissors} Komputer wybrał scissors')
    print('')
    print('***REMIS***')
if gracz == 2 and comp_losowe == 0:
    print(f'Wybrałeś scissors {scissors}  {rock} Komputer wybrał rock')
    print('')
    print('***PREZGRAŁEŚ***')
if gracz == 2 and comp_losowe == 1:
    print(f'Wybrałeś scissors {scissors}  {paper} Komputer wybrał paper')
    print('')
    print('***WYGRAŁEŚ*** !!!')
   
    
 
        

         