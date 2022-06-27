roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print(f"\nList: {roll_number}")
print(f"Dictonary: {sample_dict}\n")

for item in roll_number[:]:
    if item not in sample_dict.values():
        roll_number.remove(item)

print(f"After removing Unwanted elements: {roll_number}\n")