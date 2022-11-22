#The IN operator
#From Video #34

#in operartor used to check if there is a match in any kind of array

food = ['apple', 'orange', 'banana']

print(food)
user = input("Select a food: ")

if user.lower() in food:
    print("good choise")
else:
    print("Wrong answer try again!")

print("\nTesting in operator in Dictopnary Key")
person = {
    "name":"mohamed",
    "age": "41",

}

print("\nTesting in operator in Dictopnary Values")
if 'name' in person:
    print("name is found in dictionary Key")
else:
    print("Error not found")

if 'mohamed' in person.values():
    print("mohamed is found in dictionary Vale")
else:
    print("Error not found")

name = "Mohamed Abdullah Hassan"

if 'Hassan' in name:
    print("Hassan is found in String")
else:
    print("Error not found")
