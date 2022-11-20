#Input data from the user from Video # 18
# Using input() function to get an input from the user in cli
# The input() function returns strings even if the user write doen numbers

data = input("What is your Name? ")

print("Hello,",data)
question = "How old are you, " + data +"?"
age = input(question)

print(type(age))

new_age = age * 2

print (new_age)

#To convert user input a type casting method is used

if age.isnumeric():
    print("New age is:", int(age))
else:
    print("Not valid number")