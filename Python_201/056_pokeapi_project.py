#Using Request to use pokeapi data

import requests, json

req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
# print(req.json())

response = req.json()
# json.dumps(response, indent=4, separators=(". ", " = "))
text= json.dumps(response, indent=4, separators=(". ", " = "))
print(type(text))
print(text)

def printDataset (dataset, num, name):
    # print("=======================")
    # print("(",num+1,")")
    # print(dataset)
    # print("```````````````````````")
    num +=1
    if isinstance(dataset, dict):
        for key in dataset:
            item = dataset[key]
            if key != name:
                # print(num,"$", num*" ", key)
                print(num*" ", key)
            if isinstance(item, (list, dict, tuple, set) ):
                # print(num,'*',num*"\t",key,":")
                printDataset(item, num,key)
                print(" ")
            else:
                if key != name:
                    # print(num,'!',(num+1)*"\t",key,": ",item)
                    print((num+1)*" ",key,": ",item)
                else:
                    # print(num,'!',(num+1)*"\t","  ",item)
                    print((num+1)*" ",item)

    else:
        for item in dataset:
            if isinstance(item, (list, dict, tuple, set) ):
                printDataset(item, num,name)
                print(" ")
            else:
                # print(num,'&',num*"\t",item)
                print(num*" ",item)
    # print("<",num+1,">")

print(type(response))

for key  in response:
    # print(key)
    value = response[key]
    # print(value)
    # print("^",key," :")
    print(key," :")
    if isinstance(value, (list, dict, tuple, set) ):
        
        printDataset(value,1,key)
        # print("******************")
        print(" ")
    else:
        # print(key," : ", value)
        # print("? ","\t", value)
        print(" ", value)

        
# print(Fore.RED + 'some red text')