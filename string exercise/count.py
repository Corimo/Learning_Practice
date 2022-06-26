str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for symbol in str1:
    if symbol.isalpha() == True:
        chars += 1
    elif symbol.isdigit() == True:
        digits += 1
    else:
        symbols += 1

print (f"Total count of the characters, digits, and symbols\n\nCharacters = {chars}\nDigits = {digits}\nSymbols = {symbols}")