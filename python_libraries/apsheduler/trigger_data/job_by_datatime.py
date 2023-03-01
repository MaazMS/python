from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler_obj = BlockingScheduler()

def run_job(text):
    print(text)

# The job will be executed on july 22th, 2020 at   12:05:00

scheduler_obj.add_job(run_job, run_date=datetime(2020, 7, 22, 12, 5 , 00), args=['This is job argument'] )

scheduler_obj.start()