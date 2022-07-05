import datetime
from dateutil.relativedelta import relativedelta

given_date = datetime.datetime(2020, 2, 25).date()

months_to_add = 4
time_delta = given_date + relativedelta(months =+ months_to_add)

print(time_delta)