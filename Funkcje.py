"""
    Funkcja - to blok kodu do którego można odwołać się
              w każdej chwili, aby otrzymać pożądany przez nas wynik.

    definition


    def nazwa_funkcji():
       instrukcja1
       instrukcja2

    nazwa_funkcji()
   
"""

def wiadomosc_powitalna(imie):
    print("Cześć,",imie,"miło mi powitać Cię w moim programie!")
    

imiona = ["Arku", "Wiolu", "Bartku"]

for imie in imiona:
    wiadomosc_powitalna(imie)

