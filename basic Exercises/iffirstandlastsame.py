numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def first_last(a):
    if a[0] == a[len(a) - 1]:
        return (True)
    else:
        return (False)

print (first_last(numbers_x))
print (first_last(numbers_y))