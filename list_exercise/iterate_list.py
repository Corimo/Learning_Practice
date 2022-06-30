list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

reverse_list2 = []

for num in list2[::-1]:
    reverse_list2.append(num)

for index, item in enumerate(list1):
        print (list1[index], end=" ")
        print (reverse_list2[index])