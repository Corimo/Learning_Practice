import datetime

now = datetime.datetime.now()

print ("The current date and time are:")
print(now.strftime("%Y-%m-%d, %I:%M:%S"))