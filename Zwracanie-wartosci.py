""" return - zwrócić, pozwala na modyfikacje zwróconej wartości,  None - nic - false, return kończy funkcje tak samo jak break.
"""

def pole_prostokata(a, b):
    return a * b

poleProstokataA = pole_prostokata(2, 8)
poleProstokataB = pole_prostokata(24, 2)
#print("Pole prostokąta = ", poleProstokataA)
#print(5 * poleProstokataB)

def dzielenie(a, b):
    if (b == 0):
        return
    print("aaaa")
    return a / b
    

x = dzielenie(10, 5)
if (x):
    print("Podzielono poprawnie", x)
else:
    print("Coś poszło nie tak")

"""
Notatki z lekcji 46
Słowo return jak sama nazwa wskazuje z ang. powraca do miejsca wywołania.

Miejsce wywołania jest decydowane przez Ciebie.

Jeśli napiszesz w kodzie:

poteguj(2, 3);

to miejsce, w którym to napiszesz, jest miejscem gdzie ta funkcja zostaje wywołana.

Po tym gdy wywołasz funkcję komputer przeskakuje do deklaracji funkcji (def). Następnie komputer wykonuje wszystkie instrukcje wewnątrz funkcji aż do momentu napotkania "return", czyli powrotu do miejsca wywołania. Miejsce, gdzie została funkcja wywołana jest zastępowane przez to co jest po słówku return.

Wywołanie oznacza, wykonanie/przeskoczenie do funkcji i jej rozpoczęcie.
"""