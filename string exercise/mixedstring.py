s1 = "Abc"
s2 = "Xyz"

rev_s2 = s2[::-1]
result = []

while len(s1 + rev_s2) > 0:
    if len(s1) >= len(rev_s2):
        result.append(s1[0])
        s1 = s1[1:]
    else:
        result.append(rev_s2[0])
        rev_s2 = rev_s2[1:]

result = "".join(result)
print(result)