#Function nesting
#From video #040

#Python Allow for function decleration inside another function decleration

def myFunc1(name):
    print('Hell,',name,"How are you?")

    def myFunc2():
        print("Hello, Again", name, "From the Nested function ")
    
    myFunc2()

myFunc1("Mohamed")
