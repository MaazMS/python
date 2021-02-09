"""
This program for writing for default argument,
first function call pass value to default argument parameter and non default argument parameter.
no1 =  2
no2 =  2
0.5
second function call not pass value to default argument parameter and pass value to non default argument parameter.
no1 =  2
no2 =  10
0.1
"""

def average(no1, no2=10):
    print("no1 = ", no1)
    print("no2 = ", no2)
    return (no1/no2)/2
print(average(2, 2))
print(average(no1= 2))