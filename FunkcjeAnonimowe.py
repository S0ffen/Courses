"""
Funkcja anonimowa Lambda np:
lambda x: x * 2

Poniżej mamy dwie funkcje które robią to samo
def podwoj(x):
    return x*2 
    
lambda x: x * 2

Tak można wywołać funkcje lambda
test = lambda x: x * 2
print(test(4))

Można wywołać tą funkcje również w taki
print((lambda x: x * 2)(4))

Lambdy używamy kiedy nie chcemy robić jakieś funkcji tylko chcemy szybko np przefiltrować dane np:
my_list = [2, 14, 22, 7, 6, 4, 5, 17]
my_list_filtered = list(filter(lambda z: z % 2 == 0, my_list))

Możemy to rónież zrobić w taki sposób:
my_list = [2, 14, 22, 7, 6, 4, 5, 17]
def funkcja_dla_przefiltruj(x):
    if (x % 2) == 0:
        return x

my_list_filtered2 = list(filter(funkcja_dla_przefiltruj, my_list)) 
Lecz sposób powyżej z lambda zajmuje mniej miejsca i jest bardziej czytelny, ta funkcja będzie użyta tylko raz
"""
def podwoj(x):
    return x*2
#print(podwoj(4))

test = lambda x: x * 2
#print(test(4))
#print((lambda x: x * 2)(4))


my_list = [2, 14, 22, 7, 6, 4, 5, 17]

my_list_filtered = list(filter(lambda z: z % 2 == 0, my_list))
#print(my_list_filtered)

def funkcja_dla_przefiltruj(x):
    if (x % 2) == 0:
        return x

my_list_filtered2 = list(filter(funkcja_dla_przefiltruj, my_list))

print(my_list_filtered2)