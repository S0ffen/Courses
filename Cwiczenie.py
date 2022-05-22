
import time


"""
dodaliśmy * przed arg co umożliwi nam sprawdzenie wydajności funkcji która ma więcej niż 1 argument działa to pokolei np 
print(function_performance(is_element_in,450,setContainer,how_many_times=500)) is_element_in idzie do func dalej 450 idzie do arg dalej setContainer idzie do arg i jeżeli na końcu nie byłoby how_many_times=500 tylko samo 500 też poszło by do arg czyli wszystkie nienazwane argumenty lądują w arg

Aby uniknąć takich problem można zmienić niektóre rzeczy np
def function_performance(func, *arg, how_many_times = 1): ---> def function_performance(func, how_many_times = 1,*arg):
    teraz będzie to działało tak że pierwsze dwa argumenty idą do func i how_many_times a reszta do arg

Równiez trzeba pamiętać że jeżeli mamy taką formę funkcji def function_performance(func, how_many_times = 1,*arg) to nie możemy zapisywać argumentów do niej w taki sposób ---> function_performance(is_element_in,500, what_value=300, container=setContainer)) jeżeli chcielibyśmy zapisać w taki sposób musimy dodać drugą * do arg czyli zrobić coś takiego :
    def function_performance(func, how_many_times = 1,**arg) i również tutaj dodać gwiazdkę func(**arg)



ARGUMENTY POZYCYJNE (NIENAZWANE) PRZED ARGUMENTAMI NAZWANYMI 
RÓWNIEŻ WAŻNE JEŻELI ZROBIMY TAK JAK WYŻEJ CZYLI *arg TO ARG ZMIENIA SIĘ W KROTKE CZYLI MOŻEMY DO TEGO ODWOŁAĆ NP print(arg[0])
JEŻELI CHCEMY SIĘ ODWOŁAĆ ALE DO **arg TRZEBA UŻYC print(arg.get("what_value")) JEST TO RÓWNIEŻ DICTONARY
"""

def function_performance(func, how_many_times = 1, **arg):
   
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

"""
Napisać funkcje i sprawdzić czy dana liczba znajduję się w Pojemniku jak równiez sprawdzić co jest szybsze
"""



"""
Rozwiązanie
Wniosek: jak chcemy zobaczyć czy dany element znajduję się w zmiennej to przeszukanie po set - {} zajmie mniej czas niz przeszukanie po liście - []

Przeszukanie listy działa tak że jak jest lista [1,2,3,4,5,6,7] to idzie pokolei po każdej liczbę co znaczy że tym większa lista tym gorzej.
Set - {} ma na odwrót tym większy set tym lepiej

"""
def is_element_in(what_value,container):
    if what_value in container:
        return True
    else:
        return False

print(function_performance(is_element_in,500,what_value=300,container=setContainer))
print(function_performance(is_element_in,500,what_value=300,container=listContainer))
