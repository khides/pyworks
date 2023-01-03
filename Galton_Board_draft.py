import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import random
sns.set(font=['Meiryo','Yu Gothic','Hiragino Maru Gothic Pro'])


def galton(nail,count):
    data=[]
    for j in range(count):
        position=50
        for i in range(nail):
            p=random.random()
            if p<0.5:
                position+=0.5
            else:
                position-=0.5
        position=round(position)
        data.append(position)
    data=np.array(data)
    data=data.T
    df=pd.DataFrame(data)
    bins=np.linspace(1,nail+1,nail)
    df.hist(bins=bins,align='mid',color='r',label='galton')
    return df


count=10000
nail=100
gal=galton(nail,count)
print(gal.value_counts())


mu=float(gal.mean())
sigma=float(gal.std())

print(mu,sigma)

import numpy as np
'''
def draw_normal(mu,sigma,count):
    normal=np.random.normal(mu,sigma,count)
    #normal=normal.T
    normallist=np.zeros([1,count])
    for i in range(count):
        c=round(min(normal))
        while c<round(max(normal))+1:
            if c<=normal[i]<c:
                normallist[c+round(min(normal))]+=1
            c+=1
    x=np.arange(round(min(normal)),round(max(normal)),1)
    plt.plot(x,normallist)
       
    #df=pd.DataFrame(normal)
    
    #bins=np.linspace(1,nail+1,nail)
    #df.hist(bins=bins,align='mid',color='b')
'''


x=np.linspace(1,nail+1,10000)
#ideal_data=3*x
#ideal_data=np.exp(-((x-mu)/sigma)**2*0.5)/sigma*((2*np.pi)**0.5)
#plt.plot(x,ideal_data,label='ideal data')

from scipy.stats import norm
ideal_data=10000*norm.pdf(x=x,loc=mu,scale=sigma)
plt.plot(x,ideal_data,label='正規分布')
#draw_normal(mu,sigma,count)
plt.xlabel('玉の位置')
plt.ylabel('玉の個数')
plt.legend()
plt.show()

