"""

json.dumps(data) - zapisuje dane do postaci stringowej jsona
json.dump(data, nameOfFileHandler, ensure_ascii=False) - zaposuje dane do pliku w postaci json

"""

import json

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

encodedFilm = json.dumps(film, ensure_ascii=False)
print(encodedFilm)

with open("sample.json","w",encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)