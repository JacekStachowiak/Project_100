
PLACEHOLDER = '[name]'

with open(r'Input/Names/invited_names.txt', 'r') as name_file:
    names = name_file.readlines()
    print(names)

with open('Input\\Letters\\starting_letter.txt', 'r') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'Output\\ReadyToSend\\letter_for_{stripped_name}.txt', 'w') as invitation_letter:
            invitation = invitation_letter.write(new_letter)






