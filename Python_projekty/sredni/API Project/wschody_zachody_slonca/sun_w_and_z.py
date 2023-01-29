import requests
from datetime import datetime


MY_LAT = 52.732201
MY_LONG = 15.237570

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

URL = 'https://api.sunrise-sunset.org/json'
response = requests.get(URL, params=parameters)
response.raise_for_status()
status = response.status_code
data = response.json()

time_now = datetime.now()
sunrise = data['results']['sunrise']        # wschod_slonca
sunset = data['results']['sunset']          # zachod_slonca
solar_noon = data['results']['solar_noon']  # słoneczne południe
day_length = data['results']['day_length']  # długość dnia

print(f'Wschód słońca {sunrise}')
print(f'Zachód słońca {sunset}')
print(f'Południe: {solar_noon}')
print(f'Długość dnia: {round(day_length/3600,2)}')

print(f'Czas teraz {time_now.hour}')



