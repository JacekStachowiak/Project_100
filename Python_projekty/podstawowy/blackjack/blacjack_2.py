import random
from replit import clear
from art_logo import logo

def deal_card():
    """ Return a random card from the deck"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """Pobiera listę kart i zwraca przeliczone punkty z kart"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Remis :-)'
    elif computer_score == 0:
        return 'You lose, przeciwnik ma Blackjack-a'
    elif user_score == 0:
        return 'Win with a Blackjack'
    elif user_score > 21:
        return 'You went over. Przegrałeś '
    elif computer_score > 21:
        return 'You win. Komp przegrał'
    elif user_score > computer_score:
        return 'You win, komp przegrał'
    else:
        'You lose !!!'

def play_game():

    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards {user_cards} current score {user_score}')
        print(f'Computer first card {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input('Czy chcesz kolejną kartę?  Y or N ')
            if user_should_deal == 'Y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final hands {user_cards}, final score {user_score}')
    print(f'Computer final hands {computer_cards}, final score {computer_score}')
    print(compare(user_score, computer_score))

while input('Do you want to play a BlackJack? Y or N ') == 'Y':
    clear()
    play_game()







