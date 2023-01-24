
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
