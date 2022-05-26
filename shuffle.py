"""
shuffle - zmnienia kolejność elementów w liście
            (Działa na oryginale)

"""

import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace"
            "Joker", "Joker"]


random.shuffle(cardList)

print(cardList)



