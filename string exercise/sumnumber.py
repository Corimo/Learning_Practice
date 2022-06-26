str1 = "PYnative29@#8496"

numbers = []

for sym in str1:
    if sym.isdigit() == True:
        numbers.append(int(sym))
    else:
        continue

add = sum(numbers)
length = len(numbers)
average = add / length

print(f"Sum of digits is: {add} and Average is {average}")