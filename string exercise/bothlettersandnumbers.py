str1 = "Emma25 is Data scientist50 and AI Expert"

list_str1 = str1.split(" ")
results = []

for word in list_str1:
    alpha = False
    digit = False
    for letter in word:
        if letter.isalpha() == True:
            alpha = True
        elif letter.isdigit() == True:
            digit = True
    if alpha == True and digit == True:
        results.append(word)
    else:
        continue

for both in results:
    print (both)