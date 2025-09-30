class Programmer:

    def setName(self, user_name):
         self.__name  = user_name

    def getName(self):
        return self.__name

    def setSalary(self, Sal):
        self.__salary = Sal

    def getSalary(self):
        return self.__salary

p1 = Programmer()
p1.setName("Name")
p1.setSalary(2000)

print(p1.getName())
print(p1.getSalary())