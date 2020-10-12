import logging

logging.basicConfig(filename= "anyname.log", level=logging.DEBUG)

try:
	f = open("myfile", "w")
	a,b = [int(no) for no in input("Enter the number ").split()]
	logging.info("division in progress")
	c = a/b
	f.write("writing %d into file" % c)
# f.close()   # it is not execute if exception is throw

except ZeroDivisionError:
	print("divide by zero is not allowed")
	logging.error("divide by zero")

else:
	print("you have to inter non zero number")
finally:
	f.close() # it is  execute if exception is throw or  not and file close.
print("code after the except")
