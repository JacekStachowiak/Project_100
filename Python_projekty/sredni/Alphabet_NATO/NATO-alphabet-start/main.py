import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
data.to_dict()

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():

    word = input('Enter your name(word): ').upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, tylko litery mogą być !!!')
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()