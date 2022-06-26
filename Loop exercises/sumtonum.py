numbersto = int(input("Please input number to add below: "))

number1 = 0

for num in range(numbersto + 1):
     sum = num + number1
     number1 = sum
     
print (number1)