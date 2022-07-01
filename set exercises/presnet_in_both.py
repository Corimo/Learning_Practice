set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set({})

for item in set1:
    if item not in set2:
        set3.add(item)

for item in set2:
    if item not in set1:
        set3.add(item)

#Could also use symetric_difference()

print(set3)