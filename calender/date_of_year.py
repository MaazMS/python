import calendar
import datetime



year = 2020
for month in range(1 , 13 ):

    num_days = calendar.monthrange(year, month, )[1]
    print(num_days)
    for day in range(1, num_days+1):
        day_obj = datetime.date(year, month, day)
        print(day_obj)