import time

"""
Napisz program, który policzy sumę wszystkich liczb od 1 do podanej liczby

Dla np 5.
1+2+3+4+5
zwróci
15
"""

"""
Sposób pierwszy
"""

def sumuj_do(liczba):
    suma = 0

    for liczba in range(1,liczba+1):
        suma = suma + liczba

    return suma

#print(sumuj_do(10))

"""
Sposób drugi lista słownik i generator
"""

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1,liczba+1)))


#print(sumuj_do2(5))

"""
Sposób Trzeci
"""

def sumuj_do5(liczba):
    return (1+liczba)/2 * liczba
    

def finish_timer(start):
    end = time.perf_counter()
    return(end-start)

"""Lekcja 52"""


def function_performance(func,arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start


def show_messange(message):
    print(message)

print(function_performance(sumuj_do,50000))
print(function_performance(sumuj_do2,50000))
print(function_performance(sumuj_do3,50000))
print(function_performance(sumuj_do4,50000))
print(function_performance(sumuj_do5,50000))


