"""
Znajdź liczby od 2 do 470 włącznie które są:
-podzielne przez 7, ale nie są podzielne przez 5
"""

"""
Sposób z lekcji generator nie zabiera duzo pamieci 
"""
x = range(2,471)
numbers = (q for q in x if q % 7 == 0 and q % 5 != 0)
for number in numbers:
    print(number)


"""
Mój sposób lista łatwy dostęp do danych
"""
a = [i for i in x if i % 7 == 0 and i % 5 != 0 ]
#print(a)

