my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result_list = []

for index, info in enumerate(my_list):
    if index % 2 == 1:
        result_list.append(info)
    else:
        continue

print (result_list)