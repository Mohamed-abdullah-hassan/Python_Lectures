#Writing Pad 
#Testing python code to create simple writing Pad

#importing os.path just to check if the file exists.
import os.path

print("Hello, and wellcome to WPad")
myFile = input("Please Enter file name (press enter to exit)")

if not myFile == '':
    if os.path.isfile(myFile):
        uContent = input("File exists do you like to continou editing?")
        if 'y' in uContent.lower():
            att = str('a')
            with open(myFile, 'r') as file:
                myContent = file.readlines()
                for item in myContent:
                    print(": "+item.rstrip())
        else:
            att = str('w')
            print("Enter your text and to exit press enter on an empty line ;)")
        with open(myFile, att) as wPad:
            while True:
                uContent = input(": ")
                if uContent == '':
                    break
                wPad.writelines(uContent+'\n')
    
    print("Printing your File")
    with open(myFile, 'r') as wPad:
        print(wPad.read())
        


