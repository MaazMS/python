from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler_obj = BlockingScheduler()

def run_job(text):
    print(text)

# The job will be executed on july 22th, 2020
scheduler_obj.add_job(run_job, run_date=date(2020, 7, 22), args=['This is job argument'] )
scheduler_obj.start()