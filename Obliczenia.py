from tkinter import Menu
import Figury
from enum import IntEnum

"""
Za pomocą IntEnum możemy zrobić enumerację program wygląda czytelnej i trudniej jest popełnić błąd również w IntEnum może dać listę słownik itp np Menu_Figury = IntEnum('Menu_Figury',['Kwadrat', 'Prostokąt', 'Koło', 'Trójkąt', 'Trapez']) ,  albo jeśli chcemy dać inne wartości możemy użyć słownika Menu_Figury = IntEnum('Menu_Figury',{'Kwadrat': 4, 'Prostokąt' : 40, 'Koło': 30, 'Trójkąt': 12, 'Trapez': 39})
"""
Menu_Figury = IntEnum('Menu_Figury','Kwadrat Prostokąt Koło Trójkąt Trapez')
Menu_Figury2 = IntEnum('Menu_Figury',['Kwadrat', 'Prostokąt', 'Koło', 'Trójkąt', 'Trapez'])
Menu_Figury3 = IntEnum('Menu_Figury',{'Kwadrat': 4, 'Prostokąt' : 40, 'Koło': 30, 'Trójkąt': 12, 'Trapez':39})
print(list(Menu_Figury3))

wybor = int(input("""
1.Kwadrat
2.Prostokąt
3.Koło
4.Trójkąt
5.Trapez
Wybierz figurę, której pole chcesz obliczyć: """))

if wybor == Menu_Figury.Kwadrat:
    a = float(input("Podaj bok kwadratu: "))
    print(Figury.pole_kwadratu(a))

elif wybor == Menu_Figury.Prostokąt:
    a = float(input("Podaj pierwszy bok Prostokątu: "))
    b = float(input("Podaj drugi bok Prostokątu: "))
    print(Figury.pole_prostokata(a,b))

elif wybor == Menu_Figury.Koło:
    r = float(input("Podaj Promień koła: "))
    print(Figury.pole_kola(r))

elif wybor == Menu_Figury.Trójkąt:
    a = float(input("Podaj bok trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    print(Figury.pole_trojkata(a,h))

elif wybor == Menu_Figury.Trapez:
    a = float(input("Podaj pierwszy bok prostokąta: "))
    b = float(input("Podaj drugi bok prostokąta: "))
    h = float(input("Podaj wysokość trapeza: "))
    print(Figury.pole_trapezu(a,b,h))