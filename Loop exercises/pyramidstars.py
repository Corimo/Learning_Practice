size = int(input("Pyramid Size: "))

for row in range(size + 1):
    for star in range(row):
        print("*", end=" ")
    else:
        print("")
for row in range(size - 1, 0, -1):
    for star in range(row):
        print("*", end=" ")
    else:
        print("")