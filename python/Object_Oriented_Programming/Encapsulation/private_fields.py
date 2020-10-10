class Student:

    def __init__(self):
        self.__name = "Maaz"
        self.__roll_no = 123

    def display(self):
        print(self.__name)
        print(self.__roll_no)
s1 = Student()
s1.display()
