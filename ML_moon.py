from sklearn.datasets import make_moons

X,y=make_moons(
    random_state=3, #毎回同じランダムな値が生成されるように指定
    noise=0.1, #ばらつき
    n_samples=300 #サンプル数
)

import pandas as pd

df=pd.DataFrame(X)
df['target']=y

df0=df[df['target']==0]
df1=df[df['target']==1]

from matplotlib import pyplot as plt

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.grid()
plt.legend()
plt.show()
