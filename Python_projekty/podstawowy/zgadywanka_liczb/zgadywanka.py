from art_logo import logo
from random import randint

# http://patorjk.com/software/taag/#p=display&h=3&f=Graffiti&t=Type%20Something%20

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(komp_liczba, user_liczba, turns):
    if user_liczba > komp_liczba:
        print(f'Podałeś {user_liczba} - Twoja liczba jest za duża')
        return turns - 1
    elif user_liczba < komp_liczba:
        print(f'Podałeś {user_liczba} - Twoja liczba jest za mała')
        return turns - 1
    else:
        print('***  Zgadłeś, You win !!!!  ***')

def set_difficulty():
    level = input('Jaki poziom trudności wybierasz? easy or hard ')
    if level.lower() == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print('Welcome to the Number Guessing Game')
    print("'I'm thinking of a number between 1 and 100")
    komp_liczba = randint(1,100)
    print(f'Psss, The correct answer is: {komp_liczba}')

    turns = set_difficulty()
    print(f'You have {turns} tries')

    user_liczba = 0
    while user_liczba != komp_liczba:

        user_liczba = int(input('Podaj swoją liczbę 1-100: '))
        turns = check_answer(komp_liczba, user_liczba, turns)
        if turns == 0:
            print('You have run out of liczba, you lose ')
            return
        elif user_liczba != komp_liczba:
            print('Play again')

game()

