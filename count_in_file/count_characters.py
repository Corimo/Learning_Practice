read_file = "count_in_file\quotes.txt"

string = ""

with open(read_file) as text:
    for line in text:
        remove_spaces = line.replace(" ", "")
        remove_linebreaks = remove_spaces.strip("\n")
        string += remove_linebreaks


print (f"There are {len(string)} in this file")