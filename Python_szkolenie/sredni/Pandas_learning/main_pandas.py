import pandas as pd
# pandas.pydata.org/docs/

data = pd.read_csv('weather_data.csv')
print(data)
print('')
print(data['temp'])
print('')
print(type(data))
data_dict = data.to_dict()
print(data_dict)

lista_temp = data['temp'].to_list()
print(lista_temp)
ilosc = len(lista_temp)

avg = sum(lista_temp)/ilosc
print(round(avg, 2))  # 17.43

avg_2 = data['temp'].mean()
print(round(avg_2, 2))

max_data = data['temp'].max()
print(max_data)

min_data = data['temp'].min()
print(min_data)

mediana_data = data['temp'].median()
print(mediana_data)

# get data in columns
con = data['condition']
con2 = data.condition   # inny sposób
print(con)
print(con2)

# get data in row
m1 = data[data.day == 'Monday']
m2 = data[data['day'] == 'Monday']
print(m1)
print(m2)

# pobierz dane z max temperaturą
max_temp = data.temp.max()
print(max_temp)
max_temp_row = data[data.temp == max_temp]
max_temp_row_2 = data[data.temp == data['temp'].max()]
print(max_temp_row)
print(max_temp_row_2)
print('')
monday = data[data.day == 'Monday']
print(monday)
print(monday.condition)

# challenge --> temp Monday

monday = data[data.day == 'Monday']
far = monday.temp * 9/5 + 32
print(far)
print(f'Temperatura wynosi: {int(monday.temp)} stopni Celsjusza tzn {int(far)} F')

# Create dataframe from scratch

data_dict = {
    'students' : ['Emy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data_3 = pd.DataFrame(data_dict)
print(data_3)
data_3.to_csv('new_data.csv')

