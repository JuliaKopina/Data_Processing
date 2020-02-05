"""Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."""

import requests
import json

main_link = 'http://api.travelpayouts.com/v2/prices/latest?token='

token = 'f79dae63d33165665a8c5e5b34d8a604'

params = {'origin': 'WMI',
          'destination': 'WRO',
          'depart_date': '2020-03-07',
          'return_date': '2020-03-27',
          'number_of_changes': 0,
          'value': 1183,
          'distance': 298}

response = requests.get(main_link+token,params=params)

if response.ok:
    data = json.loads(response.text)

    with open('success.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f'success.json сохранен!')