"""
PLIK - nazwana lokacja, która przechowuje na STAŁE dane na dysku.

RAM - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWO

tell - Komenda ta mówi nam w którym momencie pliku jesteśmy po ilości znaków (Enter liczy się podwójnie bo enter to \n czyli dwa znaki) np  
    with open ('Oceany.txt',"r",encoding='UTF-8') as file:
    print(file.readline())
    print(file.tell()) - pokaże nam 12 bo jesteśmy na 12 znaku bo Atlantycki ma 10 znaków + Enter który ma 2


seek - Komenda ta pozwala nam pominąć daną ilość znaków np
    with open ('Oceany.txt',"r",encoding='UTF-8') as file:
    file.seek(4)
    print(file.readline()) - w tym momencie pominie on 4 pierwsze znaki z początku liniki
    

"""




with open ('Oceany.txt',"r",encoding='UTF-8') as file:
    file.seek(4)
    print(file.readline())
