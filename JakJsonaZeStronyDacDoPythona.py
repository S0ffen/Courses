"""

Jsonplaceholder - miejsce zastępcze na twój przyszły json

Można załadować ten plik na dwa sposoby
Sposób 1
tasks = json.loads(r.text)
Sposob 2
tasks = r.json()
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

