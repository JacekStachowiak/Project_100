def my_function(c=1 , a=5 , b=4):
    print(a + b + c)


my_function()  # 10  nie muszę dostarczać argumentów do funkcji
my_function(b=10)  # 16


def add(n1 , n2):
    return n1 + n2


print(add(n1=4 , n2=6))  # 10


def add_2(*args):
    for n in args:
        print(n)


add_2(3 + 4)

def add_3(*args):
    for _ in args:
        n = sum(args)
        return n

print(add_3(10,20,30))  # 60


def add_4(*args):
    print(args[0])
    suma = 0
    for n in args:
        suma += n
    return suma


print(add_4(1,2,3,4)) # index --> 4 (bo pierwsza), suma = 18

def add_5(*args):
    print(args)

add_5(1,2,3,4)