#Catching specific Exception 
#Video #68

num1 = input("Enter number: ")
num2 = input("Enter number enter zero to tesst another Eception: ")
num = 'Infinity'
try:
    num = int(num1)
    num = num / int(num2)
except ValueError as e:
    print("Un valid number entered")
    print(type(e))
    print("Python returned error: ",e)

except ZeroDivisionError as e:
    print("Devide by Zero Error:")
    print("Python returned error: ",e)

except Exception as e:
    print("An Exception was caught")
    print(type(e))
    print("Python returned error: ",e)
    num = "Error"

print(num)


