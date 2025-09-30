from threading import *


class myThread:

    def dispalynumber(self):
        print(current_thread().getName())
        i = 0
        while (i <= 10):
            print(i)
            i += 1


obj = myThread()
t = Thread(target=obj.dispalynumber)
t.start()
