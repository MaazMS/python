class NaturalNumber:

    def natural_no_by_for(self):

        no = int(input("Enter number \t"))

        if (no<=0):
            print("number is zero or negative")
        else:
            print("Display natural number")
            for i in range(1, no+1):
                print(i)
    def natural_no_by_while(self):

        no = int(input("Enter number\t"))

        if no <=0 :
            print("number is zero and negative")
        else:
            print("Display natural number")
            i = 1
            while(i<=no):
                print(i)
                i = i +1

    def natual_no_reverse(self):

        no = int(input("Enter number \t"))
        if no <=0:
            print("number is zero or negative")
        else:
            print("display reverse natural number ")
            i = 1
            while(no>=i):
                print(no)
                no = no - 1

    def sum_avg_by_for(self):

        no = int(input("Enter Number \t"))
        if(no<=0):
            print("Number is zero or negative")
        else:
            print("Display sum and avg of natural number")
            sum_natural = 0

            for i in range(1, no+1):
                sum_natural = sum_natural + i

            print("sum of natural number is \t",sum_natural)
            avg_natural = sum_natural / no
            print("avg of natural number is \t", avg_natural)

    def sum_avg_by_while(self):

        no = int(input("Enter number \t"))

        if(no<=0):
            print("Number is zero and negative")
        else:
            print("display sum and natural number by while loop")

            sum_natural = 0
            i = 1
            while(i <=no):
                sum_natural = sum_natural + i
                i = i +1
            print("sum of natural number is \t",sum_natural)
            avg_natural = sum_natural / no
            print("avg of natural number is ",avg_natural)


obj = NaturalNumber()
# obj.natural_no_by_for()
# obj.natural_no_by_while()
# obj.natual_no_reverse()
# obj.sum_avg_by_for()
obj.sum_avg_by_while()