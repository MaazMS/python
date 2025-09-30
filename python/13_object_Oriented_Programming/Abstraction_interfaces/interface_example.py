from abc import abstractmethod, ABC
class BMW(ABC):

    @abstractmethod
    def start(self) :
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

    def start(self):
        print("starting of car")

    def drive(self):
        print("drive a car")

threeSeries = ThreeSeries()
threeSeries.start()
threeSeries.drive()