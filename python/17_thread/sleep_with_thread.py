from threading import *
from time import sleep


class myThread():

    def dispalynumber(self):
        i = 0
        while (i <= 10):
            print(i)
            i += 1


obj = myThread()
t = Thread(target=obj.dispalynumber)
t.start()
sleep(5)
t1 = Thread(target=obj.dispalynumber)
t1.start()