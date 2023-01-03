import datetime

today=datetime.datetime.now()
print(today)
tomorrow=today+datetime.timedelta(1)
print(tomorrow)


if today.weekday()<5:
    print('今日も頑張って働こう')


if tomorrow.weekday()<5:
    print('明日も頑張って働こう')


if today.weekday()<5:
    print('今日も頑張って働こう')
else :
    print('休日だー')


if today.weekday()<4:
    print('今日も頑張って働こう')
elif today.weekday()==4:
    print('ゆっくりやろう')
else :
    print('休日だー')