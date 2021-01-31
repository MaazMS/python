class Cube_Square_Power:
    def cube(self):

        no = int(input("Enter number\t"))
        cube = no * no * no
        print("Cube of number is ", cube)

    def square(self):
        no = int(input("Enter number\t"))
        sq = no * no
        print("square of number is ", sq)

    def power_by_for(self):
        no = int(input("Enter number \t"))
        exponent = int(input("Enter exponent\t"))
        power = 1

        for i in range(1, exponent + 1):
            power = power * no
        print(
            "number is ",
            no,
            "\nnumber exponent is",
            exponent,
            "\nnumber power is",
            power,
        )


obj = Cube_Square_Power()
obj.cube()
obj.square()
obj.power_by_for()
