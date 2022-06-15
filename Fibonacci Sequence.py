position = int(input("What position in the sequence do you want? "))

def fibonacci (number):
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci (number - 1) + fibonacci (number - 2)
        
# Kinda shit exponetial growth of processing

print (fibonacci (position))