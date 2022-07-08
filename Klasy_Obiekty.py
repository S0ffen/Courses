"""
OOP - Object Oriented Programming tj. programowanie zorientowane wokół obiektów

Obiekt - to pojemniki do przechowywania zmiennych i funkcji tematycznie ze sobą powiązanych do dalszego ponownego użycia.

Klasy - foremki (szablony) do tworzenia egzemplarzy obiektów.

Atrybut - cecha opisująca obiekt

Metoda - funkcja operująca na obiekcie, opisuje akcje, czasowniki

Instancja klasy - (z ang. instance) to obiekt, który wyszedł z formy(klasy)


Obiekt posiada atrybuty np. 

OKNO - długość, szerokość, wysokość, kolor

Na obiektach można wykonywać akcje/czynności np. otwieranie, zamykanie, uchylenie itp. 


Jak tworzyć klasę?

Aby stworzyć klasę w Pythonie piszemy słówko class oraz podajemy jej nazwę, następnie stawiamy dwukropek. Po enterze i wcięciu określamy stworzoną klasę np. 

class User:
      pass


pass - słowo, które wpisujemy, po to aby móc w późniejszym czasie zastąpić te miejsce kodem


Atrybuty klasy np.

seba.age = 16
mirek.age = 22


Odwołanie do atrybutu 

print(seba.age)


Gdy stworzymy nową zmienną niepowiązaną z klasą o takiej samej nazwie:

age = 40


to nie będzie miała ona wpływu na atrybuty “age” w obiektach
"""


class User():
    age = 0


Seba = User()
Mirek = User()

Mirek.age = 10

print(Seba.age)
print(Mirek.age)
print(type(Mirek))