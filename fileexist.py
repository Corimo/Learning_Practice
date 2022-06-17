from genericpath import exists


search = "file.txt"

if exists(search) == True:
    print (f"The file {search} exsits")

else:
    print (f"The file {search} does not exist")