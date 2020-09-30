# isalnum check string contain only character then true if other then character the false
# isalnum check digits contain only digit then true if other then digit the false

# isalpha return if string contain character if other then character then false

# Decimal characters are those that can be used to form numbers in base 10.
# isdecimal check Decimal return true other then false

# isidentifier check it is idendifier or not.
a = "Fitness"
print(a.isalnum())

a1 = "123"
print(a1.isalnum())

a2 = "$*%!!!"
print(a2.isalnum())

a3 = "0.34j"
print(a3.isalnum())

b = "Fitness"
print(b.isalpha())

b1 = "123"
print(b1.isalpha())

c = "123"
print(c.isdecimal())

c1 = "1.23"
print(c1.isdecimal())

d = "123"
print(d.isidentifier())

d1 = "_user_123"
print(d1.isidentifier())
