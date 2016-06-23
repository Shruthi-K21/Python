from datetime import datetime

now = datetime.now()
print now.day
print now.month
print now.year
print now.hour
print now.minute
print now.second
print "%s/%s/%s %s:%s:%s" %(now.month,now.day,now.year,now.hour,now.minute,now.second)
