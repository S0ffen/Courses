"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""




import random
from enum import Enum

def findApproximateValue(value, percentRange):
    lowestValue = value - (percentRange/100) * value
    highestValue = value + (percentRange/100) * value
    return random.randint(lowestValue,highestValue)


Event = Enum('Event', ['Chest', 'Empty'])

eventDictonary = {
                    Event.Chest : 0.6,
                    Event.Empty: 0.4

                    }

EventList= list(eventDictonary.keys())
EventProbability = list(eventDictonary.values())

Colours = Enum('Colors',{'Green' : 'Zielony', 
                         'Orange': 'pomarańczowy',
                         'Purple': 'fiolet',
                         'Gold': 'złoty'   
                        }
                        )

ChestColoursDictonary = {
                            Colours.Green: 0.75,
                            Colours.Orange: 0.2,
                            Colours.Purple: 0.04,
                            Colours.Gold: 0.01

}

chestColorList = tuple(ChestColoursDictonary.keys())
ChestColourProbability = tuple(ChestColoursDictonary.values())

rewardsForChests = {
                        chestColorList[reward]: (reward + 1) * (reward + 1) * 1000
                        for reward in range(len(chestColorList))

                    }

GameLength = 5
GoldAcquired = 0


print("Welcome to my game KOMNATA")
print("""You have only 5 steps to make, 
see yourself how much gold you gonna acquire till the end!""")

while GameLength > 0:
    GamerAnswer = input("Do you want to move forward?: ")
    if (GamerAnswer == "yes"):
        print("Great, let's see what you got...")
        DrawnEvent = random.choices(EventList,EventProbability)[0]
        if (DrawnEvent == Event.Chest):
            print("You've drawn a chest")
            DrawnChest = random.choices(chestColorList,ChestColourProbability)[0]
            print("The chest color is", DrawnChest.value)
            GamerReward = findApproximateValue(rewardsForChests[DrawnChest],10)
            GoldAcquired = GoldAcquired + GamerReward
            

        elif (DrawnEvent == Event.Empty):
            print("You've drawn nothing")

    else:
        print("You can go just straight man, nothing else")
        continue

    GameLength = GameLength - 1

print("Congratulation, you have acquired: ", GoldAcquired)








