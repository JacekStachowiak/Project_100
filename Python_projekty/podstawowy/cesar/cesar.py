# poprawiony plik
from logo_cesar import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
shuold_continue = True
while shuold_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def cesar(direction, text, shift):
        end_text = ''
        if direction == 'encode':
            shift *= -1
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                end_text += alphabet[new_position]
            else:
                end_text += letter
        print(f'Wiadomość {direction} to "{end_text}"')

    shift = shift % 26
    cesar(direction, text, shift)

    result = input('Napisz Yes jeżeli chcesz zakończyć albo naciśnij enter !!!')
    if result == 'Yes':
        shuold_continue = False
        print('Do widzenia')





