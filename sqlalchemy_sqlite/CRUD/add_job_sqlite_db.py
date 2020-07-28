from time import sleep
import sqlalchemy as sa

from apscheduler.schedulers.background import BackgroundScheduler

engine = sa.create_engine('sqlite:///add_job_sqlite_db.sqlite')

def alarm():
    print('Alarm')

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    print("created scheduler")

    scheduler.add_jobstore('sqlalchemy', engine=engine)
    print("Added jobstore")


    scheduler.start()
    print("Started scheduler")
    return_job=scheduler.add_job(alarm, 'interval', seconds=2)
    print(return_job)
    try:
        while True:
            sleep(1)
    except (KeyboardInterrupt, SystemExit):
        pass