#Reading Multiple line from files
#From Video toutorial #038

#using .readlines() returns the content of the file in an array so each element represent a line in file

fileName = "038_multi_file.txt"
with open(fileName, 'r') as myFile:
    myContent = myFile.readlines()

print(type(myContent))

for item in myContent:
    print(item)

print(myContent)

#to remove the last \n use .rstrip()

for item in myContent:
    print(item.rstrip())

#now we can use other features for txt file processing

print("\nShowing only emails")
for item in myContent:
    if '@' in item:
        print(item.rstrip())

