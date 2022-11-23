#Writing to files
#From Video Toutorial #37

print("*Writing to a file:")
with open("037_wrting_example.txt", 'w') as myFile:
    myFile.write("Hello, From python writing files")

print("\n*Now reading then printing the content of the file:")

with open("037_wrting_example.txt", 'r') as myFile:
    print(myFile.read())

print("\n*If we try to rewrite to the file it will over-write the old data")

with open("037_wrting_example.txt", 'w') as myFile:
    myFile.write("\nThe secound line of code")

print("\n Now reading then printing the content of the file:")

with open("037_wrting_example.txt", 'r') as myFile:
    print(myFile.read())

print("\n\t\t*Using a for append insted of w for write")

with open("037_wrting_example.txt", 'a') as myFile:
    myFile.write("\nThe Third line of code")

print("\n Now reading then printing the content of the file for the 3rd time:")

with open("037_wrting_example.txt", 'r') as myFile:
    print(myFile.read())
