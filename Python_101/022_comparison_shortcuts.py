#Comparison shortcut from video #22
#in python if statement evaluate condition to True or False 
#so if passing only a variable to if statment without comparison 
# python will check if the variable is empty or not 
# so if a vriable is bool and equals False then the if statement will evaluate to false
# Also if the variable is None or if its an empty string, list or any dataset then the condition will equale false


name = input("Your name? ") #If you press enter without entring any charecter the string will be empty

if name:
    print("nice name!")
else:
    print("Please enter a name")
print(type(name))
