import datetime
# to get date time now
x = datetime.datetime.now()
print(x)
# get year
print(x.year)
# name of weekday
print(x.strftime("%A") + str(x.month) + " " + str(x.year))
print(x.strftime("%p"))
