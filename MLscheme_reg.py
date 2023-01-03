from statistics import linear_regression
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


#########################################
# データを用意する

X,y=make_regression(
    random_state=3, #毎回同じランダムな値が生成されるように指定
    n_features=1, #特徴量数
    noise=20, #ばらつき
    n_samples=30 #サンプル数
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


model=LinearRegression()
model.fit(Xtrain,ytrain)


#######################################################
#モデルをテストする

pred=model.predict(Xtest)


#######################################################
#正答率を求める

score=r2_score(ytest,pred)
print('正答率{}%'.format(score*100))


######################################################
#新たな値を与えて予測する

pred1=model.predict([[1]])
print('1=',pred1)

pred2=model.predict([[2]])
print('1=',pred2)


###########################################################
#可視化

df=pd.DataFrame(X)
df['target']=y


plt.figure(figsize=(5,5))
plt.scatter(df[0],df['target'],color='blue',label='data')
plt.plot(df[0],model.predict(X),color='red',label='reg')
plt.grid()
plt.show()