maxnumber = int(input("Maximum Number: "))
mimnumber = int(input("Minimum Number: "))

for num in range(mimnumber, maxnumber + 1):
    for digit in range(2, num):
        if num % digit == 0:
            break
    else:
        print(num)