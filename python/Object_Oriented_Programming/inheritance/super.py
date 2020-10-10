class BMW:

    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year

    def display(self):
        print(" BMW car ")

class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled,  model, make, year):
        super().__init__(model, make, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        super().display()
        print("ThreeSeries of BMW")



bmw = BMW("BMW", '328i', "2018")
bmw.display()

threeSeries = ThreeSeries(True, "BMW", '328i', "2018")
threeSeries.display()