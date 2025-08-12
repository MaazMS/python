import pickle
from python.file import  student_info

file_name = open("student_info.dat", "wb") # write binary file
object_name = student_info.Student("Maaz", 225)
pickle.dump(object_name, file_name)
file_name.close()