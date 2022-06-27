first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

def subset(set1, set2):
    length = len(set1)
    count = 0
    for item in set1:
        if item in set2:
            count += 1
        else:
            continue
    if count == length:
        return True
    else:
        return False

def superset(set1, set2):
    length = len(set1)
    count = 0
    for item in set2:
        if item in set1:
            count += 1
        else:
            continue
    if count == length:
        return True
    else:
        return False

"Subsets"
print("\nIs the sets sup sets of each other: ")
print(f"    First set a Subset of Second set: {subset(first_set, second_set)}")
print(f"    Second set a Subset of First set: {subset(second_set, first_set)}\n")

"Supersets"
print("\nIs the sets sup sets of each other: ")
print(f"    First set a Superset of Second set: {superset(second_set, first_set)}")
print(f"    Second set a Superset of First set: {superset(first_set, second_set)}\n")

"Resulting Sets"
if subset(first_set, second_set):
    first_set.clear()

if subset(second_set, first_set):
    second_set.clear()

print (f"First Set: {first_set}")
print (f"Second Set: {second_set}\n")