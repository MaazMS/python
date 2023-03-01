from apscheduler.schedulers.blocking import BlockingScheduler

scheduler_obj = BlockingScheduler()

def run_job(text):
    print(text)

# The 'date' trigger and datetime.now() as run_date are implicit
scheduler_obj.add_job(run_job, args=['This is job argument'] )

scheduler_obj.start()