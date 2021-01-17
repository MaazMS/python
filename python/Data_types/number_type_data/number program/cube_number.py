class CubeNumber:

    def cube(self):

        no = int(input("Enter number\t"))
        cube = no * no * no
        print("Cube of number is ", cube)

obj = CubeNumber()
obj.cube()