try:
	a,b = [int(no) for no in input("Enter the number ").split()]
	c = a/b
	print(c)
except ZeroDivisionError:
	print("divide by zero is not allowed")
print("code after the except")