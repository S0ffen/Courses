"""
    obiekt to zmienna, która ma więcej możliwości, można wywołać na nim "funkcje"
    może mieć więcej niż 1 wartość

    obiekty immutable: bool, int, float, tuple, str

    immutable - niezmienne
    mutable - zmienne

    = ZMIANA miejsca wskazywania na nowy adres, na inny obiekt


"""
def sectionA():
    a = 4

    listSample =[1, 4, 512, 24]
    print(id(listSample))

    listSample2 = listSample # mutable czyli zmienna
    print(id(listSample2)) # id jest takie samo jak u listSample czyli (id listSample=listSample2)


    listSample2.append(465) # do obu list doda się 465
    listSample2[0] = 7 # tak samo działa dla indeksów

    print(listSample)
    print(listSample2)

    a = 4
    b = a # immutable nie zmienna
    print(id(b)) 
    b = 7
    print(id(b)) # b posiada dwa różne id pomimo przypisania do a

    print(a)
    print(b) # imutable ponieważ b tutaj będzie równe 7 

    k = 4
    h = 4
    # id k i h będą takie same ponieważ mają taką samą wartość print(id(k)), print(id(h))


c = 5
#print(id(c))

def add(c, amount = 1):
    print(id(c))
    c = c + amount
    print(id(c)) # widzimy że zmiana id nastąpiła dopiero po dodaniu mimo tego że są to zmienna lokalna i globalna

#add(c)

listSample =[1, 4, 512, 24]
def append_elemnt_to_list(list,element):
    print(id(list))
    list.append(element)
    print(id(list))

#print(id(listSample)) # widzimy że w tym przypadku id list jak i listsample jest ciągle takie samo
#append_elemnt_to_list(listSample,5)


def append_elemnt_to_list2(list,element):
    print(id(list))
    list = [2, 4, 20]
    print(id(list))
print(id(listSample)) # Tutaj widzimy że id się zmieniło bo użyliśmy znaku równości
append_elemnt_to_list2(listSample,5)
