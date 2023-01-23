

student_dict = {
    'student': ['Angela', 'James', 'Jack'],
    'score': [56, 76, 98]
}

# przegladanie słownika pętlą
for key, value in student_dict.items():
    print(key)
    print(value)

# przeglądanie df
import pandas as pd

data = pd.DataFrame(student_dict)
print(data)

# przejście pętlą przez dataframe
print('')

for key, value in data.items():
    #print(key)
    print(value)

# iterowanie przy pomocy Pandas
for (index, row) in data.iterrows():
    #print(index)
    print(row)
    print(row.student)
    print(row.score)

print('')

for (index, row) in data.iterrows():
    if row.student == 'Angela':
        print(f'Angela ma {row.score} punktów')
