position = int(input("Up to which Digit: "))

num1 = 0
num2 = 1

for digit in range(position):
    num3 = num2 + num1
    print (num3)
    num1 = num2
    num2 = num3