import math


"""
Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie figur:

1) prostokąta

2) kwadratu

3) trójkąta

4) trapezu

5) koła

Pamiętaj, by skorzystać z funkcji.
"""
def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h
    
