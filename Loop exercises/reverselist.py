list1 = [10, 20, 30, 40, 50]

list2 = []

for num in range(len(list1)):
    revpos = len(list1) - 1 - num
    list2.append(list1[revpos])

print (list2)