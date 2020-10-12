import pickle

file_name = open("student_info.dat", "rb") # read binary file
obj = pickle.load(file_name)
obj.display()