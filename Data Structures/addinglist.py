l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

for index, element in enumerate(l1):
    if index % 2 == 1:
        l3.append(element)
    else:
        continue

for position, item in enumerate(l2):
    if position % 2 == 0:
        l3.append(item)
    else:
        continue
    
print(l3)