import webbrowser

import requests
import json
import pprint


def get_Json_Content_from_Response(response):
    try:
        content = response.json()
    except json.JSONDecodeError:
        print("Nie poprawny format" ,response.text)
    else:
        return content


def get_favorite_cats(userId):
    params = {
        "sub_id" : userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites',params, headers=headers)
    return get_Json_Content_from_Response(r)

def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
    return get_Json_Content_from_Response(r)[0]


def add_favorite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId

    }
    r = requests.post('https://api.thecatapi.com/v1/favourites',json=catData,
                      headers=headers)
    return get_Json_Content_from_Response(r)

def remove_favorite_cat(userId, favoriteCatId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/'+favoriteCatId,
                      headers=headers)

    return get_Json_Content_from_Response(r)


headers = {
    "x-api-key": "here you put your APIKEY"
}


"""

Logowanie przez nagłowek czyli header

strona : https://docs.thecatapi.com/favourites

"""

r = requests.get('https://api.thecatapi.com/v1/favourites',headers=headers)






userId = "agh2m"
name = "Adrian"

print("Witaj " + name)
favoriteCats = get_favorite_cats(userId)
print("Twoje ulubione kotki to ", favoriteCats)

randomCat = get_random_cat()
print("Wylosowano kotka" , randomCat['url'])

addToFavorites = input("Czy chcesz dodać go do ulubionych T/N: ")

if addToFavorites.upper() == 'T':
    resultFromAddingFavoriteCat = add_favorite_cat(randomCat['id'], userId)
    newlyAddedCat = {resultFromAddingFavoriteCat["id"]: randomCat['url']}
else:
    print("No to lipa kotek będzie smutny")
    newlyAddedCat = ()

favoriteCatById = {
    favoriteCat['id']: favoriteCat["image"]['url']
    for favoriteCat in favoriteCats

}
favoriteCatById.update(newlyAddedCat)

print(favoriteCatById)

catToRemove = input("Czy chcesz usunąć kotka z ulubionych? Podaj jego id: ")

print(remove_favorite_cat(userId,catToRemove))
webbrowser.open_new_tab(favoriteCats[0]['image']['url'])