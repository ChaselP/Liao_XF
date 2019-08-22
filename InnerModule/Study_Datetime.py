from datetime import datetime,timezone,timedelta
import re

def to_timestamp(dt_str, tz_str):
    temp=re.match(r'UTC([\+|-][0-9]+):(.*)',tz_str).group(1)
    tz=timezone(timedelta(hours=int(temp)))
    t = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz)
    return datetime.timestamp(t)

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')