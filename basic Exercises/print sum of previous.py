length = int (input("How far would you like to go: "))

prev_num = 0

for num in range(length):
    current_num = num
    sum = prev_num + current_num
    print (f"The current Number {current_num}, previous number is {prev_num} Sum: {sum}")
    prev_num = num