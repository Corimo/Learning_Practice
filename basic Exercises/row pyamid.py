size = int(input("pyramid size: "))

for row in range(1, size + 1):
    no = 0
    while no < row:
        print (row, end=" ")
        no += 1
    print ("", end="\n")