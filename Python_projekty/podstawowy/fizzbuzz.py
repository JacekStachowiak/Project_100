# liczba podzielna przez 3 --> fizz
# liczba podzielna przez 5 --> buzz
# liczba podzielna przez 15 --> fizzbuzz

for number in range(1,101):
    if number % 15 == 0:
        print('FIZZBUZZ !!!')
    if number % 3 == 0:
        print('FIZZ !!!')
    elif number % 5 == 0:
        print('BUZZ !!!')
    else:
        print(number)
