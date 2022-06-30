sample_dict = {'a': 100, 'b': 200, 'c': 300}

search_value = 400
for item in sample_dict:
    if sample_dict[item] == search_value:
        print (f"{search_value} present in dictonary")
    else:
        continue
else:
    print ("Value is not prresent in dictonary")