
from datetime import datetime, timedelta 

# now = datetime.now()
# t = -1

# if t < 20 and t >= 0:
#     print("more 0")

# else:
#     print("less 0")
    
# print(now.weekday())
now = datetime.now()
now = datetime(year=now.year, month=now.month, day=now.day, hour=23, minute=46)
update_time = now + timedelta(minutes=15)

print( update_time.day - now.day)