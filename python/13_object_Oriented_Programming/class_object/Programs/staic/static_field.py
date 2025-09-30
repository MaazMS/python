class Student:

    bord = "state bord"
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

s1  = Student("Shaikh", 1)
print(s1.name)
print(s1.rollno)
print(s1.bord)
print(Student.bord)

print("==============================================")
s2  = Student("Maaz", 2)
print(s2.name)
print(s2.rollno)
print(s2.bord)
print(Student.bord) 