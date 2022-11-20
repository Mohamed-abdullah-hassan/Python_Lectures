# For Loop in python from Video #24

fav_food = ['Pizza', 'Burger', 'Shawerma', 'Tacos', 'Kofta']

#Using for _item in dataset 
for food in fav_food:
    if food == 'Pizza':
        size = input("What Pizza size would you like?")
        print(f"You like {size} Pizza!")
    elif food == 'Burger' or food =='Shawerma':
        type = input(f"Your {food}, do you like Cheken or Meat? ")
        size = input(f"What {type},{food} size would you like?")
        print(f"You like {size} {type},{food}!")
    else:
        print (f"You Like {food}")

# to iterate in dictionary item

userInfo = {
    'Name': "Mohamed",
    'ID'  : "1234567",
    'email': "myemail@email.com",
    'FaceBook': '/mohamed',
    'twitter' : '@kdok',
}

print("\nIterating and printring Dctionary directly")
for value in userInfo:
    print(f"User info is : {value}")

print("\nIterating and printring Dctionary using items()")
for key, value in userInfo.items():
    print(f"User {key} is : {value}")

print("\nIterating and printring Dctionary using values()")
for value in userInfo.values():
    print(f"User is : {value}")

print("\nIterating and printring Dctionary using keys()")
for key in userInfo.keys():
    print(f"User dictionary item: {key}")
