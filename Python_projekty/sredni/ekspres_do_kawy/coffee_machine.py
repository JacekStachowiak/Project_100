from data import menu, resources, profit

profit = 0
def zasoby_wystarczajace(order_ingredients):
    """Returns zamówienie gdy są składniki i False gdy brakuje"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry, nie możemy przyjąć zamówienia, brak {item}')
            return False
    return True

def process_coins():
    """Returns sumę włożonych monet"""
    print('Please insert coins. ')
    total = int(input('How many quarters?:  ')) * 0.25  # tworzy zmienną reszta do niej dodaje
    total += int(input('How many dimes?:  '  )) * 0.1
    total += int(input('How many nickles?:  ')) * 0.05
    total += int(input('How many pennies?:  ')) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True gdy płatność jest zaakceptowana i False jeżeli jest za mało środków"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f'Here is ${change} in change - reszta')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry, środków jest za mało')
        return False


def make_coffee(drink_name, order_ingredients):
    """Celem jest odjęcie składników od posiadanych surowców"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕. Enjoy!!! ')


is_on = True
while is_on:
    choice = input('What would you like: (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':  # alt_shift
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]} g')
        print(f'Money: ${profit} ')
    else:
        drink = menu[choice]
        if zasoby_wystarczajace(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])






