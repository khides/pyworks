import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(font=['Meiryo','Yu Gothic','Hiragino Maru Gothic Pro'])


data=[
    [60,65,66],
    [80,85,88],
    [100,100,100]
    ]

#df=pd.DataFrame(data)
#df.columns=['国語','数学','英語']
#df.index=['A','B','C']


#col=['国語','数学','英語']
#idx=['A','B','C']
#df=pd.DataFrame(data,columns=col,index=idx)


data={
    '国語':[60,80,100],
    '数学':[65,85,100],
    '英語':[66,88,100],
    }
idx=['A','B','C']
df=pd.DataFrame(data,index=idx)
print(df)

print(type(df.plot()))
df.head()
print(list(df.columns))

df.plot.bar()
plt.legend()
plt.show()

data=[
    [1,1,1],
    [10,5,2],
    [4,4,3],
    [7,5,4],
    [5,6,7],
    [10,6,6],
    [1,7,9],
    [10,9,10]
]
col=['A','B','C']
df=pd.DataFrame(data,columns=col)
print(df)




bins=[1,3,5,7,9,11]
#plt.hist(df,bins=5,label=df.columns)
for i in df.columns:
    plt.hist(df[i],bins=bins,label=i,align='right')
df.plot.hist(bins=5)
plt.legend()
plt.show()

