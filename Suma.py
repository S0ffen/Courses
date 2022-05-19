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


start = time.perf_counter()
print(sumuj_do(2355555))
end = time.perf_counter()
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do2(2355555))
end = time.perf_counter()
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do3(2355555))
end = time.perf_counter()
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do4(2355555))
end = time.perf_counter()
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do5(23555))
end = time.perf_counter()
print(finish_timer(start))


