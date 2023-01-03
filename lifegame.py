def count_neighbor(data,i,j):#周囲の情報を得る
    count=0
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if 0<=k<len(data) and 0<=l<len(data[k]):
                count=count+data[k][l]
    return count-data[i][j]

def lg_rule(cur,neighbor):
    if cur==0:#もし任意の箇所が死んでて
        if neighbor==3:#周りに生存者が三名だったら
            return 1
        else:
            return 0
    else:
        if neighbor==2 or neighbor==3:
            return 1
        else:
            return 0

import ita
def lifegame_step(data):
    n=len(data)
    m=len(data[0])
    next=ita.array.make2d(n,m)
    for i in range(0,n):
        for j in range(0,m):
            c=count_neighbor(data,i,j)
            next[i][j]=lg_rule(data[i][j],c)
    return next

def lifegame(data,n):
    results=ita.array.make1d(n)
    for i in range(0,n):
        results[i]=data
        data=lifegame_step(data)
    return results
    
    
from matplotlib import pyplot as plt

data=ita.lifegame_glider()
images=lifegame(data,100)
anim=ita.plot.animation_show(images)
plt.show()