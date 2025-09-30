# The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers,
# starting with 0, and 1. The Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13.
#
class Fibonacci_Series:
    def find_fibonacci_series(self):
        n1, n2 = 0, 1
        count = 0

        number = int(input("Enter number \t"))
        if number < 0:
            print("Please enter a positive integer")
        elif number == 1:
            print("Fibonacci sequence is", number)
        else:
            while count < number:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1


obj = Fibonacci_Series()
obj.find_fibonacci_series()