class EvenOdd:

    def even_number(self):

        no = int(input("Enter number \t"))

        if no<=0:
            print("Number is zero or negative")
        else:

            if no % 2 ==0 :
                print("Even number", no)
            else:
                print("Enter valid even number")
    def odd_number(self):

        no = int(input("Enter number \t"))

        if no<=0:
            print("Number is zero or negative")
        else:
            if no % 2 != 0:
                print("odd number", no)
            else:
                print("Enter valid odd number")
obj = EvenOdd()
obj.even_number()
obj.odd_number()
