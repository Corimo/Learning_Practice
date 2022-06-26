str1 = "PyNaTive"

lower = [""]
upper = [""]

for letter in str1:
    if letter.islower() == True:
        lower.append(letter)
    else:
        upper.append(letter)
sort = "".join(lower + upper)
print(sort)