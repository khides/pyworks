from datetime import timedelta,timezone,datetime
tz=timezone(timedelta(hours=+9),'JST')

now=datetime.now()
print(now)

now=datetime.now(timezone.utc)
print(now)

jst=now+timedelta(hours=+9)
print(jst)

now=datetime.now(tz)
print(now)

now=datetime(2022,9,4,12,49)
print(now)