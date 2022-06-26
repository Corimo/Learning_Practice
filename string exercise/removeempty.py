str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

result = []

for words in str_list:
    if words:
        result.append(words)

print (result)