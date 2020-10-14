from threading import *
import threading

class BookMyBus():

    def bus(self):
        print("\n", threading.current_thread().getName(), "\n")
        print("conforming a seat")
        print("processing the payment")
        print("printing the ticket")


obj = BookMyBus()
t1 = Thread(target=obj.bus)
t2 = Thread(target=obj.bus)
t3 = Thread(target=obj.bus)

t1.start()
t2.start()
t3.start()