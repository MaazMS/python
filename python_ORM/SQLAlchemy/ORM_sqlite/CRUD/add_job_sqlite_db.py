from time import sleep
import sqlalchemy as sa
import json

from apscheduler.schedulers.background import BackgroundScheduler

engine = sa.create_engine('sqlite:///add_job_sqlite_db.sqlite')

def alarm():
    print('Alarm')



if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    print(type(scheduler))
    scheduler.add_jobstore('sqlalchemy', engine=engine)
    print(engine)

    scheduler.start()
    return_job=scheduler.add_job(alarm, 'interval', seconds=2, )
    print(return_job)
    print(type(return_job))

    job_details = {}
    for job in scheduler.get_jobs():

        job_details['id'] = "%s" % job.id
        job_details['name'] = "%s" % job.name
        job_details['trigger'] = "%s" % job.trigger
        job_details['next_run'] = "%s" % job.next_run_time
        job_details['handler'] = "%s" % job.func
        job_details['executor'] = "%s" % job.executor

    print(job_details)

    job_details_json = json.dumps(job_details)
    print(job_details_json)

    try:
        while True:
            sleep(1)
    except (KeyboardInterrupt, SystemExit):
        pass


#     job_details['status'] = "%s" % job.status
# AttributeError: 'Job' object has no attribute 'status