liczby = [1,2,3,4,5,6]
'''
Sposób Pierwszy
'''
potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if (element % 2) == 0:
        liczbyParzyste.append(element)

#print(potegiDwojki)
#print(liczbyParzyste)

'''
Sposób drugi (działa szybciej)
'''

potegiDwojki2 = [element**2 
                for element in liczby]
#print(potegiDwojki2)

liczbyParzyste2 = [element
                    for element in liczby
                    if element % 2 == 0]

print(liczbyParzyste2)