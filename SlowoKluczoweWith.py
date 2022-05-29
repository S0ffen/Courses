"""
Z komendą with możemy usunąć jedną linike mianowicię file.close(), 
ponieważ z komendą with plik zamknię się sam po wykonaniu swojej funkcji,
również plik zamknię się mimo errora
"""


with open(file = open("Test2.txt", "w")) as file:
    file.write("sample")

