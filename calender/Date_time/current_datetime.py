import datetime

dt = datetime.datetime.today()
print(dt.day, dt.month, dt.year)
print(dt.hour, dt.minute, dt.second)

print("current datte{}\{}\{}".format(dt.day, dt.month, dt.year))
print("current time {}:{}:{}".format(dt.hour, dt.minute, dt.second))