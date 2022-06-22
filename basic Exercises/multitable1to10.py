num = int(input("Times tables up to: "))

for digit in range(1, num + 1):
    print (digit, end="  ")
    for digit2 in range (1, 11):
        product = digit * digit2
        print(product, end=" ")
    print ("", end="\n")