from sklearn.datasets import make_gaussian_quantiles

X,y=make_gaussian_quantiles(
    random_state=3, #毎回同じランダムな値が生成されるように指定
    n_features=2, #特徴量数
    n_classes=3, #グループ3つ
    n_samples=300 #サンプル数
)

import pandas as pd

df=pd.DataFrame(X)
df['target']=y

df0=df[df['target']==0]
df1=df[df['target']==1]
df2=df[df['target']==2]

from matplotlib import pyplot as plt

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.scatter(df2[0],df2[1],color='green',label='2')
plt.grid()
plt.legend()
plt.show()
