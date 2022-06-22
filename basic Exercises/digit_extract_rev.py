digit = int(input("Enter Digit: "))

while digit > 0:
    remainder = digit % 10
    digit = digit // 10
    print (remainder, end=" ")
