#Python Datastructures Tuples From Video #014

#Tuples are Restricted List which means that it can't be changed onese created
#To create a tuple we use ( and ) with , seperated elements for python to understand its a tuple
#the last , is not mendatory except for backward compatapility with older version of python
food = ("Pizza", 'Chicken', 'Meat', "salad",)

#The List can be changed and new items inserted and other things like sorting
food2 = ["Pizza", 'Chicken', 'Meat', "salad"]
print (food2)
food2.sort()
print(food2)

#For Tuple once created we can't change it 
print(food)
#The following sentance will generate an error
#Un-Comment to verifie
#food.sort()
print(food)