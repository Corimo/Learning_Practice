number = int(input("Please input size: "))

for digit in range(number, 0, -1):
    for no in range(digit, 0, -1):
        print (no, end=" ")
    print ("")