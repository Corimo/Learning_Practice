import datetime

given_date = datetime.datetime(2020, 3, 22, 10, 0, 0)

week_delta = datetime.timedelta(days = 7)
hours_delta = datetime.timedelta(hours = 12)

print (given_date + week_delta + hours_delta)