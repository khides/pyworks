from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from matplotlib.colors import ListedColormap



def plot_boundary(model,X,Y,target,xlabel,ylabel):
    cmap_dots=ListedColormap(['#1f77b4','#ff7f0e','#2ca02c'])
    cmap_fills=ListedColormap(['#c6dcec','#ffdec2','#cae7ca'])
    plt.figure(figsize=(5,5))

    if model:
        XX,YY=np.meshgrid(
            np.linspace(X.min()-1,X.max()+1,200),
            np.linspace(Y.min()-1,Y.max()+1,200)
        )
        pred=model.predict(np.c_[XX.ravel(),YY.ravel()]).reshape(XX.shape)
        plt.pcolormesh(XX,YY,pred,cmap=cmap_fills,shading='auto')
        plt.contour(XX,YY,pred,colors='gray')
    plt.scatter(X,Y,c=target,cmap=cmap_dots)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

#########################################
# データを用意する
X,y=make_blobs(
    random_state=4, #毎回同じ値が生成されるよう指定
    n_features=2, #特徴量の個数
    centers=3, #塊の個数
    cluster_std=2, #塊のばらつき
    n_samples=500 #サンプルの数
    )



#########################################################
# データを学習用とテスト用に分ける


Xtrain,Xtest,ytrain,ytest=train_test_split(
    X,
    y,
    random_state=0 #毎回分け方が変わってしまわないように固定
)


#########################################################
# モデルを選んで学習する


model=LogisticRegression()
model.fit(Xtrain,ytrain)


#######################################################
#モデルをテストする

pred=model.predict(Xtest)


#######################################################
#正答率を求める

score=accuracy_score(ytest,pred)
print('正答率{}%'.format(score*100))


######################################################
#新たな値を与えて予測する

pred1=model.predict([[1,0]])
print('1,0=',pred1)

pred2=model.predict([[1,4]])
print('1,4=',pred2)


###########################################################
#可視化

df=pd.DataFrame(Xtest)

plot_boundary(model,df[0],df[1],ytest,'df[0]','df[1]')