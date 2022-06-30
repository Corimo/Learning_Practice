list1 = [5, 20, 15, 20, 25, 50, 20]

item_to_remove = 20

for item in list1:
    if item == item_to_remove:
        list1.remove(item)

print(list1)