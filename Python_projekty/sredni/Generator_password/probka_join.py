import json

my_tuple = ('John', 'Peter', 'Vicky')

x = '#'.join(my_tuple)
print(x)    # John#Peter#Vicky
x = ','.join(my_tuple)
print(x)    # John,Peter,Vicky


my_list = ['John', 'Peter', 'Vicky']
x = '#'.join(my_list)
print(x)    # John#Peter#Vicky
x = ','.join(my_list)
print(x)    # John,Peter,Vicky
x = ''.join(my_list)
print(x)    # JohnPeterVicky

with open('data.json', 'r') as data_file:
    data = json.load(data_file)

website = 'Amazon'
message = data[website]

print(message)