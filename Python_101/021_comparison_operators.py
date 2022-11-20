# Comparison Operators and if Satements From video #21

userName = input("What is your Name?")
age = int(input("How Old are you ?"))

#if statement

if userName == "Mohamed":
    print("Hello, Mohamed welcome on board")
elif userName == "mohamed":
    print("Hello, Mohamed! Next time type Mohamed")
else:
    print("No user found")

if age == 20:
    print("You need to get a new ID")
elif age > 20:
    print("Now you can drive")
elif age < 20:
    print("Sorry, you can't drive")
else:
    print("I need to see your ID")
if age != 16:
    if age >= 16:
        print("Now must have an ID")
    elif age <= 15:
        print("be ready to get an ID")
else:
    print("Get an ID!!!!!!!!!!!")    
