#Converting String containning json info into usable json dictionary
#From video #43
import json

char = '''{
    "name": "C-3PO", 
    "height": "167", 
    "mass": "75", 
    "hair_color": "n/a", 
    "skin_color": "gold", 
    "eye_color": "yellow", 
    "birth_year": "112BBY", 
    "gender": "n/a", 
    "homeworld": "https://swapi.dev/api/planets/1/", 
    "films": [
        "https://swapi.dev/api/films/1/", 
        "https://swapi.dev/api/films/2/", 
        "https://swapi.dev/api/films/3/", 
        "https://swapi.dev/api/films/4/", 
        "https://swapi.dev/api/films/5/", 
        "https://swapi.dev/api/films/6/"
    ], 
    "species": [
        "https://swapi.dev/api/species/2/"
    ], 
    "vehicles": [], 
    "starships": [], 
    "created": "2014-12-10T15:10:51.357000Z", 
    "edited": "2014-12-20T21:17:50.309000Z", 
    "url": "https://swapi.dev/api/people/2/"
}'''

print(type(char))

char= json.loads(char)
print(char)

print(type(char))

print(char)
print('\nNow we can use it as a Dictionary')
print(f'The Name is : {char["name"]}')
print ("Changing name to Sweet_Nana")
char['name'] = "Sweet_Nana"

char = json.dumps(char)
print(type(char))

print(char)
