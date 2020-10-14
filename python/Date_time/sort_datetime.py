from datetime import *

ldates = []

d1 = date (2020,10,13)
d2 = date (2020,2,13)
d3 = date (2020,5,13)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

for d in ldates:
	print(d)