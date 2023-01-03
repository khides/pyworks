from sklearn.datasets import make_blobs
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from my_module import plot_boundary

X,y=make_blobs(
    random_state=0, #毎回同じ値が生成されるよう指定
    n_features=2, #特徴量の個数
    centers=3, #塊の個数
    cluster_std=0.6, #塊のばらつき
    n_samples=200 #サンプルの数
    )


Xtrain,Xtest,ytrain,ytest=train_test_split(
    X,
    y,
    random_state=0 #毎回分け方が変わってしまわないように固定
)


model=RandomForestClassifier()
model.fit(Xtrain,ytrain)


pred=model.predict(Xtest)
score=accuracy_score(ytest,pred)
print('正答率{}%'.format(score*100))


df=pd.DataFrame(Xtest)
plot_boundary(model,df[0],df[1],ytest,'df[0]','df[1]')
