
import time




def function_performance(func, arg, how_many_times = 1):

    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

"""
Napisać funkcje i sprawdzić czy dana liczba znajduję się w Pojemniku jak równiez sprawdzić co jest szybsze
"""

"""
Moje rozwiązanie
"""
def FirstContainer(Number):
    if Number in setContainer:
       return Number
    else:
        return False


def SecondContainer(Number):
    if Number in listContainer:
        return Number
    else:
        return False

#print(function_performance(FirstContainer,500,50))
#print(function_performance(SecondContainer,500,50))

"""
Rozwiązanie z lekcji
Wniosek: jak chcemy zobaczyć czy dany element znajduję się w zmiennej to przeszukanie po set - {} zajmie mniej czas niz przeszukanie po liście - []
"""


"""
Przeszukanie listy działa tak że jak jest lista [1,2,3,4,5,6,7] to idzie pokolei po każdej liczbę co znaczy że tym większa lista tym gorzej.
Set - {} ma na odwrót tym większy set tym lepiej

"""
def is_element_in(what_value):
    if what_value in setContainer:
        return True
    else:
        return False

print(function_performance(is_element_in,450,500))

