"""
A decorator is a function that takes another function and extends the behavior of the latter
function without explicitly modifying it.
Explain
function take function as parameter
Inside function define function and call the function which is function name as parameter
function return function name
For function call pass function name.
"""
def dec1(func):
    def nowexec():
        print("executing now")
        func()
        print("executed")
    return nowexec

def user_name():
    print("my name is Maaz")

# user_name() # simple function call
variable = dec1(user_name)
variable()