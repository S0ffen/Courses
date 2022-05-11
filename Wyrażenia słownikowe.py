names = {"Arkadiusz","Wioletta","Karol","Bartłomiej","Jakub","Ania"}

numbers = [1,2,3,4,5,6]

celcius = {"tl": -20,"t2": -15, "t3": 0, "t4": 12, "t5": 24}

namesLenght = {
    name : len(name)
    for name in names
    if name.startswith("A")
}
#print(namesLenght)

multipedNumbers = {
    number : number * number
    for number in numbers

}
#print(multipedNumbers)


"""
Zmiana temperatury na fahrenheita
"""

fahrenheit = {
    key: celcius* 1.8 + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20
}

print(fahrenheit)