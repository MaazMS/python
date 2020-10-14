from threading import *


class BookMyBus():

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats

    def bus(self, seatsRequested):
        if (self.availableSeats >= seatsRequested):
            print("Total  seats avaialable ", self.availableSeats)
            print("conforming a seat")
            print("processing the payment")
            print("printing the ticket")
            self.availableSeats -= seatsRequested
        else:
            print("sorry no seats avaialable")


obj = BookMyBus(10)
t1 = Thread(target=obj.bus, args=(3,))
t2 = Thread(target=obj.bus, args=(3,))
t3 = Thread(target=obj.bus, args=(5,))

t1.start()
t2.start()
t3.start()