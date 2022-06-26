from re import L


length = int(input("Insert digit you want ot go to: "))

result = 1

if length < 0:
    print("Invalid Input")
elif length == 0:
    print("0")
else:
    for num in range (1, length + 1):
        result = result * num
    print (result)