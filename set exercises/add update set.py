set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

for item in set2:
    if item not in set1:
        set1.add(item)

print(set1)

set3 = set({10, 20, 30, 40, 50})
set4 = {30, 40, 50, 60, 70}

set3.intersection_update(set4)

print(set3)