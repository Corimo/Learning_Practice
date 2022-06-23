with open ("io exercises\ext.txt", "r") as text:
    list_num = [4]
    lines = text.readlines()
    for no, ind in enumerate(lines):
        if no in list_num:
            print (ind)