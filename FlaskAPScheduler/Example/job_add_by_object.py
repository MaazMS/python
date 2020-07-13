from flask import Flask
from flask_apscheduler import APScheduler


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'job_add_by_object:job1',   # file name:function name
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 1
        }
    ]

    SCHEDULER_API_ENABLED = True


def job1(a, b):
    print(str(a) + ' ' + str(b))


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())
    #  form_objectUpdates the values from the given object
    # The configuration dictionary as :class:`Config`  This behaves exactly like a regular dictionary
    # but supports additional methods to load a config from files.
    # The keys will be function names which are also used to generate URLs and the values are
    # the function objects themselves.

    scheduler = APScheduler()
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True

    scheduler.init_app(app)
    scheduler.start()

    app.run()