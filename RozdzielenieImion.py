"""
ĆWICZENIE:

Wczytaj imiona i nazwiska z pliku o nazwie:
imionanazwiska.txt

1) rozdziel je tak, by powstała lista krotek, gdzie wewnętrzne krotki to
pary imiona/nazwiska
2) zapisz imiona do pliku imiona.txt
3) zapisz nazwiska do pliu nazwiska.txt

Zastanów się jak rozwiązać problem,
gdy nie ma podanego nazwiska w pliku imionanazwiska.txt, gdy będziesz
zapsywał nazwiska do pliku nazwiska.txt


[
 ("Arkadiusz", "Włodarczyk"),
 ("Jakis", "Ziom")
]
"""

NamesAndSurnames = []

with open("imionanazwiska.txt","r",encoding="UTF-8") as file:
    for line in file:
        NamesAndSurnames.append(tuple(line.replace("\n","").split(" ")))
    print(NamesAndSurnames)

with open("imiona.txt","w",encoding="UTF-8") as file:
    for item in NamesAndSurnames:
        file.write(item[0] + "\n")

"""
Sposób pierwszy

with open("Nazwiska.txt","w",encoding="UTF-8") as file:
    for item in NamesAndSurnames:
        if len(item) == 2:
            file.write(item[1] + "\n")
        else:
            file.write("\n")
"""

"""
Sposób drugi - Czytelniejszy i bardziej profesjonalny
"""  
with open("Nazwiska2.txt","w",encoding="UTF-8") as file:
    for item in NamesAndSurnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")
