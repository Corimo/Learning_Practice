set1 = {10, 20, 30}
set2 = {20, 40, 50}

for item in set2:
    if item in set1:
        set1.remove(item)

# Could also use
# set1.difference_update(set2)

print(set1)

set3 = {10, 20, 30, 40, 50}
remove_set = {30, 20, 10}

set3.difference_update(remove_set)

print (set3)