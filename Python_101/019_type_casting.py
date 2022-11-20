#Data types conversion From video #19

myLst = ['Apple','Orange','Banana','Mango', 'Grapes', 'Apple', 'Frutes','Kiwi','Orange']
myName = "Mohammed"
number = "23098309"



print(myLst)
print(type(myLst))
print(myName)
print(type(myName))
print(number)
print(type(number))



#To convert from or to List
print("01-Casting to Set:")
newLst = set(myLst)
print(newLst)
print(type(newLst))
print("Size:")
print(newLst.__sizeof__())

print("02-Casting to Tuple:")
newLst = tuple(myLst)
print(newLst)
print(type(newLst))
print("Size:")
print(newLst.__sizeof__())

print("03-Casting to List:")
newLst = list(newLst)
print(newLst)
print(type(newLst))
print("Size:")
print(newLst.__sizeof__())

print("04-Casting to String:")
newLst = str(myLst)
print(newLst)
print(type(newLst))
print(newLst.__sizeof__())


#Strings can be converted to other data types
newLst = set(myName)
print(newLst)
print(type(newLst))
newLst = tuple(myName)
print(newLst)
print(type(newLst))

newLst = list(myName)
print(newLst)
print(type(newLst))

#casting strings to numbers
print(type(number))
num = int(number)
print(num)
print(type(num))
