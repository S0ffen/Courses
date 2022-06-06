import requests
import json

"""
chcemy mieć user id i ilość ukończonych tasków i wybrać tego co ma najwięcej np:
{
userId 1 : 11
userId 2 : 9 
itd

}

"""

"""
Poniżej jest dobrze rozwiązane zadanie lecz mało czytelne
"""


r = requests.get('https://jsonplaceholder.typicode.com/todos')
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Nie poprawny format")
else:
    completedtasksFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedtasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedtasksFrequencyByUser[entry["userId"]] = 1
    userIdWithMaxCompletedTasks = []
    maxAmountOfCompletedTasks = max(completedtasksFrequencyByUser.values())
    for userId, NumberOfCompletedTasks in completedtasksFrequencyByUser.items():
        if (NumberOfCompletedTasks == maxAmountOfCompletedTasks):
            userIdWithMaxCompletedTasks.append(userId)
#print(userIdWithMaxCompletedTasks)

"""
Sposob 2 bardziej czytelniejszy z użyciem funkcji (w taki sposób powinien wyglądać kod)
"""


r = requests.get('https://jsonplaceholder.typicode.com/todos')

def count_Task_Frequency(tasks):
    completedTasksFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTasksFrequencyByUser[entry["userId"]] = 1
    return completedTasksFrequencyByUser

def get_keys_with_top_values(my_dict):
    return [
        key
        for (key,value) in my_dict.items()
        if value == max(my_dict.values())
     ]


def user_With_Top_Completed_Tasks(completedTaskFrequencyByUser):
    userIdWithMaxCompletedTasks = []
    maxAmountOfCompletedTasks = max(completedTaskFrequencyByUser.values())
    for userId, NumberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if (NumberOfCompletedTasks == maxAmountOfCompletedTasks):
            userIdWithMaxCompletedTasks.append(userId)
    return userIdWithMaxCompletedTasks


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Nie poprawny format")
else:
    completedtasksFrequencyByUser = count_Task_Frequency(tasks)
    userWithTopCompletedTasks = user_With_Top_Completed_Tasks(completedtasksFrequencyByUser)
    #print("Wręczamy ciasteczko mistrzunia dyscypliny o id: ",userWithTopCompletedTasks)

print(get_keys_with_top_values(completedtasksFrequencyByUser))
"""

Lekcja 85 mamy już kto ma najlepszy wynik i teraz chcemy mu wysłać to ciasteczko
ale żeby tego dokonać musimy znać jego imie itp

Sposob 1 jest dobry dla małej ilości danych jakby było w milionach to by było wolniejsze



r = requests.get('https://jsonplaceholder.typicode.com/users')

users = r.json()
for user in users:
    if user["id"] in userWithTopCompletedTasks:
        print("Wręczamy ciasteczko mistrzunia dyscypliny o imieniu: ", user['name'])

"""


"""
Lekcja 86

Sposob 2

"""

for userId in userWithTopCompletedTasks:
    r = requests.get('https://jsonplaceholder.typicode.com/users/'+str(userId))
    user2 = r.json()
    print("Wręczamy ciasteczko mistrzunia dyscypliny o imieniu: ", user2['name'])
