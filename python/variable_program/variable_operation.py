# Assign values to multiple variables in one line.after one line value is not assign to variable
# Assign the same value to multiple variables in one line
# To combine both text and a variable uses the + character.
# + character is also use to add a variable to another variable
# For numbers, the + character works as a mathematical operator:
# If combine a string and number,It give you TypeError: can only concatenate str (not "int") to str

first_name, last_name = "Maaz", "Shaikh"
print(first_name)
print(last_name)

name = full_name = "Maaz Shaikh"
print(name)
print(full_name)

name = "Maaz"
print("Hello    "+name)

my_name = "Maaz"
surname = "Shaikh"
print(my_name+surname)

numnber1 = 1
numnber2 = 2
print(numnber1 + numnber2)


friute = "Apple"
quntity = 5
print(friute +quntity)
