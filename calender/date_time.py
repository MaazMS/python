import datetime as dt

next_time  = dt.datetime.now() + dt.timedelta(seconds=20)
print(next_time)
data_format = dt.datetime.strftime(next_time, "%Y-%m-%d- %H:%M:%S")
print(data_format)