
print('Welcome to the tip calculator')

rachunek_calkowity = input('Ile wyniósł całkowity rachunek? ')
procent_napiwku = input('Jaki % napiwku chciałbyś dać: 10, 12, or 15? ')
osoby = input('Na ile osób dzielisz rachunek? ')

rachunek_na_osobe = float(rachunek_calkowity)/float(osoby)
procent_napiwku_value = float(rachunek_calkowity) * (float(procent_napiwku)/100)
napiwek_na_osobe = float(procent_napiwku_value)/float(osoby)
zaplac = rachunek_na_osobe + napiwek_na_osobe

print(f'Każda osoba powinna załacić {"%.2f" % round(zaplac,2)} PLN')        # Każda osoba powinna załacić 36.60 PLN
print('Każda osoba powinna załacić {:.2f}'.format(round(zaplac,2)), 'PLN')  # Każda osoba powinna załacić 36.60 PLN

# %.2f % --> mamy 2 miejsca po przecinku nawet jeżeli wynik to 36.6 - 36.60
