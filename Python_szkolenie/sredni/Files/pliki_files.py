
# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# r --> read()
# w --> write()
# a --> dopisanie


with open('my_file.txt', mode='a') as file:
    file.write('\nNew text')

with open('new_file.txt', 'w') as f:
    f.write('\nZnowu ja')

with open('new_file.txt') as f:
    contents = f.read()
    print(contents)




