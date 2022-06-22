base = int(input("Enter Base: "))
exponent = int(input("Enter Power: "))

def exponential(number, power):
    if power == 0:
        return 1
    else:
        return number * exponential(number, power - 1)

print (exponential(base, exponent))