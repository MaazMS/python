from abc import abstractmethod, ABC
class BMW(ABC):

    def start(self) :
        print("starting of car")

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

    def display(self):
        print("ThreeSeries of BMW")

    def drive(self):
        print("drive method implements because it is abstract method")
threeSeries = ThreeSeries()
threeSeries.start()
threeSeries.display()