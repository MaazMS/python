from threading import Thread

class myThread(Thread):

    def run(self):
        i = 0
        while (i <= 10):
            print(i)
            i += 1
t = myThread()
t.start()