#  return the set_type_data of allnumber.symmetric_difference(number1) elements in either number or number1, but not both
number = {1, 2 ,3 ,4}
number1 = {4, 5, 6, 7}
print("difference using operator is ^ ")
print(number ^ number1)

print("difference method is union ")
print(number.symmetric_difference(number1))

