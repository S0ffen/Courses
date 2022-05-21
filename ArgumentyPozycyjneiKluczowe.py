"""
    Argumenty kluczowe i pozycyjne 
    kluczowy - w postaci: klucz - wartość (domyślny)
    pozycyjne - takich, których liczy się kolejność przy wywołaniu
"""

"""
Arguemnty pozycyjne to takie które nie mają przypisanej wartości
"""
def greet(name, message, separator = " "):
    print(message,name, sep=separator) # sep oznacza separation czyli co ma być pomiedzy tekstami (\n oznacza enter)

# greet(message="Witaj",name="Arek") zastosowanie 
greet("Arek","Witaj","\n")
greet("Wiola","\n")

print("tralalal","aaaa","bbb",sep="\n") # sep= jest kluczowy bo ma wartość