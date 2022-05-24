import copy
"""
copy - płytkie copy
deepcopy - głębokie copy

evil_function_list(mylist.copy) jeżeli zrobimy kopie to widzimy że id są różne natomiast jeżeli nie zrobimy kopii to id są identyczne i zmiana również zachodzi na naszej główej liście

mySet ={1,4,5,78,9,3}  można tak również zrobić na secie(dictonary)
evil_function_set(myset.copy()) 

evil_function_list(mylist.copy)
print(id(toBeDestroyedList[0]))
print(id(mylist[0]))   możemy zauważyć że nawet w momencie robienia kopii id elementów w liście jest takie sam

print(id(toBeDestroyedList[0]))
toBeDestroyedList[0] = 4
print(id(toBeDestroyedList[0]))
evil_function_list(mylist.copy()) Po przypisaniu innej wartości kopii naszej listy również zachodzi zmiana w ID 


mylistOfList = [[1,4],[5,78],[9,3]]
def evil_function_ListOfList(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList[0][0] = 20

evil_function_ListOfList(mylistOfList.copy()) 
print(mylistOfList)
print(id(mylistOfList))  W tym przypadku nawet jeżeli pracujemy na kopii listy list to dojdzie do zmiany ponieważ jest lista w liście czyli tak jak wcześniej mieliśmy np [5,61,2,4] to w środku był obiekt INT czyli immutable to teraz jest [[5,61],[2,4]] jest lista w liście czyli lista jest obiektem muttable czyli zrobiliśmy kopie zewnętrzną a nie kopie wewnętrzną obiektów aby to zrobić musimy skorzystać z deepcopy a nie samego copy lecz aby z niego skorzystać trzeba zimportować biblioteke copy


evil_function_ListOfList(copy.deepcopy(mylistOfList)) Teraz możemy zauważyć że niechciana zmiana nie zaszła na naszej głównej liście lecz na jej kopii

Jest jeszcze parę sposobów strzonia kopii np:

evil_function_list(list(mylist)) kopia również będzie posiadała różne ID
evil_function_list(mylist[:]) Tutaj również kopia będzie miała różne Id od oryginału
Sposobem powyżej można również wycinać elementy ale jak sie nie poda wartości to wytnie wszystkie elementy np
evil_function_list(mylist[:]) wytnie wszystkie elementy
evil_function_list(mylist[0:3]) od 0 do 3
"""

def evil_function_list(toBeDestroyedList):
    print(id(toBeDestroyedList[0]))
    toBeDestroyedList[0] = 4
    print(id(toBeDestroyedList[0]))


def evil_function_set(toBeDestroyedSet):
    print(id(toBeDestroyedSet))
    toBeDestroyedSet.clear

def evil_function_ListOfList(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList[0][0] = 20
    print(toBeDestroyedList)

def evil_function_list2(toBeDestroyedList):
    print(toBeDestroyedList)
    print(id(toBeDestroyedList))



mylist = [1,4,5,78,9,3]
mySet ={1,4,5,78,9,3} 
mylistOfList = [[1,4],[5,78],[9,3]]
#print(id(mylist))


#print(id(mylist[0])) 
#print(mylist)

#evil_function_list(mylist.copy)
#evil_function_ListOfList(mylistOfList.copy()) 
#evil_function_ListOfList(copy.deepcopy(mylistOfList))
#print(mylistOfList)
#print(id(mylistOfList))
evil_function_list2(mylist[0:3])