#Getting Responce from websit using swapi.dev
#From video #42
import requests

req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()

# print(person)

for key in person:
    print(f"\n{key}:")
    if key =='films':

        value = person[key]
        for film in value:
            req = requests.get(film)
            filmName = req.json()
            print("  ",filmName['title'])
    else:
        print(f"\t{person[key]}")
