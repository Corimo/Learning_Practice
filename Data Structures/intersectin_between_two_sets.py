first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

remainder = {}
result = first_set.intersection(second_set)

for item in result:
    if item in first_set:
        first_set.remove(item)

print (result)
print (first_set)