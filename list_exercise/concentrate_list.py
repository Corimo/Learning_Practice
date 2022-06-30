list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

output_list = []

for index, item in enumerate(list1):
    for pos, data in enumerate(list2):
        output_list.append(list1[index] + list2[pos])

print(output_list)