list1 = [20, 10, 35, 30, 25]
list2 = [20, 45, 60, 75, 90]

final_list = []

for item1 in list1:
    if item1 % 2 == 1:
        final_list.append(item1)

for item2 in list2:
    if item2 % 2 == 0:
        final_list.append(item2)

final_list.sort()
print (final_list)