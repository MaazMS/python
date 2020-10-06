# input
full_name = input(" enter full name ")
print(full_name)

Roll_number = int(input(" enter number"))
print(Roll_number)

# multiple input separated by space
_list = [number  for number in input("enter multiple input separated by space  ").split()]
print(_list)

# multiple input separated by comma
_list = [number  for number in input("enter multiple number separated by comma  ").split(',')]
print(_list)

# multiple integer input separated by comma
_list = [ int(number)  for number in input("enter multiple number separated by comma  ").split(',')]
print(_list)