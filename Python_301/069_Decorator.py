#Decorators in python l
#From Video #69
#Decorator is used to encapsulate a function in another function to do extra process

def myHelloDecorator(func):
    def myWrapper():
        print("Hello, ")
        func()
        print("I'm Glad to meet you!")
    return myWrapper

def message():
    print("I'm Mohammed")

@myHelloDecorator   #put @ follwed by the funtion decrator name
def message2():
    print('I am a programmer')

myfunc = myHelloDecorator(message)

myfunc()

print('\nAnother Decorator method ')
message2()