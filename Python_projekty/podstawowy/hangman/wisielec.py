import random
from art_hangman import logo, stages
from words import list_words
import os

end_of_game = False
# losowanie słów
word_list = list_words
stag = stages
logo = logo

print(logo)
print('Zaczynamy grę')

word = random.choice(word_list)
word_length = len(word)
lives = 6

# print(f'Wybrane słowo to: {word}')

display = []
for _ in range(word_length):
    display += "_"
# litera użytkownika

while not end_of_game:
    litera_user = input('Wpisz literę. ').lower()

    os.system('cls')
    # print("\033[H\033[J", end="")

    if litera_user in display:
        print(f"Twoja litera jest w słowie {litera_user}")

    for position in range(word_length):
        litera = word[position]
        # print(f'Current position {position}\n Current letter {litera}\n Litera użytkownika {litera_user}\n')
        if litera == litera_user:
            display[position] = litera

    if litera_user not in word:
        print(f'Wprowadziłeś {litera_user}, litery nie ma w słowie. Straciłeś życie')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('### You lose !!! ###')
            print(f'Szukane słowo to: {word}')

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('*** You win !!! ***')
        print(f'Szukane słowo to: {word}')

    print(stag[lives])


