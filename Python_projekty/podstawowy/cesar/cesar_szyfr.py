
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    szyfr_code = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        szyfr_code += new_letter
    print(f'Twoja wiadomość zakodowana to {szyfr_code}')


def decrypt(code_text, shift_amount):
    szyfr_decode = ''
    for letter in code_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        szyfr_decode += new_letter
    print(f'Twoja wiadomość odkodowana to {szyfr_decode}')


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
if direction == 'decode':
    decrypt(code_text=text, shift_amount=shift)








