"""
random()     0 <= x < 1 lub [0,1) losuję liczby od 0 do 0.999999 nie włączając 1

uniform(2.5, 10.0) 2.5 <= x < 10.0 lub [2.5, 10.0) czyli tak samo jak wyżej od 2.5 do 10 

randrange(10) wylosuje liczby z puli (0,1,2,3,4,5,6,7,8,9)

randrange(0, 15, 2) wylosuje parzyste liczby z puli (0,2,4,6,8,10,12,14)

randint(0,4) [0,4] tutaj mamy  możliwość wylosowania (0,1,2,3,4) 


"""

import random

# x = 0
# while x < 100:
#     x += 1
#     print(random.uniform(0,100)) 

def will_weapon_hit(weaponChance):
    isHitChance = random.uniform(0,100)
    if(isHitChance < weaponChance):
        return "hit"
    else:
        return "not hit"

print(will_weapon_hit(10))

x = 0

listhit = []

while x < 100:
    x = x + 1
    listhit.append(will_weapon_hit(10))



from collections import Counter

dictionaryHit = Counter(listhit)

print(dictionaryHit)

print(random.randrange(10))# tutaj jest od 0 do 10 bez 10

print(random.randint(0,10)) # a tutaj jest od 0 do 10 z 10 włącznie
