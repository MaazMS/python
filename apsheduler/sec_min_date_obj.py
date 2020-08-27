import schedule
import time

class jobs_based_on_time:

    def job_by_sec(self):
        print("This job work on the every 5 second")


    def job_by_min(self):
        print("This job work on every 1 min ")


    def job_by_houe(self):
        print("This job work on every day 11:00")




obj = jobs_based_on_time()

schedule.every(1).seconds.do(obj.job_by_sec)
schedule.every(10).seconds.do(obj.job_by_min)
schedule.every().hours.do(obj.job_by_hour)

while True:
        schedule.run_pending()
        time.sleep(1)

