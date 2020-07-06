import datetime

year = 2013
month = 0
days_in_month = [32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]
for days_in_month in days_in_month:
    month += 1
    print("=====================================")
    for days in range(1, days_in_month):
        date = datetime.date(year, month, days)
        print(date)
