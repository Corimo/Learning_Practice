sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

new_dict = {}

for iter in keys:
    if iter not in new_dict:
        new_dict[iter] = sample_dict.get(iter)
    else:
        continue

print(new_dict)