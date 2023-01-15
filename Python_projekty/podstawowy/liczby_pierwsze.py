
n = int(input('Podaj dowolną liczbę: '))


def prime_checker(number = n):
    is_prime = True
    for s in range(2, number):
        if number % s == 0:
            is_prime = False
    if is_prime:
        print(f'{number} to jest liczba pierwsza')
    else:
        print(f'{number} to nie jest liczba pierwsza')

prime_checker(n)
