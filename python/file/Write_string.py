# The first step to write to a file is to open the file itself.
# open the file for writing

f = open("myfile.txt", "w")
txt = input("enter the text ")
f.write(txt)
f.close()
