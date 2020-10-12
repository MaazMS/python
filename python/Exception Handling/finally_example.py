try:
	f = open("myfile", "w")
	a,b = [int(no) for no in input("Enter the number ").split()]
	c = a/b
	f.write("writing %d into file" %c)
# f.close()   # it is not execute if exception is throw
except ZeroDivisionError:
	print("divide by zero is not allowed")
finally:
	f.close() # it is  execute if exception is throw or  not and file close.
print("code after the except")