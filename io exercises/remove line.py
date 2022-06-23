with open ("io exercises\ext.txt", "r") as text:
    lines = text.readlines()

with open ("io exercises\output_text.txt", "w") as newtext:
    count = 0
    for line in lines:
        if line.strip("\n") == "line 5":
            count += 1
        else:
            newtext.write(line)
            count += 1