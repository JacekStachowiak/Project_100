from art_logo import logo


def dodawanie(n1, n2):
    return n1 + n2

def odejmowanie(n1, n2):
    return n1 - n2

def dzielenie(n1, n2):
    return n1 / n2

def mnozenie(n1, n2):
    return n1 * n2

def potega(n1, n2):
    return n1**n2


operatiors = {
    '+': dodawanie,
    '-': odejmowanie,
    '/': dzielenie,
    '*': mnozenie,
    '**': potega,
}

def calc_num1():

    print(logo)
    print('')
    print('*' * 40)
    print('')

    num1 = float(input('Wprowadź pierwszą liczbę/cyfrę: '))
    for symbol in operatiors.keys():
        print(symbol)

    while True:

        operation_symbol = input('Wprowadź operator: ')

        num2 = float(input('Wprowadź kolejną liczbę/cyfrę: '))

        calc_function = operatiors[operation_symbol]
        answer = calc_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {round(answer,2)}')
        decyzja = input(f'''Chcesz kontynuować z liczbą {round(answer),2}?  
            Y - kontynuacja
            N - new calculation
            W - ESC   ''')

        if decyzja == 'Y':
            num1 = answer
        elif decyzja == 'N':
            calc_num1()
        elif decyzja == 'W':
            break
            calc_num1()

calc_num1()



