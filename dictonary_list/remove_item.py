from os import remove


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for item in keys:
    if item in sample_dict:
        del sample_dict[item]

print (sample_dict)