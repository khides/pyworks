data='abc,abc,abc\n'

print(data.split(','))

print(data.upper())

print(data.index(','))

print(data.strip())
print(data)



data='answer={0:*<6.1f}'
x=1/3
print(data.format(x))
print(data)


data='-'
print(data.join(['1','2','3']))
print(data)