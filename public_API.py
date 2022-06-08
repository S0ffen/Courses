import pprint

import requests
import json

"""

API - Application Programming Interface

"""

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": "2022-05-15",
    "tagged": "python",
    "min": 15,
}

r = requests.get('https://api.stackexchange.com/2.3/questions/', params)

try:
    questions = r.json()
except json.JSONDecodeError:
    print("Nie poprawny format")
else:
    pprint.pprint(questions)