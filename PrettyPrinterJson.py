"""
indent - dodaje wcięcia

sort_keys=True - Sortuje alfabetycznie

with open("sample.json","w",encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False, indent=4) - w ten sposób również plik zostanie zapisany w czytelniejszy sposób



Te dwie komendy robią mniej więcej to samo czyli pokazują kod z jsona w czytelniejszy sposob
lecz ten 2, jest prostszy i szybszy i zajmuje mniej linijek kodu,
Sposob 1
print(json.dumps(wynik, indent=4, ensure_ascii=False, sort_keys=True))
Sposob 2
pprint.pprint(wynik)

"""

import json
import pprint

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
    }
}


encodedFilm = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)
#print(encodedFilm)

with open("sample.json","w",encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False, indent=4)

with open("sample.json","r",encoding="UTF-8") as file:
    wynik = json.load(file)

#print(json.dumps(wynik, indent=4, ensure_ascii=False, sort_keys=True))
pprint.pprint(wynik)