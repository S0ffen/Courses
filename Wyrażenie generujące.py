


import sys
evenNumbers = [element
               for element in range(4400)
               if (element % 2 == 0)]

"""
Generator - pozwala na generowanie, tworzenie, wyciąganie poszczególnych elementów na bieżąco.  

Aby dostać się do wygenerowanych elementów stosujemy:
             for item in evenNumbersGenerator:    
                 print(item)

W ten sposób wypisujemy elementy ale po zakończeniu, czyli otrzymaniu przez generator elementu nie jest on zapisywany w pamięci.

Przy pomocy import sys możemy sprawdzić jakiej wielkości jest nasz generator
print(sys.getsizeof(evenNumbersGenerator))


Wyrażenie generujące tworzymy za pomocą nawiasów okrągłych ( ) używamy go kiedy dane z których pobieramy wartości są ogromne. Jest ich bardzo dużo i nie potrzebujemy przechowywać danych w pamięci komputera, a także gdy potrzebujemy skorzystać z funkcji list czyli np. dodawanie (sum), sortowanie..


"""

evenNumbersGenerator = (element
                        for element in range(4400)
                        if (element % 2 ==0)
                        )
print(sum(evenNumbersGenerator))
for item in evenNumbersGenerator:
    print(item)
print(sys.getsizeof(evenNumbersGenerator))