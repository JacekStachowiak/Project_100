'''
def function_a():
    .....
def function_b():
    .....

function_a(function_b) --> bez nawiasów
'''

def add(n1,n2):
    return n1 + n2
def subtrack(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

def calculator(n1, n2, func):
    return func(n1, n2)

wynik = calculator(2,3,add)
wynik2 = calculator(3,4,divide)
wynik3 = calculator(3,4,multiply)
print(wynik)
print(wynik2)
print(wynik3)


