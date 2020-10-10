class Programmer:

    def __init__(self):
        self.__name = "Maaz"
        self.__salary = 2020

    def getName(self):
        return self.__name


    def getSalary(self):
        return self.__salary

p1 = Programmer()

print(p1.getName())
print(p1.getSalary())