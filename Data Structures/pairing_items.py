first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

third_list = []

for index, item in enumerate(first_list):
    pair = (first_list[index], second_list[index])
    third_list.append(pair)

print(set(third_list))