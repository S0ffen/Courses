def add():
    c = 5 # zmienna lokalna czyli istnieje w miejscu funkcji która została stworzona (istnieję w ciele funkcji)





def add2():
    global c # jeżeli chcemy dostać się do globalnego zasięgu 
    c = c + 4
    print(c)

c = 1 #zmienna globalna 

add2()

print(c) # jeżeli użyjemy global (variable) znaczy to również że operujemy na globalnej wartości np global c