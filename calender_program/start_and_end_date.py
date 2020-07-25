import datetime as dt
from datetime import date,timedelta

class GitRepoApisDetails:
    def get_repo_details_by_two_date(self, repo_name, year1, month1, days1, year2, month2, days2):

        start_dt = date(year1, month1, days1)
        print(start_dt)
        end_dt = date(year2, month2, days2)
        print(end_dt)
        flag = 1
        nextTime = ''

        for dti in self.daterange(start_dt, end_dt):

            day_obj = dti.strftime("%Y-%m-%d")
            print(day_obj)
            if flag == 1:
                nextTime = dt.datetime.now() + dt.timedelta(seconds=10)
                dat = dt.datetime.strftime(nextTime, "%Y-%m-%d %H:%M:%S")
                flag = 0
            else:
                nextTime = nextTime + dt.timedelta(seconds=10)
                dat = dt.datetime.strftime(nextTime, "%Y-%m-%d %H:%M:%S")


    def daterange(self, date1, date2):

        new_date = (date2 - date1).days + 1
        print(new_date)
        for n in range(int((date2 - date1).days) + 1):
            yield date1 + timedelta(n)


obj = GitRepoApisDetails()
obj.get_repo_details_by_two_date("dockerfile",2020,1,1,2020,1,1)