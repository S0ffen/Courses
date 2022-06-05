"""

pip - pip installs packages - instalator pakunków

PyPi - Python packages index - indeks (spis) pakunków do Pythona

<Response [404]> - oznacza że nie prawidłowo podaliśmy link i strona nie istnieje(nie została znaleziona)

<Response [200]> - oznacza to że strona została znaleziona i wszystko jest w porządku

"""

import requests

response = requests.get("http://videokurs.pl")


def WebSites(Link):
    Web = requests.get(Link)
    if Web.status_code == 200:
        print("Strona znaleziona")
    elif Web.status_code == 404:
        print("Strona nie znaleziona")


#WebSites('http://videokurs.pl')
print(response.text)