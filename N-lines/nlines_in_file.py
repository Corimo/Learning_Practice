text_file = "test_file.txt"

linesToRead = 6

lines_to_print = []

with open(text_file) as text_lines:
    read_lines = text_lines.readlines()
    number_lines = len(read_lines)

    if linesToRead > number_lines:
        print ("Invalad line text file does not have enough lines")

    else:
        for line in range(linesToRead):
            print (read_lines[line])