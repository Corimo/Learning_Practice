sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

key_to_rename = "city"
new_name = "location"

sample_dict[new_name] = sample_dict.pop(key_to_rename)

print (sample_dict)