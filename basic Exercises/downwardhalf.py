size = int(input("Size: "))

for row in range(size, 1, -1):
    for width in range(1, row):
        print ("*", end=" ")
    print ("")