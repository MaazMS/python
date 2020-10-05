# It is check string contain only character or only digits without decimal then true otherwise false.

# isalpha return if string contain character if other then character then false

# Decimal  are those that can be used to form numbers by base 10 1.e 1 , 3, 5,etc.
# isdecimal check Decimal return true other then false

# isidentifier check it is idendifier or not.
a = "Fitness"
print("a = ", a.isalnum())

a1 = "123"
print("a1 = ", a1.isalnum())

a2 = "$*%!!!"
print("a2 = ", a2.isalnum())

a3 = "0.34j"
print("a3 = ", a3.isalnum())

b = "Fitness"
print("b = ", b.isalpha())

b1 = "123"
print("b1 = ", b1.isalpha())

c = "123"
print("c = ", c.isdecimal())

c1 = "1.23"
print("c1 = ", c1.isdecimal())

d = "123"
print("d = ", d.isidentifier())

d1 = "_user_123"
print("d1 = ", d1.isidentifier())
