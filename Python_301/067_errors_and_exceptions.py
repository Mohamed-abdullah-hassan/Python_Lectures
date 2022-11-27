#Erros and working around
#Video #67

try:
    a = 323
    b = 'Error'
    c = b/a
    print("Division value is:", c)
    c = a/b
    print("Division value is:", c)
except Exception:
    print("Error not Allowed")


num = input("Enter a num or try entring a text: ")

try:
    num = int(num)
except Exception:
    num = "Not a valid number"

print("Your number is:",num)
