#  return the set_type_data of all elements in either number or number1, but not both
number = {1, 2 ,3 }
number1 = {4, 5, 6, 7}
print("isdisjoint using operator is & ")
print(number & number1)

print("isdisjoint method is union ")
print(number.isdisjoint(number1))

