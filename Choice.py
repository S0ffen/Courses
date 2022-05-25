"""
choice - zwraca losowy element
choices - zwraca listę elementów i ma większe możliwości

Zastosowanie komendy choices
random.choices(nagrodaZeSkrzynki, [80 ,15 ,4 ,1] ,k = 100) najpierw podajemy z czego ma losować w tym przypadku nagrodaZeSkrzynki potem możemy  podać szanse (szansę mogą być również w ułamkach typu 0.8) na dany  przedmiot nie musimy go podawać lecz jak go nie podamy szanse będą takie same w tym przypadku mamy 
[80 ,15 ,4 ,1] a na końcu podajemy ile razy ma losować czyli k = 100

"""
import random
from collections import Counter

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia"]

nagrodaZeSkrzynki =["zielona","pomarańczowa","purpurowa","legendarna"]

#print(random.choice(movieList)) #losowanie tytułu każdy ma taką samą szansę

print(Counter(random.choices(nagrodaZeSkrzynki, [80 ,15 ,4 ,1] ,k = 100)))