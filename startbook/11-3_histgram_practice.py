import collections

counter=collections.Counter([1,1,2,2,2,3])
print(counter)
print(counter[2])

import sqlite3
conn=sqlite3.connect('my_database.db')
data=[]
cur=conn.execute('select random_val from data_table')
for row in cur:
    data.append((int(row[0]*10)))

print(data[:10])


hist_data=collections.Counter(data)

for i in range(10):
    print('{:0.1f}〜{:0.1f}: {}個'.format(0.1*i,0.1*(i+1),hist_data[i]))


import turtle
import kame

turtle.setup(750,750,0,0)
hist_kame=kame.Kame()

hist_kame.histogram(hist_data)

turtle.done()
