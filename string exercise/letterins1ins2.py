s1 = "Yn"
s2 = "PYnative"

list_s1 = []

for letter in s1:
    list_s1.append(letter)

for alpha in s2:
    if alpha in s1:
        list_s1.remove(alpha)
    
if list_s1 == []:
    print (True)
else:
    print (False)