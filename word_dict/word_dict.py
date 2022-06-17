word_list = "word_dict\word list.txt"

dictonary = {}

with open(word_list) as lines_of_text:
    for word in lines_of_text:
        word = word.strip("\n")
        if word not in dictonary:
            dictonary[word] = 1
        else:
            dictonary[word] += 1

print (dictonary)