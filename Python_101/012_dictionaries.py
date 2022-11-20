#Dtata structures in Python Dictionaries from Video # 12

#To create a dictionary 
person = {
    "Key": "Value",
    "Name": "Mohamed",
    "Age" : 41,
    "Location": "borg la arab"
}

#print an element using it's key
print (person["Name"])

#print the whole Dictionary variable
print(person)

#To Add another element to dictionary
person['tel'] = "+123456789"
print(person)

#To Delete an element from dictionary variable
del person["Key"]
print(person)