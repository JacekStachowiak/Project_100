from random import randint, choice, shuffle
import pyperclip

def gen_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C',
               'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    nr_letters = randint(8,15)
    nr_symbols = randint(2,5)
    nr_numbers = randint(2,5)

    password_list = [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]
    # for c in range(nr_numbers):
    #     password_list.append(random.choice(numbers))

    shuffle(password_list)


    password = ''.join(password_list)   # to samo niżej
    pyperclip.copy(password)

    return password


    # password = ''
    # for c in password_list:
    #     password += c




# # II sposób
#
# nr_letters = random.randint(8,10)
# nr_symbols = random.randint(2,4)
# nr_numbers = random.randint(2,4)
#
# secure = x+y+z
# random.shuffle(secure)
#
# password2 = ''
# for s in secure:
#     password2 += s
#
# print(f'Your password is: {password2}')




