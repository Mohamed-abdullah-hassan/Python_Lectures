#Break and continue in loop from Video #26

items = {'Table', 'pass', 'chair', 'coffie', 'books', 'pass', 'stop', 'pass','window', 'door', 'fridge', 'pass', 'sink'}

print("Printing the List Directly")
for item in items:
    print(item)

print("\nPrinting the List without pass or stop keywords")
for item in items:
    if item == 'pass' or item == 'stop':
        continue
    print("Item is: ", item)

print("\nPrinting the List without pass and stopping at stop keywords")
for item in items:
    if item == 'pass':
        continue
    elif item == 'stop':
        break
    print("Item is: ", item)

print("\nPrinting Odd numbers from 0 to 50 using while loop")
num = 0
while num <50:
    num = num + 1
    if num % 2 ==0:
        continue
    print(num)

print("Looping from 0 to 1000000000 and stoping at 23")
num = 0
while num < 1_000_000_000:
    if num ==23:
        break
    print(num)
    num = num +1
