import art_mlotek
import replit
#import os

aukcja = {}

def max_value(aukcja):
    max_oferta = 0
    winner = ''
    for b in aukcja:
        v = aukcja[b]
        if v > max_oferta:
            max_oferta = v
            winner = b
    print('Koniec licytacji')
    print(f'The winner is {winner}, max offer {max_oferta}')

print(art_mlotek.logo)

while True:

    licytacja = input('Czy ktoś jeszcze licytuje? Y or N ')

    if licytacja == 'Y':
        replit.clear()
        name = input('Jak się nazywasz? ')
        kwota = int(input('Jaką kwotę deklarujesz? '))
        aukcja[name] = kwota

    if licytacja == 'N':
        max_value(aukcja)
        break
