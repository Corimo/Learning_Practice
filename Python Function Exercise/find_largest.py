num = [4, 6, 8, 24, 12, 2]

def find_largest(numbers):
    biggest = 0
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest

print (find_largest(num))