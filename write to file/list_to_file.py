location = "write to file\list.txt"

toWrite = ["green", "red", "blue", "yellow", "purple"]

with open(location, "w") as writing:
    for listno in toWrite:
        writing.write(str(listno) + "\n")