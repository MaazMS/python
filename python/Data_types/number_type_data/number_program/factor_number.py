# A factor is a number that divides into another number exactly and without leaving a remainder.
# factor of 6 is 1, 2, 3, 6
#
class FactorNumber:
    def find_factor_number(self):

        no = int(input("Enter number \t"))

        if no < 0:
            print("Enter positive number")
        else:
            for i in range(1, no + 1):
                if no % i == 0:
                    print(i)


obj = FactorNumber()
obj.find_factor_number()
