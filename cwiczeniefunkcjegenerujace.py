""" Stwórz funkcję generującą w nieskończoność kolejne liczby przemnożone przez siebie tzn.:

1

4

9

16

25

36

Skorzystaj z funkcji generującej generując 20 elementów, po czym wróć od momentu skończenia i wygeneruj następnie 30 kolejnych liczb.

Zapisz wygenerowane elementy w tej samej liście.

"""
import pprint


def number_multipied_by_itself():
    number = 0
    while True:
        number = number + 1
        yield number * number

generatedNumbers = []

a = number_multipied_by_itself()
print(next(a),next(a),next(a))

for i in range(30):
    generatedNumbers.append(next(a))
pprint.pprint(generatedNumbers)