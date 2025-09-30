def decor(fun):
    def inner():
        dubble_decor_fun =  fun ()
        return dubble_decor_fun  * 2
    return inner

@decor
def num():
    return 5
print(num())