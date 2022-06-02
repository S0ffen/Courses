"""
podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie,
                        jeśli nie to stworzy
a - A ppend (dopisywanie)

mnogie tryby otwierania plików:
r+ - do czytania i pisania

file.read file.write

w+ - do pisania i czytania
różni sie tym, że usunie zawartość istniejącego pliku
lub stworzy plik gdy go nie było

a+ - "wieczny tryb" dopisywania i przy okazji czytania
UWAGA! wskaźnik dopisywania jest zawsze na końcu
jeśli plik nie istniał - stworzy go

Możemy zauważyć że file tell zawsze nam powie że jesteśmy na końcu naszego dokumentu,
dopóki nie użyjemy komendy file.seek() np chcemy być na początku to file.seek(0)

print(file.tell())
file.write("Ocean Arka")
print(file.tell())

Jesteśmy również w stanie dopisać coś do końca i zobaczyć np pierwsza linikę tekstu 
    file.write("Ocean Arka")
    file.seek(0)
    print(file.readline())
    

Tutaj jest ciekawy przypadek:
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write("Ocean Arkadiusza Wielkiego") - Ponieważ pomimo skoku do początku dokumentu (file.seek(0)) to ostatnia komenda czyli (file.write("Ocean Arkadiusza Wielkiego")) i tak dopisze ten tekst na końcu dokumenty dlatego tryb "a+" jest nazywany trybem wiecznego dopisywania.

"""

with open("Oceany.txt","a+") as file:
    file.write("Ocean Arka")
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write("Ocean Arkadiusza Wielkiego")
