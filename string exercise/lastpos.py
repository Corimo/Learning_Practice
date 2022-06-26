str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"

#split_str1 = str1.lower().split(" ")
#position = 0

index = str1.rfind(str2)
#for index, word in enumerate(str1):
#    if word == str2.lower():
#        position = index

print(index)