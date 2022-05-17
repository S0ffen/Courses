""" return - zwrócić, pozwala na modyfikacje zwróconej wartości,  None - nic - false, return kończy funkcje tak samo jak break"""

def pole_prostokata(a, b):
    return a * b

poleProstokataA = pole_prostokata(2, 8)
poleProstokataB = pole_prostokata(24, 2)
#print("Pole prostokąta = ", poleProstokataA)
#print(5 * poleProstokataB)

def dzielenie(a, b):
    if (b == 0):
        return
    print("aaaa")
    return a / b
    

x = dzielenie(10, 5)
if (x):
    print("Podzielono poprawnie", x)
else:
    print("Coś poszło nie tak")
