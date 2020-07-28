from time import sleep
import sqlalchemy as sa
import json

from apscheduler.schedulers.background import BackgroundScheduler

engine = sa.create_engine('sqlite:///add_job_sqlite_db.sqlite')

def alarm():
    print('Alarm')

if __name__ == '__main__':
    scheduler = BackgroundScheduler()

    scheduler.add_jobstore('sqlalchemy', engine=engine)

    scheduler.start()
    print("Started scheduler")

    return_job=scheduler.add_job(alarm, 'interval', seconds=2)
    print(return_job)
    print(type(return_job))


    print(scheduler.get_jobs)
    for job in scheduler.get_jobs():

        job_details = dict()
        job_details['name'] = "name: %s" % job.name
        job_details['trigger'] = "trigger: %s" % job.trigger
        job_details['next_run'] = "next_run: %s" % job.next_run_time
        job_details['handler'] = "handler: %s" % job.func

    job_details_json = json.dumps(job_details)
    print(job_details_json)

    try:
        while True:
            sleep(1)
    except (KeyboardInterrupt, SystemExit):
        pass