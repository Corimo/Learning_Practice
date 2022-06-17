words = "longest word\words.txt"
longest = [""]

with open(words) as list_words:
    lines = list_words.readlines()

    for word in lines: 
        length = len(word.strip("\n"))
        if len(longest[0]) < length:
            longest.remove(longest[0])
            longest.append(word.strip("\n"))

print (longest)
