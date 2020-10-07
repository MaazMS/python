def decor(fun):
    def inner():
        dubble_decor_fun =  fun ()
        return dubble_decor_fun  * 2
    return inner
def num():
    return 5

result = decor(num)
print(result())