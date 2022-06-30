list1 = [5, 10, 15, 20, 25, 50, 20]
value_to_change = 20
replacement_value = 200

for index, item in enumerate(list1):
    if item == value_to_change:
        list1[index] = replacement_value
        break

print(list1)