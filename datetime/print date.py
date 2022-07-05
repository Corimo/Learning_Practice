import datetime
from time import strftime

given_date = datetime.datetime(2020, 2, 25)

string_time = given_date.strftime('%A %d %B %Y')

print (string_time)