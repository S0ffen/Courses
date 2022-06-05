"""
Wyobraź sobie, że szef zlecił Ci zadanie otwarcia z jego pliku tekstowego 1500 stron i przefiltrowania ich w taki sposób,
aby podać mu tylko te, które działają. Szef chce, abyś działające strony zapisał do pliku tekstowego.

Szef nie przesłał Ci jeszcze pliku ze stronami. Wiesz tylko o tym, że będziesz musiał wykonać te zadanie następnego dnia.

Załóżmy, że tylko 300 stron z tej listy działa. Czy zrobiłbyś to wszystko ręcznie?
A może zastosowałbyś Pythona i to co do tej pory poznałeś? :)

Masz czas na zastanowienie się co zrobić do następnego dnia. Możesz napisać krótki program,
który zrobi robotę za Ciebie lub też będziesz wykonywał cały dzień żmudną robotę ;)

  i = 0
    while i <= 10:
       Sites(file.readline())
       i + 1
"""

import requests


def Sites(Link):
    Web = requests.get(Link)
    if Web.status_code == 200:
        print("Strona znaleziona", Link)
    elif Web.status_code == 404:
        print("Strona nie znaleziona", Link)


with open("Strony internetowe.txt", "r", encoding="UTF-8") as file:
    i = 0
    while i <= 11:
        Sites(file.readline())
        i + 1
