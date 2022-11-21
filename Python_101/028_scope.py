#Scope In functions
#From Video #28

#Variables declared in a function can't be accessed from outside the function

#Functions can use variable outside it
name = "Mohamed"

def myFunc1():
    return "Hello, "+name

print(myFunc1())

#if a function has defiend a variable that its already defined outside 
#the function will use its local defiend variable 

def myFunc2():
    name = 'world'
    return "Hello, "+name

print("Using both global variable and local variable")
print("Original variable:", name)
print("Calling myFunc2() \n", myFunc2())
print("Same variable after variable:", name)