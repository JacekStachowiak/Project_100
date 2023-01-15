
import random
from art_logo import logo
from replit import clear

print('')
print('**** WITAMY W  BLACKJACK ****')
print('-'*30)
print('')
print(logo)
print('')

kolor = ['karo', 'pik', 'kier', 'trefl']
talia = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'As', 'Król', 'Dama', 'Walet']

wynik_komp = []
wynik_user = []

def user_karty():
    """Funkcja wybiera losowo karty i dopisuje do listy wynik_user"""

    kolor_user = random.choice(kolor)
    talia_user = random.choice(talia)

    if talia_user == 'Król' or talia_user == 'Walet' or talia_user == 'Dama':
        naz = talia_user
        talia_user = 10
        wynik_user.append(talia_user)
    elif talia_user == 'As':
        naz = talia_user
        print('Wypadł As')
        user = input('Wybierasz 1 czy 11? ')
        if user == '1':
            talia_user = 1
            wynik_user.append(talia_user)
        else:
            talia_user = 11
            wynik_user.append(talia_user)
    else:
        naz = talia_user
        wynik_user.append(talia_user)

    print(f'Tasuję karty --> {naz} {kolor_user}')
    print(f'Wynik user {wynik_user} suma {sum(wynik_user)}')

def komp_karty():
    """ Funkcja wybiera losowo karty i dopisuje do listy wynik_komp """

    kolor_komp = random.choice(kolor)
    talia_komp = random.choice(talia)

    if talia_komp == 'Król' or talia_komp == 'Walet' or talia_komp == 'Dama':
        naz_2 = talia_komp
        talia_komp = 10
        wynik_komp.append(int(talia_komp))
    elif talia_komp == 'As':
        naz_2 = talia_komp
        talia_komp = 11
        wynik_komp.append(int(talia_komp))

    else:
        naz_2 = talia_komp
        wynik_komp.append(talia_komp)

    print(f'Komputer tasuje --> {naz_2} {kolor_komp}')
    print(f'Wynik kompa {wynik_komp} suma {sum(wynik_komp)}')

def poczatek():
    """Funkcja zaczyna od początku grę gdy wybrana jest opcja Y od poczatku"""
    print('')
    wynik_komp.clear()
    wynik_user.clear()
    komp_karty()


komp_karty()
while True:

    user = input('Czy chcesz wybrać kartę? Y or N ')
    print('')
    if user == 'Y':
        user_karty()
        if sum(wynik_user) > 21:
            print(f'### FURA ### - User przegrał !!!!')
            print('')
            user = input('Czy chcesz grać od początku? Y or N ')
            if user == 'Y':
                poczatek()
            else:
                print('KONIEC GRY !!!')
                break
    elif user == 'N':
        print(f'Mój wynik: {wynik_user} {sum(wynik_user)} czekam na komp-a !!! ')
        print('='*40)

        while sum(wynik_komp) <= 17:
            komp_karty()
        if sum(wynik_komp) == 21 and sum(wynik_komp) > sum(wynik_user):
            print('*** Komp Wygrał !!! ***')
            user = input('Czy chcesz grać od początku? Y or N ')
            if user == 'Y':
                poczatek()
            if user == 'N':
                print('KONIEC GRY !!!')
                break
        if sum(wynik_komp) == sum(wynik_user):
            print('Remis !!!')
            user = input('Czy chcesz grać od początku? Y or N ')
            if user == 'Y':
                poczatek()
            if user == 'N':
                print('KONIEC GRY !!!')
                break
        if sum(wynik_user) > sum(wynik_komp) and sum(wynik_user) <= 21:
            print('*** Wygrałeś ***')
            user = input('Czy chcesz grać od początku? Y or N ')
            if user == 'Y':
                poczatek()
            if user == 'N':
                print('KONIEC GRY !!!')
                break
        if sum(wynik_komp) > 21:
            print(f'### FURA ### - Komp przegrał !!!!')
            print('='*35)
            print('')
            user = input('Czy chcesz grać od początku? Y or N ')
            if user == 'Y':
                poczatek()
            else:
                print('KONIEC GRY !!!')
                break
        else:
            print('Przegrałeś !!!')
            poczatek()
