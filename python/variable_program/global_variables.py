# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside
# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function. The global variable with the same name will remain as it was,
# global and with the original value.
# create a global variable inside a function,  use the global keyword.
# change the value of a global variable inside a function, by using the global keyword:
# one one variable declare without value. if assign value at declaration time is give an error invalid syntax
# This variable global variable which is declare inside function using keyword global


global_variable = "global_variable"
change_globale_variable= "It is global variable"
def global_and_local_variable():
    change_globale_variable = "It is local varaible "
    print(global_variable)
    print(change_globale_variable)

def check_global_variable_value():
    print("check globale variable is ",global_variable)
    print("check globale variable is ",change_globale_variable)

def global_keyword():
    global global_variable
    global_variable = "The global variable is change "
    print(global_variable)


global_and_local_variable()
check_global_variable_value()
global_keyword()
print(global_variable)