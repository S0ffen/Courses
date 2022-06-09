import requests
import json
import webbrowser
import pprint

"""

Api Key - jest to coś co identyfikuje nas jako użytkownika
Niektóre strony tego wymagają by wiedzięć kto robi ile requestow itp 
ze strony
https://calendarific.com/

"""


params = {
    "api_key": '', # tutaj wstawiamy nasz klucz
    "country": 'pl',
    "year": "2022",
    "month": "12",


}

r = requests.get('https://calendarific.com/api/v2/holidays/',params)

try:
    content = r.json()
except json.JSONDecodeError:
    print("Nie poprawny format")
else:
    pprint.pprint(content)