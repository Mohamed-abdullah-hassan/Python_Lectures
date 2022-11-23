#Functions Keywords
#From Video #45

#Keywords are difeined by **  and its given to the function using a dictionary

def myFunc(**myKwargs):
    print(type(myKwargs))
    print(myKwargs)

myFunc(name = "Moso", Age= "33", Place = "USA")

myFunc()

def myfunc2(color, length, *myargs, **mylist):
    print("Color is:",color)
    print("Length is:",length)
    print("Arguments are:", myargs)
    print("Key-Words are:", mylist)

myfunc2('red','XL', 338,'decorated','extra packing', count = 5, price = 33, Home_deleviry = True)


