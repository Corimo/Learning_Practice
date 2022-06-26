str1 = "Apple"

result = {}

for letter in str1.upper():
    if letter not in result:
        result[letter] = 1
    else:
        result[letter] += 1

print (result)