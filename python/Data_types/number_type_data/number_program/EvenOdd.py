class EvenOdd:
    def even_number(self):

        no = int(input("Enter number \t"))

        if no <= 0:
            print("Number is zero or negative")
        else:

            if no % 2 == 0:
                print("Even number", no)
            else:
                print("Enter valid even number")

    def odd_number(self):

        no = int(input("Enter number \t"))

        if no <= 0:
            print("Number is zero or negative")
        else:
            if no % 2 != 0:
                print("odd number", no)
            else:
                print("Enter valid odd number")

    def even_odd_by_for(self):

        no = int(input("Enter number \t"))
        if no <= 0:
            print("number is zero or negative")

        for i in range(1, no + 1):
            if i % 2 == 0:
                print("Even number is \t", i)
            elif i % 2 != 0:
                print("Odd number is \t", i)

    def even_odd_by_while(self):

        no = int(input("Enter number \t"))
        if no <= 0:
            print("number is negative or zero")
        else:
            i = 1
            while i <= no:
                if i % 2 == 0:
                    print("Even number is \t", i)
                elif i % 2 != 0:
                    print("Odd number is \t", i)
                i = i + 1


obj = EvenOdd()
obj.even_number()
obj.odd_number()
obj.even_odd_by_for()
obj.even_odd_by_while()
