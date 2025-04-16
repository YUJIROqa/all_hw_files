import datetime


now = datetime.datetime.now()
print(now)
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)

after_midnight = now - today_midnight
print(after_midnight.seconds)

print(now + datetime.timedelta(days=20, hours=10, minutes=15))



