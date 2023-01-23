import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
data.to_dict()

word = input('Enter your name(word): ').upper()

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

output_list = [nato_dict[letter] for letter in word]
print(output_list)

