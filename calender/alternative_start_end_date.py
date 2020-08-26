from datetime import date,timedelta


def display_days_between_two_date(year1, month1, days1, year2, month2, days2):
    start_dt = date(year1, month1, days1)
    end_dt = date(year2, month2, days2)


    for index in range((end_dt - start_dt).days + 1):
        new_date = start_dt + timedelta(index)
        day_obj = new_date.strftime("%Y-%m-%d")
        print(day_obj)

display_days_between_two_date(2020, 1, 1, 2020, 1, 15)