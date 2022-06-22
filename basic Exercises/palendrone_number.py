number = int(input("Enter number: "))
rev_num = 0
original_num = number

while number > 0:
    remining = number % 10
    rev_num = (rev_num *10) + remining
    number = number // 10

if rev_num == original_num:
    print ("The number is a palendrone")
else:
    print ("The number isn't a Palendrone")