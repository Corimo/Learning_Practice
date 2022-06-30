list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", None]

for item in list1:
    if item == None:
        list1.remove(item)
    elif len(item) <= 0 or item == None:
        list1.remove(item)

print(list1)