
#########################################
# データを用意する

from sklearn.datasets import make_blobs
import pandas as pd
from matplotlib import pyplot as plt

X,y=make_blobs(
    random_state=0, #毎回同じ値が生成されるよう指定
    n_features=2, #特徴量の個数
    centers=2, #塊の個数
    cluster_std=1, #塊のばらつき
    n_samples=300 #サンプルの数
    )


'''
df=pd.DataFrame(X)
df['target']=y
print(df.head())

df0=df[df['target']==0]
df1=df[df['target']==1]

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.grid()
plt.legend()
plt.show()
'''



#########################################################
# データを学習用とテスト用に分ける

from sklearn.model_selection import train_test_split

Xtrain,Xtest,ytrain,ytest=train_test_split(
    X,
    y,
    random_state=0 #毎回分け方が変わってしまわないように固定
)

'''
df=pd.DataFrame(Xtrain)
df['target']=ytrain

df0=df[df['target']==0]
df1=df[df['target']==1]

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.grid()
plt.legend()
plt.title('train:75%')
plt.show()

df=pd.DataFrame(Xtest)
df['target']=ytest

df0=df[df['target']==0]
df1=df[df['target']==1]

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.grid()
plt.legend()
plt.title('test:75%')
plt.show()
'''




#########################################################
# モデルを選んで学習する

from sklearn import svm

model=svm.SVC()
model.fit(Xtrain,ytrain)


#######################################################
#モデルをテストする

pred=model.predict(Xtest)

'''
df=pd.DataFrame(Xtest)
df['target']=pred

df0=df[df['target']==0]
df1=df[df['target']==1]

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.grid()
plt.legend()
plt.title('pridict')
plt.show()
'''

#######################################################
#正答率を求める

from sklearn.metrics import accuracy_score

score=accuracy_score(ytest,pred)
print('正答率{}%'.format(score*100))




######################################################
#新たな値を与えて予測する

pred1=model.predict([[1,3]])
print('1,3=',pred1)

pred2=model.predict([[1,2]])
print('1,2=',pred2)

'''
df=pd.DataFrame(Xtest)
df['target']=pred

df0=df[df['target']==0]
df1=df[df['target']==1]

plt.scatter(df0[0],df0[1],color='blue',label='0')
plt.scatter(df1[0],df1[1],color='red',label='1')
plt.scatter([1],[3],color='blue',marker='x')
plt.scatter([1],[2],color='red',marker='x')
plt.grid()
plt.legend()
plt.title('pridict')
plt.show()
'''


###################################################
#分類の状態を可視化する
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

df=pd.DataFrame(Xtest)
pred=model.predict(Xtest)
print(Xtest)
print(pred)
plot_boundary(model,df[0],df[1],pred,'df[0]','df[1]')




########################################################
#実践

from sklearn.datasets import make_moons
X,y=make_moons(
    random_state=3, #毎回同じ値が生成される
    noise=0.1, #ばらつき
    n_samples=300 #サンプル
)

df=pd.DataFrame(X)
model=svm.SVC()
model.fit(X,y)
plot_boundary(model,df[0],df[1],y,'df[0]','df[1]')