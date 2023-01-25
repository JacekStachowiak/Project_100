
# fileNotFound --> mamy zapisany FileNotFoundError dlatego łapie też bład słownika
try:
    with open('a_file.txt') as file:
        file.read()
    a_dictionary = {'key': 'value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    print('Brak takiego pliku --> zostanie utworzony')
    with open('a_file.txt', 'w') as file:
        file.write('Wiadomosc zapisana')
except KeyError as error_message:
    print(f'Nie ma takiego klucza: {error_message}')
else:
    with open('a_file.txt') as file:
        content = file.read()
        print(content)
finally:
    # raise KeyError('Ten błąd zgłosiłem sam --> błąd klucza')
    print('Finaly - To jest zawsze realizowane')
    # file.close()

# Raising Exceptions --> własne wyjątki
# np.BMI podajemy wagę i wzrost
# przy podaniu wzrostu 45 m nie ma błędu technicznego, BMI zostanie policzone, ale taka osoba nie istnieje i tu możemy zrobć wyjątek
wzrost = 4

if wzrost > 3:
    raise ValueError('Osoba nie może mieć więcej jak 3 m')




# key error
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_key']

# index error
# fruit_list = ['Aple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# type error
# text = 'abc'
# print(text + 5)

# try:
#
# except:
#
# else: --> jeżeli wszystko powyżej zostanie wykonane
#
# finally: --> działa zawsze



