# mała, duża, średnia
# dodać peperoni lub sera lub oba

# small pizza = 15
# medium pizza = 20
# large pizza = 25

# add pepperoni small pizza = +2
# add pepperoni medium or large pizza = +3
# extra chees for any size = +1
# pokaż rachunek 

print('Welcome to Python Pizza Deliveries')
size = input('What size pizza do you want? S, M or L. ')
# pepperoni = input('Do you want pepperoni? Y or N. ')
#cheese = input('Do you want extra chees? Y or N. ')

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

pepperoni = input('Do you want pepperoni? Y or N. ') 
if pepperoni == 'Y' and size == 'S':
    bill += 2
elif pepperoni == 'Y' and (size == 'M' or size == 'L'):
    bill += 3

cheese = input('Do you want extra chees? Y or N. ')                   
if cheese == 'Y':
    bill += 1
print(f'Your bill is {bill} PLN')    
    
# a and b
# a or b
# not a
