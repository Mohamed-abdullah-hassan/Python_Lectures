#List Data Structures From video #11

number = 30
name = "mohamed"
myList = ["my name", name, number, ["This is", "a nested", "lists"], 984705948]

print(myList)

myList.append("new item")

print(myList)
print(myList)
#using for to extract list items
i =0
for myItem in myList :
    print(i, "This item is:", myItem)
    i+=1

myList.remove(number)

print(myList)
