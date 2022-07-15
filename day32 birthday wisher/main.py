import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)  # year is an int
month = now.month
print(month)

date_of_birth = dt.datetime(year=2010, month=6, day=25)
print(date_of_birth)




