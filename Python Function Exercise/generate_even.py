max_number = int(input("Even numbers up to: "))

def even_number(max):
    evens = []
    for number in range(4, max):
        if number % 2 == 0:
            evens.append(number)
    return evens

print (even_number(max_number))