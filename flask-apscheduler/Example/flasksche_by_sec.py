from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler =  APScheduler()

@app.route("/")
def index():
    return "Hello World"

def schedulerTask():
    print("This sheduler work every 2 second")

if __name__=='__main__':
    scheduler.add_job(id ='Sheduler Task', func= schedulerTask, trigger = 'interval', seconds= 2)
    scheduler.start()
    app.run(host= '0.0.0.0', port= 8080   )