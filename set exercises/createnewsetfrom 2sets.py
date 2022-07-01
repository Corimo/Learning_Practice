set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set({})

for item in set1:
    if item in set2:
        set3.add(item)
    else:
        continue

# Could also use
# set3 = set1.intersection(set2) 

print(set3)


set4 = set({})

def unite_set(first_set, second_set):
    for entry in second_set:
        if entry in first_set:
            continue
        else:
            set(first_set)
            first_set.add(entry)

unite_set(set4, set1)
unite_set(set4, set2)

# Could also use
# set4 = set1.union(set2)

# print (set1)
print (set4)