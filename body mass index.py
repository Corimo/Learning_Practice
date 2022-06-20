height = int(input("Pleae enter your height in cm: "))
mass = int(input("Please enter your Weight (Mass) in kg: "))

height_m = height / 100
BMI = mass / (height_m ** 2)

print (round(BMI, 1))

if BMI <= 18.5:
    print ("Underweight")
elif BMI <= 24.9:
    print ("Normal")
elif BMI <= 29.9:
    print ("Overweight")
else:
    print ("Obease")