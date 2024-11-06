from ast import Param

import requests

while True:
    api = 'a3aacad1d98bce12f727060c2632025f'
    city = input('Введите город: ')

    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid='+api+''

    weather_data = requests.get(url).json()

    print('Сейчас в городе', city, weather_data['main']['temp'], '°C')
    print('Ощущается как', weather_data['main']['feels_like'], '°C')