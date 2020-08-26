import datetime as dt
from datetime import date,timedelta

class GitRepoApisDetails:
    def get_repo_details_by_two_date(self, repo_name, year1, month1, days1, year2, month2, days2):

        start_dt = date(year1, month1, days1)
        end_dt = date(year2, month2, days2)
        flag = 1
        nextTime = ''
        for index in range((end_dt - start_dt).days + 1):
            print("==================")
            print(timedelta(index))
            new_date = start_dt + timedelta(index)
            print("**************************")
            print(start_dt)
            print(new_date)
            day_obj = new_date.strftime("%Y-%m-%d")

            if flag == 1:
                nextTime = dt.datetime.now() + dt.timedelta(seconds=10)
                dat = dt.datetime.strftime(nextTime, "%Y-%m-%d %H:%M:%S")

                flag = 0
            else:
                nextTime = nextTime + dt.timedelta(seconds=10)
                dat = dt.datetime.strftime(nextTime, "%Y-%m-%d %H:%M:%S")



obj = GitRepoApisDetails()
obj.get_repo_details_by_two_date("dockerfile",2020,1,1,2020,1,3)