
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

print('type = ',type(x))

print(x.strftime("%Y%m%d")) 
