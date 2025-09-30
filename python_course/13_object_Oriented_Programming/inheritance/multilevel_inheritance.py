class BMW:

    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year

    def start(self) :
        print("starting of car")

    def stop(self) :
        print("stopping of car")
class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled,  model, make, year ):
        BMW.__init__(self, model, make, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print("ThreeSeries of BMW")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled,  model, make, year ):
        BMW.__init__(self, model, make, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def display(self):
        print("FiveSeries of BMW")

threeSeries = ThreeSeries(True, "BMW", '328i', "2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.model)
print(threeSeries.make)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = ThreeSeries(True, "BMW", '508i', "2020")
print(fiveSeries.cruiseControlEnabled)
print(fiveSeries.model)
print(fiveSeries.make)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()