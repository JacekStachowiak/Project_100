import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C',
           'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# I sposob
password_list = []

for c in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for c in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for c in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list) # losowanie listy
print(password_list)

password = ''
for c in password_list:
    password += c

print(f'Your password is: {password}')

# II sposób

x = random.sample(letters, k=nr_letters)
y = random.sample(numbers, k=nr_symbols)
z = random.sample(symbols, k=nr_symbols)

secure = x+y+z
random.shuffle(secure)

password2 = ''
for s in secure:
    password2 += s

print(f'Your II password is: {password2}')




