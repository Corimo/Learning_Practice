string = input("Enter string:")
liststring = list(string.split(" "))

for item in liststring:
    print(f"Name{liststring.index(item) + 1}: {item}")