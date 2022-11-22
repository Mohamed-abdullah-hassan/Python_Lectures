# The NOT operator
#From Video #035

#the not operator changes the condition of the comparison ie: from True to False or From True to False

answer = True

if answer:
    print ("The answer is true")

answer = not answer

if answer:
    print("The answer is still True")
else:
    print("The answer is changed to False")

#not can be combined with other operators to revers its result
myName = "Mohamed Abdullah"

if "Mohd " not in myName:
    print("the not in operator is working")