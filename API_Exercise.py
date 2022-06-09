import requests
import webbrowser
import json
import pprint

params = {
    'amount': 5,
    'animal_type': 'cat'

}

r = requests.get('https://cat-fact.herokuapp.com/facts/random',params)

try:
    content = r.json()
except json.JSONDecodeError:
    print("Nie poprawny format")
else:
    for cat in content:
        print(cat['text'])