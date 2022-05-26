"""
Napisz funkcję, która zasymuluje jak działa lotto,
tzn wybirasz 6 UNIKALNYCH liczb z 49
"""
import random
from secrets import choice



"""
Rozwiązanie z lekcji
Sample - próbka/przykład
Sample gwarantuje unikalne wartości jeżeli nie powtarzają się one w liście 


random.sample(range(total_amount + 1),amount) Komenda ta losuje unikalne liczby z zasięgu od 49 do 6 i zmienia je w liste


Czyli tak naprawdę zrobiło to samo co ja na dole lecz szybciej i zabrało mniej linik kodu
"""

def Choose_random_numbers(amount,total_amount):
    print(random.sample(range(total_amount + 1),amount))

Choose_random_numbers(6,49)

"""
Moje rozwiązanie
"""
def Lotto(amount,total_amount):
    
    list_of_numbers = []
    i = 0
    while i < amount:
        x = random.randint(amount,total_amount)
        if x not in list_of_numbers:
            list_of_numbers.append(x)
            i += 1
            continue
            
        else:
            continue
    return list_of_numbers


#print(Lotto(6,20))
