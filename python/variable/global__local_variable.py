variable = "global variable"

def global_and_local_variable():

    print("same variable name of local and global variable")
    variable = " local variable "
    print(variable)


def globals_keyword():
    variable = " local variable "
    print(variable)
    print(globals()['variable'])

def  global_keyword():
    global variable
    variable = 10
    print(variable)

global_and_local_variable()
globals_keyword()
global_keyword()