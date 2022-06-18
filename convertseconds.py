seconds =  int(input("Please enter number of seconds:"))

minutes = seconds // 60
hours = round(seconds / 3600, 1)

print (f"{seconds} is equal to")
print(f"{minutes} minutes")
print (f"and {hours} hours")