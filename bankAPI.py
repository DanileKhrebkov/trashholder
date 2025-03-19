import json
import requests


# response = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js')
# date = response.json()["Timestamp"].split("T")
# print(date)
# for valute, value in response.json()["Valute"].items():
#     nameValute = value["Name"]
#     valueValute = value["Value"]
#     print(f'({valute} {nameValute}, значение: {valueValute})')

response = requests.get('https://favqs.com/api/qotd')
if response.status_code == 200:
    print(response.json()["quote"]["body"])
    print(response.json()["quote"]["author"])
else:
    print('Соединение с сервером прервано:', response.status_code, response.text)