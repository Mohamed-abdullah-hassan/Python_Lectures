#Project for a simple bakking account for withdraw and deposit
#From Video #72 from now on the file numbering will not be alligned with video numbers!

import os.path
import json
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Hello, and wellcome to PyBank")
# user_id = input("Please Enter User account number")
bankDBFile = '071_zBank.txt'

class user_Acount():
    id = 0
    name =''
    ac_type = ''
    ammount = 0
    def __init__(self, usrList):
        temp = usrList[0].split(':')[1]
        self.id = int(temp)
        self.name = usrList[1].split(':')[1]
        self.ac_type = usrList[2].split(':')[1]
        self.ammount = int(usrList[3].split(':')[1])

    def print(self):
        print(self.id)
        print(self.name)
        print(self.ac_type)
        print(self.ammount)
    
    def get_ammount(self):
        return self.ammount
    
    def withdraw(self, value):
        if(value > self.ammount):
            return False
        else:
            self.ammount -= value
            return True

    def deposit(self, value):
        self.ammount += value
        return True

    def updateLst(self, usrLst):
        usrLst[1] = f"name:{self.name}"
        usrLst[2] = f"type:{self.ac_type}"
        usrLst[3] = f"ammount:{self.ammount}"

def load_db():
    dataBase = list()
    with open(bankDBFile, 'r') as file:
        myContent = file.readlines()
        if(len(myContent)%4) ==0:
            count = 0
            print("Database is correct")
            cl_list = list()
            for item in myContent:
                cl_list.append(item.rstrip())
                count +=1
                if count >3:
                    dataBase.append(cl_list)
                    cl_list = list()
                    count =0
    return dataBase

def saveDB(bankList):
    with open(bankDBFile, 'w') as file:
        for item1 in bankList:
            for item2 in item1:
                file.writelines(item2 +'\n')
        

bankClients = load_db()
iterator = 0
accounts = dict()

while iterator < len(bankClients):
    id = bankClients[iterator][0]
    tmp = id.split(':')
    accounts[int(tmp[1])] = iterator
    iterator +=1
try:
    userId = input("Please enter your user id: ")
except:
    print("\nExiting.....\n\nThanks for Using PyBank\n")
try:
    userId = int(userId)
except:
    print('Invalid id')
    userId = None

if not userId == None:
    indx = accounts[userId]
    usr = user_Acount(bankClients[indx])
    print(f"Welcome {usr.name}")
    while True:
        try:
            action = input("\nPlease select one of the following:\n\
1 for ptint your balance\n\
2 for Deposit\n\
3 for Withdraw\n\
4 to change user name\n\
0 to Exit\n :")
        except:
            print("\nExiting....\n\nThanks for Using PyBank\n")
            break
        try:
            action = int(action)
        except:
            print("Please enter 1 , 2 , 3 , 4 or 0 to exit")
            continue
        if action ==1:
            print(f"The Balance for {usr.name} is: \n  [ ",usr.get_ammount()," ]")
            continue

        elif action ==2:
            value = input("How Much you will Deposit?\n :")
            try:
                value = int(value)
            except:
                print("Enater a valid ammount")
                continue
            if(not usr.deposit(value)):
                print("Cant Deposit now Try again later")
                continue
            print(f"Deposit Success, Your new ballance is:\n [ {usr.get_ammount()} ]")
            continue
        elif action ==3:
            value = input("How much you will Withdraw?\n :")
            try:
                value = int(value)
            except:
                print("Enater a valid ammount")
                continue
            if(usr.withdraw(value)):
                print(f"Withdrawel of [{value}] complete, your current balance is:\n [{usr.get_ammount()}]")
            else:
                print(f"Sorry not Enough balance \n Try less than {usr.get_ammount()}")
            continue
        elif action ==4:
            value = input("What is the name you like?\n :")
            usr.name = value
            print(f"Name change complete to {usr.name}\n")
            continue
        elif action ==0:
            usr.updateLst(bankClients[indx])
            saveDB(bankClients)
            print("\n\n\nThanks for Using PyBank\n")
            break



    
    

