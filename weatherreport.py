import requests
import json

# response = requests.get('https://jsonplaceholder.typicode.com/users')
# # print(response.text)

# data = json.loads(response.text)
# for person in data:
#     print(person['email'])
access_key = '42b6ced0-abbf-4089-8c78-326396a39403'
headers = {
    'X-Yandex-Weather-Key': access_key
}


response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={40.71427}&lon={-74.00597}', headers=headers)
if response.status_code == 200:
    for day in response.json()['forecasts']:
        day_temp = day['parts']['day']['temp_max']
        night_temp = day['parts']['night']['temp_max']
        date = day['date']
        weather = day['parts']['day']["condition"]
        print(f'Дата:{date}, Дневная температура: {day_temp}, Ночная температура:{night_temp}, погода: {weather}')