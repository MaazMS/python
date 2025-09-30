class BMW:

    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year

    def start(self) :
        print("starting of car")

    def stop(self) :
        print(" stopping of car")

    def display(self):
        print(" BMW car ")


class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled,  model, make, year ):
        BMW.__init__(self, model, make, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print("ThreeSeries of BMW")

    def start(self):
        print("button starting of car")

    def stop(self):
        print(" button stopping of car")


bmw = BMW("BMW", '328i', "2018")
bmw.start()
bmw.stop()
bmw.display()

threeSeries = ThreeSeries(True, "BMW", '328i', "2018")
threeSeries.start()
threeSeries.stop()
threeSeries.display()