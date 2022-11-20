# Multiple comparison operators from Video # 23

#to make multi comparison is done by using and, or operators

userName = input("Hello, What is your name? ")
userID   = input("Please enter your ID: ")

if userID.isnumeric():
    userID = int(userID)
    if userName == "Mohamed" and userID == 123456789:
        print("Welcome, Mohamed Abdullah")
    elif userID == 00000 or userName == "New":
        print("New User?")
    else:
        print("Wrong Name or ID")
else:
    print("Not a valid number")