import os

size = os.stat("io exercises\empty_file.txt").st_size

if size == 0:
    print ("The file is empty")
else:
    print ("File is not empty")