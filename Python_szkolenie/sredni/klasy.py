class User1:
    pass

user1 = User1()
user1.id = '001'
user1.username = 'Angela'
print(user1.username)  # Angela

user2 = User1()
user2.id = '002'
user2.username = 'Jack'
print(user2.username)


# aby nie pisać kilku użytkowników, z wieloma atrybutami używamy konstruktora

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1     # my obserwujemy - jego liczba wzrasta o 1
        self.following += 1     # samoobserwacja - liczba samoobserwacji także o 1


new_user1 = User('001', 'Jacek')
new_user2 = User('002', 'angela')
print(new_user1.username)
print(new_user1.id)
print(new_user2.username)
print(new_user2.id)

print(new_user1.followers)
new_user1.follow(new_user2)
print(new_user1.followers)  # nie ma obserwatora
print(new_user1.following)  # obserwuje
print(new_user2.followers)  # ma obserwatora
print(new_user2.following)  # nie obserwuje

class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats  = 2

my_car = Car(5)  # to samo
my_car.seats = 5
my_car.enter_race_mode()
