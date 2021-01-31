class PrimeNumber:

    def find_prime_number(self):

        no = int(input("Enter number \t"))

        if no <= 0:
            print("Enter positive number")
        elif no > 1:
            for i in range(2, no):
                if no % i == 0:
                    print(no, "is not a prime number")
                    break
                else:
                    print(no)


obj = PrimeNumber()
obj.find_prime_number()
