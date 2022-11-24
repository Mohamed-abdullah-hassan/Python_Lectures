#Getting Dictionary Values
#From Video #51

person1 = {
    'name':'michel',
    'age' : 40,
    'kids' : ['john', 'sally', 'kress'],
    'ocupation' : 'worker',
}

pesron2 = {
    'name' : 'Fuddel',
    'age' : '25',
    'ocupation' : 'technitian'
}

Person3 = {
    'name' : 'Somer',
    'age' : 33,
    'kids' : ['sweet', 'mary', 'kane'],
    'ocupation' : 'House Wife'
}

myList = [person1,pesron2,Person3]

for name in myList:
    print(f"{name.get('name')}, is {name.get('age') } years old, and Ocupation of: {name.get('ocupation',)}, and has {name.get('kids', 'no kids')}")
