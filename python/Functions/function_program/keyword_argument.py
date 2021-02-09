"""
keyword argument is simply say that function definition and function call parameter having same variable name.
example
function definition    `def average(no1, no2):`
function call           average(no2=4 , no1= 2)
"""
def average(no1, no2):
    print("no1 = ", no1)
    print("no2 = ", no2)
    return (no1/no2)/2
print(average(2, 2))
print(average(no2=4 , no1= 2))