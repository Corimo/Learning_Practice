triBase = 12
triHeight = 10

areaOfTriangle = round(0.5 * triBase * triHeight, 2)

if triBase < 0 or triHeight < 0:
    print("Please Enter valad values")
else:
    print(areaOfTriangle)