original = "write file to file\originaltext.txt"
destination = "write file to file\destintext.txt"

with open(original) as source, open(destination, "w") as goingto:
    for line in source:
        goingto.write(line)

