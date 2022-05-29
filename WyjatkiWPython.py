"""
print(0/0) ZeroDivisionError
tab = [1,2] 
print(tab[4]) IndexError
"""

file = open("Test2.txt", "w")
print(0/0)
#plik się stworzył ale nie doszło do napisania słowa sample ani do zamknięcia pliku bo w połowie zdarzył się error 
file.write("sample")
file.close() 

"""
Aby uniknąć takich problemów jak wyżej że plik się stworzył ale nie zapisał nic w środku i się nie zamknął używamy sposobu poniżej
"""
try:
    file = open("Test2.txt", "w")
    print(0/0)
    a = 5 # możemy zobaczyć że a wogule tutaj nie istnieje bo wszystko co jest po errorze się nie wykona
    file.write("sample")
finally:
    file.close()
    a = 5 # temu możemy stworzyć a tutaj i ono się już stwrozy mimo errora powyżej
