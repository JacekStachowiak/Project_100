import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
futro = data['Primary Fur Color']
gray = len(data[futro == 'Gray'])
cinnamon = len(data[futro == 'Cinnamon'])
black = len(data[futro == 'Black'])


print(f'Gray {gray}')
print(f'Cinnamon {cinnamon}')
print(f'Black {black}')

data_dict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Count': [gray, cinnamon, black]
}

df = pd.DataFrame(data_dict)
df.to_csv('Squirrel_count.csv')


