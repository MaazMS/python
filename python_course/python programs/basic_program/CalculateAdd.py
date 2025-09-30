class CalculateAddition:

    def addint(self):

        no1 = int(input("Enter number 1       "))
        no2 = int(input("Enter number 2       "))

        print("Addition of two int number is     ", no1 + no2)

    def addfloat(self):
        no1 = float(input("Enter float no1          "))
        no2 = float(input("Enter float no2           "))
        add = no1 + no2
        print("sum of two flat number is        ", add)
obj = CalculateAddition()
obj.addint()
obj.addfloat()