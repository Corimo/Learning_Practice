list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

for item in sub_list:
    list1[2][1][2].append(item)

print(list1)