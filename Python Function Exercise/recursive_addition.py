number = int(input("What do you need all digits up to: "))

def add_below (a):
    if a == 0:
        return 0
    else:
        return a + add_below(a - 1)

add = add_below(number)
print (add)

new_function = add_below

print(new_function(10))