from threading import *


class BookMyBus():

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Semaphore()

    def bus(self, seatsRequested):
        self.l.acquire()
        if (self.availableSeats >= seatsRequested):
            print("Total  seats avaialable ",self.availableSeats)
            print("conforming a seat")
            print("processing the payment")
            print("printing the ticket")
            self.availableSeats -= seatsRequested
        else:
            print("sorry no seats avaialable")
        self.l.release()


obj = BookMyBus(10)
t1 = Thread(target=obj.bus, args=(3,))
t2 = Thread(target=obj.bus, args=(3,))
t3 = Thread(target=obj.bus, args=(5,))

t1.start()
t2.start()
t3.start()