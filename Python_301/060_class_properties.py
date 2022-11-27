#Class Properties
#From Video #60

class Animal:
    kindome = "Mamuls"
    powers = {
        'speed kmh' : '25'
    }
    color = ['white', 'black','brown']
    _private_test = "This is a private propertie that can't be accessed outside the class"

animal = Animal()

print(animal.kindome)
print(animal.powers)
print(animal.color[0])
# print(animal._private_test)
