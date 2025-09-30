# number greater then zero is Positive no.
# number less then zero is Positive no.
class PositiveNegativeNumbe:

    def positive_number(self):

        no = int(input("Enter number \t"))
        if no > 0 :
            print("Positive number", no)
        else:
            print("It is not Positive number")

    def negative_number(self):

        no = int(input("Enter number \t"))
        if no < 0:
            print("negative number", no)
        else:
            print("It is not negative number")

obj = PositiveNegativeNumbe()
obj.positive_number()
obj.negative_number()