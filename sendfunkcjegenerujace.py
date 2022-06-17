def number_multipied_by_itself():
    number = 0
    while True:
        print("start number", number)
        number = number + 1
        number =  yield number * number
        print("po yield number", number)



generatedNumbers = []

a = number_multipied_by_itself()

next(a)

"""
Wysyłamy wartośc 20 do generatora
print(a.send(20))

Czyli najpierw trzeba rozpocząć generatora komendą
next(a)
Potem możemy wysłać wartość np
a.send(30)

"""

print(a.send(20))

"""
Z użyciem tych komend możemy genererować liczby od danego momentu 
przykład poniżej
"""

for i in range(20):
    generatedNumbers.append(a.send(i))

for i in range(30,50):
    generatedNumbers.append((a.send(i)))

print(generatedNumbers)