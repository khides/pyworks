from sklearn.datasets import make_regression

X,y=make_regression(
    random_state=3, #毎回同じランダムな値が生成されるように指定
    n_features=2, #特徴量数
    noise=3, #ばらつき
    bias=100, #ｙ切片
    n_samples=300 #サンプル数
)

import pandas as pd

df=pd.DataFrame(X)

from matplotlib import pyplot as plt

plt.scatter(df[0],y,color='blue',label='0')
plt.grid()
plt.legend()
plt.show()


'''
自動生成されたシンプルなデータセットは、
学習モデルをテストするのに有用
'''