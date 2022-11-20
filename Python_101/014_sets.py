# Python Data Structure Sets From Video #14
# Set is like List data structure with some diffrences, sets dosen't maintain the order of elemnts
#as it was initialized with
#also sets cantains only uniqe elements, which means that any repeted elements will be removed from it
# to create a set { } are used witout "key": "Value" style

name = {"Hello", "World", "Python","101", "Item 1", "Item 2", "Item 3", "Item 1"}

print(name)

#Sets can be add elemnts
name.add("Programming")

print(name)

#set can remove elemnts

name.remove("101")

print(name)
