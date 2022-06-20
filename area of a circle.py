from math import pi


diameter = int(input("How wide will you like the circle (cm): "))

area = round((pi * ((0.5 * diameter)**2)), 2)

print(f"The are of a circle with the Diameter {diameter} cm is {area} cm^2")