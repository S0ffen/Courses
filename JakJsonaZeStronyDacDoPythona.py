"""

Jsonplaceholder - miejsce zastępcze na twój przyszły json

"""

import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/todos')
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Nie poprawny format")
else:
    print("Wszystko jest ok")
    print(tasks[0])

