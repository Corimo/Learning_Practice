tuple1 = (45, 45, 45, 45)

state = True
for items in tuple1:
    if items != tuple1[0]:
        state = False

print (state)