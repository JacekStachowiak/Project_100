from art_logo import logo
import random

# http://patorjk.com/software/taag/#p=display&h=3&f=Graffiti&t=Type%20Something%20

print(logo)

print('Welcome to the Number Guessing Game')
print("'I'm thinking of a number between 1 and 100")
komp_liczba = random.randrange(1,101)

ilosc_prob = 0
def proba():
    user = input('Jaki poziom trudności wybierasz? easy or hard ')
    global ilosc_prob
    if user.lower() == 'easy':
        ilosc_prob = 10
        print(f'You have {ilosc_prob} tries')
    else:
        ilosc_prob = 5
        print(f'You have {ilosc_prob} tries')
def compare():
    global ilosc_prob
    user_liczba = int(input('Podaj swoją liczbę 1-100: '))

    if user_liczba > komp_liczba:
        ilosc_prob -= 1
        print(f'Podałeś {user_liczba} - Twoja liczba jest za duża')
        print(f'Pozostało {ilosc_prob} prób')
    elif user_liczba < komp_liczba:
        ilosc_prob -= 1
        print(f'Podałeś {user_liczba} - Twoja liczba jest za mała')
        print(f'Pozostało {ilosc_prob} prób')
    else:
        print('***  Zgadłeś, You win !!!!  ***')
        user = input('Czy chcesz zagrać od poczatku? Y or N ')
        if user == 'Y':
            ilosc_prob = 0
            proba()
        else:
            print('Koniec gry !!!!')
            ilosc_prob == 0

proba()
while ilosc_prob != 0:

    compare()
    if ilosc_prob == 0:
        print('Przegrałeś - brak dodatkowych szans')
        user = input('Czy chcesz zagrać od poczatku? Y or N ')
        if user == 'Y':
            ilosc_prob = 0
            proba()
        else:
            print('Koniec gry !!!!')
            ilosc_prob == 0



