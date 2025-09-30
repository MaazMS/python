def factorial(no):
    if no== 0:
        result = 1
    else:
        result = no * factorial(no -1)
    return result

print(factorial(3))