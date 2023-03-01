
from datetime import date
import time
start_time = time.perf_counter()
ldates = []

d1 = date (2020,1,13)
d2 = date (2020,2,13)
d3 = date (2020,5,13)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()
time.sleep(10)

for d in ldates:
	print(d)

end_time = time.perf_counter()
print("excecution time", end_time - start_time)