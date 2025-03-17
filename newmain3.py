import requests

access_key = '42b6ced0-abbf-4089-8c78-326396a39403'

headers = {
    "X-Yandex-Weather-Key": access_key
}

query = """{
  weatherByPoint(request: { lat: 52.37125, lon: 4.89388 }) {
    now {
      temperature
    }
  }
}"""

response = requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query})

print(response.content)