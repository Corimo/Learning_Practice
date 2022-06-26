str1 = 'I am 25 years and 10 months old'

digits = []

for symbol in str1:
    if symbol.isdigit() == True:
        digits.append(symbol)
    else:
        continue

digi_list = "".join(digits)
print(digi_list)