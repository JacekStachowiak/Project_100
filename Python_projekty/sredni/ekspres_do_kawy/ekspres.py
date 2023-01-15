from data import menu, resources, profit

profit = 0

def zapotrzebowanie(user):
    print(f'Produkty potrzebne do zrobienia {user}: ')
    woda_zap = menu[user]['ingredients']['water']
    kawa_zap = menu[user]['ingredients']['coffee']
    mleko_zap = menu[user]['ingredients']['milk']
    print(f'Woda: {woda_zap} ml')
    print(f'Kawa: {kawa_zap} g')
    print(f'Mleko: {mleko_zap} ml')


def koszt_kawy(user):
    koszt = menu[user]['cost']
    print(f'Koszt kawy {user} to: {koszt} PLN')


def rozliczenie(user):
    wplata = 0
    koszt = float(menu[user]['cost'])
    razem = profit

    print(f'Wrzucić monety aby zapłacić  0.5 USD, 0.25 USD, 0.10 USD, 0.05 USD, 0.01 USD')
    while wplata <= koszt:
        user = float(input('wpłać monetę:  '))
        wplata += user
        print(f'Twoja wpłata to: {wplata} PLN')
        if wplata == koszt:
            print('Zamówienie opłacone')
            razem += wplata
            return razem
        elif wplata > koszt:
            reszta = wplata - koszt
            print(f'Twoja reszta to {reszta} PLN')
            razem -= reszta
            return razem
        # else:
        #     wplata -= user
        #     print(f'Za mało środków, zamówienie nie może być zrealizowane - zwrot środków {user}')
        #     break


def raport_prod():
    woda_stan = resources['water']
    kawa_stan = resources['coffee']
    mleko_stan = resources['milk']
    print(f'Woda: {woda_stan} ml')
    print(f'Kawa: {kawa_stan} g')
    print(f'Woda: {mleko_stan} ml')

def raport_portfel():
    stan_port = (f'Stan portfela: {profit}')
    print(stan_port)

def order():
    user = input('What would you like: (espresso/latte/cappuccino) ')
    if user == 'espresso' or 'latte' or 'cappuccino':
        zapotrzebowanie(user)
        koszt_kawy(user)
        rozliczenie(user)
        raport_portfel()

order()