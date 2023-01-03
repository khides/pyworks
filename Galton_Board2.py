import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import random
from scipy.stats import norm
sns.set(font=['Meiryo','Yu Gothic','Hiragino Maru Gothic Pro'])

#ゴルトンボードをシミュレーション　stepsが釘の数、countがボールの数
def galton(steps,count):
    data=[]
    for j in range(count):
        position=50
        for i in range(steps):
            p=random.random()
            if p<0.5:
                position+=0.5
            else:
                position-=0.5
        position=round(position)
        data.append(position)
    df=pd.DataFrame(data)
    df=df.T
    bins=np.linspace(1,steps+1,steps)
    sns.distplot(df,bins=bins,fit=norm,\
        fit_kws={'color':'blue','label':'正規分布回帰'},\
        color='r',label='galton')
    return df
    


count=10000
steps=100
gal=galton(steps=steps,count=count)
#rint(gal.value_counts())

plt.xlabel('玉の位置')
plt.ylabel('玉の個数')
plt.legend()
plt.show()