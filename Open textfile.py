filelocation = "test_file.txt"

test_file = []

with open(filelocation) as textfile:
    for line in textfile:
        test_file.append(line)

print (test_file)