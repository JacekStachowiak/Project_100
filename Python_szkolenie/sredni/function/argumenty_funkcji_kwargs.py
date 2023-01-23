

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiplay']
    print(n)
    for key, value in kwargs.items():
        print(key, value)


calculate(2, add= 3, multiplay= 5) # {'add': 3, 'multiplay': 5}

class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.make = kwargs.get('make')  # zamiast nawiasów []
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')


my_car = Car(model='Fiat', make='125p', color='white', seats=5)
print(my_car.model)
print(my_car.make)
print(my_car.color)
print(my_car.seats)