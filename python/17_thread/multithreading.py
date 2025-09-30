from threading import *
import threading

class myThread():

    def dispalynumber(self):
        i = 0
        print("\n",threading.current_thread().getName(),"\n")
        while (i <= 10):
            print(i)
            i += 1


obj = myThread()
t = Thread(target=obj.dispalynumber)
t.start()

t1 = Thread(target=obj.dispalynumber)
t1.start()

t2 = Thread(target=obj.dispalynumber)
t2.start()