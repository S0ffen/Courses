"""

yield - z ang. dostarczyć ,dać ,wydać z siebie

return znaczy też zakończenie funkcji

generate_even_numbers_wrong() - zadziała źle ponieważ,
wyjdzie 0 % 2 = 0 i zakończy się funkcja
"""

def generate_even_numbers_wrong():
    for element in range(400):
        if element % 2 == 0:
            return element

def generate_even_numbers():
    for element in range(400):
        if element % 2 == 0:
            yield element

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0))

a = generate_even_numbers()
print(next(a),next(a),next(a))
"""
dwie rzeczy poniżej robią to samo i to zależy od nas
co jest bardziej czytelniejsze lub czy chcemy coś co jest szybsze
"""
def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x + 1

print(list(generate_10_numbers()))

generate_10_numbers_expresion = (x
                         for x in range(10))

print(list(generate_10_numbers_expresion))
