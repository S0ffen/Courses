import pprint
import webbrowser
import requests
import json
from datetime import datetime, timedelta

"""

API - Application Programming Interface

timestamp - znak czasu 
od 1 stycznia 1970 w sekundach 

"""

timeBefore = timedelta(days=10)

searchDate = datetime.today() - timeBefore


params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": int(searchDate.timestamp()),
    "tagged": "python",
    "min": 15,
}

r = requests.get('https://api.stackexchange.com/2.3/questions/', params)


try:
    questions = r.json()
except json.JSONDecodeError:
    print("Nie poprawny format")
else:
    for questions in questions["items"]:
        webbrowser.open_new_tab(questions['link'])
