class CalculateTriangle:

    def are(self):

        h = int(input("Enter height\t"))
        b = int(input("Enter base\t"))

        triangle_are = 1/2 * b * h

        print("area of triangle is ", triangle_are,"\n")

obj = CalculateTriangle()
obj.are()