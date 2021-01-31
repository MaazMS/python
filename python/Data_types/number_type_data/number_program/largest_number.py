class LargestNumber:
    def twonumber(self):

        no1 = int(input("Enter no1 \t"))
        no2 = int(input("Enter no2 \t"))

        if no1 > no2:
            print("No1 is greater\t", no1)
        elif no2 > no1:
            print("No2 is grater\t", no2)
        else:
            print("No1 and No2 both are equal")

    def threenumber(self):

        no1 = int(input("Enter No1 \t"))
        no2 = int(input("Enter No2 \t"))
        no3 = int(input("Enter No3 \t"))

        if (no1 > no2) and (no1 > no3):
            print("No1 is greater \t", no1)
        elif (no2 > no1) and (no2 > no3):
            print("No2 is greater \t", no2)
        elif (no3 > no1) and (no3 > no2):
            print("No3 is greater \t", no3)
        else:
            print("Either two number or three number equal")


obj = LargestNumber()
obj.twonumber()
obj.threenumber()
