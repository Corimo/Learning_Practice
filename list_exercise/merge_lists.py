list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

merged_list = []

for index, item in enumerate(list1):
    merged_list.append(list1[index] + list2[index])

print(merged_list)