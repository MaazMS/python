try:
	num  = int(input("enter the numbr"))
	assert num % 2== 0, "you have to enter the odd number"
except AssertionError as obj:
	print(obj)
print("you have to handel assertion")