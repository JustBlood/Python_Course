from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import locale
'''
d1 = date(2019,3,12)
print(d1)
print(d1.year, d1.month, d1.day, "\n")

t1 = time(23,10,59)
print(t1, "\n")

print(date.today())
print(date.min,date.max)
print(time.min, time.max, "\n")

dt = datetime(2019,3,12,15,16)
print(dt)
print(dt.date().year)
print(dt.time().hour)
print(dt.hour, "\n")

now = datetime.now()
print(now)

new_dt = now.replace(year=2023)
print(new_dt, "\n")

'''
# %Y - XXXX year; %y - XX year
dt = datetime.strptime("30/08/2018", "%d/%m/%Y")
print(dt)

dt = datetime.strptime("29/03/2019 10:40", "%d/%m/%Y %H:%M")
print(dt)

dt = datetime.strptime("06-28-2022 09:20", "%m-%d-%Y %H:%M")
print(dt)

dt = datetime.strptime("2018-06-28", "%Y-%m-%d")
print(dt)

locale.setlocale(locale.LC_ALL,"")
now = datetime.now()
print(now.strftime('%Y-%m-%d (%A) %H:%M'))
print(now.strftime('%Y-%B-%d число, (%a)'))

delta1 = timedelta(days=3,hours=2,minutes=10)
print(delta1)

delta2 = timedelta(days=2,hours=1,minutes=5)
print(delta2)

print(delta1-delta2)
print(delta2-delta1)

my_birthday = date(2003,10,31)
delta = date.today() - my_birthday
print(delta, type(delta))

my_age = int(delta.days/365)
print(my_age)

wife_birthday = date(2003,5,7)
am_i_older = my_birthday < wife_birthday
print(am_i_older)