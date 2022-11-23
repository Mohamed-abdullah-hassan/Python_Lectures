#Function Arguments in python
#From Video #44

#Arguments is defined by using single * in function decleration
#Arguments mean that it can take many items those items are stroed in tuples 

def myFunc1(*myArgs):
    print(type(myArgs))
    print(myArgs)

myFunc1(1,2,4,5,2,67,23425,349709, 0,0,0,0)
myFunc1('FIFA', '2022', '@#$%#@$')
myFunc1()

#Arguments can be also combined with other variables

def myFunc2(name, age, *myArgs):
    print("Name:",name)
    print("Age:",age)
    print(myArgs)

myFunc2("Somo",3478,"Planets",'player',123249, {"smart","Fast","Inteligent","Strong"})
