class PerfectNumber:

    def find_perfect_number(self):

        no = int(input("Enter number \t"))

        if no <= 0:
            print("Enter positive number")
        else:
            sum = 0
            for i in range(1, no+1):
                if no % i == 0:
                    sum = sum + 1
            if sum == no:
                print("The number is a Perfect number")
            else:
                print("The number is not a Perfect number")


obj = PerfectNumber()
obj.find_perfect_number()