from string import punctuation


str1 = "/*Jon is @developer & musician"

result = str1.translate(str.maketrans("", "", punctuation))

print (result)