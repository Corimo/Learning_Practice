number = int(input("Number you want the number of digits in: "))

count = 0

while number > 0:
    number = number // 10
    count += 1

print(f"The number of digits are: {count}")