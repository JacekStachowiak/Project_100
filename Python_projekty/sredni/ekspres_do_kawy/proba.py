

profit = 0
koszt = 5

while profit < koszt:
    user = float(input('Moneta:  '))
    profit += user
    print(profit)
    if profit == koszt:
        print('zaplacone')
    else:
        print
print(profit)