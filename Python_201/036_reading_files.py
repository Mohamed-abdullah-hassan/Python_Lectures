#Reading a files
#From video #36

with open("036_Examples.txt", 'r') as myFile:
    print(myFile.read())
    

#after exiting the code context manager block the file is automaticaly closed
#print(myFile.read())

# Access the content after exiting context manager block simply place it in a variable

with open("036_Examples.txt", 'r') as myFile:
    content =myFile.read()
    print("The file content is: \n", content)

print("Again printing the conttent of the file: \n", content)

