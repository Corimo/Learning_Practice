number = int(input("Enter Number to be reversed: "))

result = 0

while number > 0:
    lastdigit = number % 10
    result = (result * 10) + lastdigit
    number = number // 10
print (result)