from apscheduler.schedulers.blocking import BlockingScheduler

scheduler_obj = BlockingScheduler()

def run_job(text):
    print(text)

# The job will be executed on july 22th, 2020 at   12:11:00 do not use datatime or date function in text
scheduler_obj.add_job(run_job, run_date='2020-7-22 12:20:00', args=['This is job argument'] )

scheduler_obj.start()