class ArithmeticOperationList:
    def addition_opertion_list(self):

        list1 = [int(list1) for list1 in input().split()]
        list2 = [int(list2) for list2 in input().split()]
        addition = []

        for i in range(3):
            addition.append(list1[i] + list2[i])
        print("addition of list element", addition)

    def substraction_opertion_list(self):

        list1 = [int(list1) for list1 in input().split()]
        list2 = [int(list2) for list2 in input().split()]
        substraction = []

        for i in range(3):
            substraction.append(list1[i] - list2[i])
        print("substraction of list element", substraction)

    def multiplication_opertion_list(self):

        list1 = [int(list1) for list1 in input().split()]
        list2 = [int(list2) for list2 in input().split()]
        multiplication = []

        for i in range(3):
            multiplication.append(list1[i] * list2[i])
        print("multiplication of list element", multiplication)

    def divide_opertion_list(self):

        list1 = [int(list1) for list1 in input().split()]
        list2 = [int(list2) for list2 in input().split()]
        divide = []

        for i in range(3):
            divide.append(list1[i] / list2[i])
        print("divide of list element", divide)

    def Modulus_opertion_list(self):

        list1 = [int(list1) for list1 in input().split()]
        list2 = [int(list2) for list2 in input().split()]
        Modulus = []

        for i in range(3):
            Modulus.append(list1[i] % list2[i])
        print("Modulus of list element", Modulus)


obj = ArithmeticOperationList()
obj.addition_opertion_list()
obj.substraction_opertion_list()
obj.multiplication_opertion_list()
obj.divide_opertion_list()
obj.Modulus_opertion_list()
