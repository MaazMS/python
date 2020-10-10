class Programmer:

    def setName(self, user_name):
        self.name = user_name

    def getName(self):
        return self.name

    def setSalary(self, Sal):
        self.Salary = Sal

    def getSalary(self):
        return self.Salary

p1 = Programmer()
p1.setName("Name")
p1.setSalary(2000)

print(p1.getName())
print(p1.getSalary())