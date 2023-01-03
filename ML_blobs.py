from sklearn.datasets import make_blobs

X,y=make_blobs(
    random_state=3, #毎回同じ値が生成されるよう指定
    n_features=2, #特徴量の個数
    centers=2, #塊の個数
    cluster_std=1, #塊のばらつき
    n_samples=300 #サンプルの数
    )

import pandas as pd

df=pd.DataFrame(X)

df['target']=y
print(df.head())

from matplotlib import pyplot as plt

df0=df[df['target']==0]
df1=df[df['target']==1]

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.grid()
plt.legend()
plt.show()



fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax1.scatter(df0[0],df0[1],color='b',alpha=0.5,label='0')
ax1.scatter(df1[0],df1[1],color='r',alpha=0.5,label='1')
ax1.grid()
ax1.legend()

ax2=fig.add_subplot(1,2,2)
ax2.scatter(df0[0],df0[1],color='b',alpha=0.5,label='0')
ax2.scatter(df1[0],df1[1],color='r',alpha=0.5,label='1')
ax2.grid()
ax2.legend()
plt.show()
