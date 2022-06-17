openFile = "test_file.txt"

number_read_from = 2

line_to_print = []

with open(openFile) as text_lines:
    total_lines = text_lines.readlines()
    number_lines = len(total_lines)

    if number_lines > number_lines:
        print ("Invalad line text file does not have enough lines")

    else:
        for line in range(-number_read_from, 0):
            print (total_lines[line])