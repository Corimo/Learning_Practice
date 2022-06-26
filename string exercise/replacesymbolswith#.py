from string import punctuation


import string

str1 = '/*Jon is @developer & musician!!'

for letter in string.punctuation:
    str1 = str1.replace(letter, "#")

print (str1)