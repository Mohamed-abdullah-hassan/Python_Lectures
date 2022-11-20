#String Formatting From Video #20

myName = "Mohamed"
myTime1 = "Day"
myTime2 = "Night"

welcome_message1 = "Hello, " + myName + " Its a nice " + myTime1
welcome_message2 = "Hello, {} its a nice {}".format(myName,myTime2)
welcome_message3 = f"Hello, {myName} its a nice {myTime1}"
welcome_message4 = "Hello, %s its a nice %s" % (myName, myTime2)

print(welcome_message1)
print(welcome_message2)
print(welcome_message3)
print(welcome_message4)
