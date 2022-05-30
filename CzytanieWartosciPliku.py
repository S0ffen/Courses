"""
read

readline - pozwala czytać plik po linice (czyta cała linie jedna za kazdym wywołaniem) np 
oceany2 = file.readline() - przeczyta pierwsza linię pliku 
oceany3 = file.readline() - przeczyta druga linie pliku

readlines - też zamieni zawartość pliku w listę lecz zachowa \n(backslash n) czyli poprostu entery


splitlines - komenda ta powoduje że zmienia zawartość pliku w listę 
encoding="UTF-8" - komenda ta powoduje że znaki polskie typu ł,ó,ż działają poprawnie


"""

with open("Oceany.txt", "r", encoding="UTF-8") as file:
    #oceany2 = file.readline()
    #oceany3 = file.readline()
    oceany4 = file.readlines()
    oceany = file.read().splitlines()


#print(oceany4)

"""
Możemy też zastosować pętle for żeby przeczytać linie
"""
with open("Oceany.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)