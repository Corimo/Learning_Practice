sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
list_dict = {}

for item in sample_list:
    if item not in list_dict:
        list_dict[item] = 1
    else:
        list_dict[item] += 1

print (f"\nOccurences of items in list: ")

for item in list_dict:
    print (f"The number of times {item} occured in list was {list_dict[item]}")

print("\n")