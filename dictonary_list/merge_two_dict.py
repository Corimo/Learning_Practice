dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 ={}

def merge_dict(first, second): #first is the dictionary we are adding to and second is the dictonary we are getting inofrmatiion from
    for item in second:
        if item not in first:
            first[item] = second.get(item)
        else:
            if first[item] <= second[item]:
                second[item] = first.get(item)
            else:
                continue

merge_dict (dict3, dict1)
merge_dict (dict3, dict2)

print(dict3)