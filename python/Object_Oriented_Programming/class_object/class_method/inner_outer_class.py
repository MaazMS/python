class Car:

    def __init__(self, make, year ):
        self.make = make
        self.year = year

    class Engine:

        def __init__(self, number):
            self.number = number

        def started(self):
            print(" Engine started")

c1 = Car("BMW", 2020)
E1 = c1.Engine("s6")
E1.started()
Car.Engine.started("s10")