size = int(input("Please input size: "))

for row in range(1, size + 1):
    for num in range(1, row + 1):
        print(num, end=' ')
    print("")