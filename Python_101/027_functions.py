#Introduction to Python Functions 
#From Video #27

# Defining a function by starting def function_name():
# and place the code underneth, and noting indentation.
# then call it using function_name()

def myFunc():
    print("Hello, World")

print("Simple function usage:")
myFunc()
myFunc()
myFunc()

#Functions can take argument

def myFunc2(name):
    print(f"Hello, {name}")

print("\nPassing argument to a Function:")
myFunc2('Mohamed')
myFunc2('World')
myFunc2('FIFA')
myFunc2("Any other Name here")

#for multi arguments 

def myFunc3(name, act, obj):
    print(f"Hello, {name} Lets {act} {obj}")

print("\nPassing multiple arguments to a Function:")
myFunc3('Mohamed', 'Eat', "Pizza")
myFunc3('World', 'Make', "Peace")
myFunc3('FIFA', 'play', "Football")
myFunc3("Any other Name here", "sya", 'anything')

#makeing default argument in a function

def myFunc4(name, act="Say", obj="A word"):
    if name.lower() == "mohamed":
        print("Hello Mohamed, Lets Eat Pizaa and watch football")
    else:
        print(f"Hello, {name} Lets {act} {obj}")

print("\nPassing multiple arguments to a Function and using default :")
myFunc4('Mohamed', 'Eat', "Pizza")
myFunc4('World', 'Make')
myFunc4('FIFA')

#functions by default returns None value
#Adding return follwed by the value to return 

def myAdd(num1, num2):
    return num1 + num2

print(myAdd(378,489))

#Example making Exponent caluculator

def myExp(num1, num2):
    total = num1 ** num2
    return total

bigNumber = myExp(2,32)
print(bigNumber)
