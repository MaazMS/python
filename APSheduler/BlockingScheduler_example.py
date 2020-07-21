from datetime import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(some_job, 'interval', seconds=1)
    scheduler.start()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()