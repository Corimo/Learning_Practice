number = int(input("INput single number diigit: "))

start = 2
sum_seq = 0

for iter in range (0, number):
    print (start, end="+")
    sum_seq += start
    start = start * 10 + 2

print("\n", sum_seq)