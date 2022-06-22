str_x = "Emma is good developer. Emma is a writer Emma"

word_list = list(str_x.split(" "))

count = 0

for word in word_list:
    if word == "Emma":
        count += 1

print (f"Emma appeared {count} times")
