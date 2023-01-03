from sklearn.datasets import load_digits
from sklearn import decomposition
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


digits=load_digits()
X=digits.data #数字の画像データ
y=digits.target #画像データに対応する数字の名前

numbercolor=['BLACK','BROWN','RED','DARKORANGE','GOLD','GREEN','BLUE','PURPLE','GRAY','SKYBLUE']

colors=[]
for i in y: #何百個とあるｙそれぞれに対応した色のリストを作る
    colors.append(numbercolor[i])

pca=decomposition.PCA(n_components=3)
feature3=pca.fit_transform(X) #64個ある特徴量を三個に減らす


df=pd.DataFrame(feature3)

#3ｄグラフの準備
fig=plt.figure(figsize=(12,12))
ax=fig.add_subplot(projection='3d')

ax.scatter(df[0],df[1],df[2],color=colors)

#数字の色のラベルをつくる
ty=0
for col in numbercolor:
    ax.text(50,30,30-ty*5,str(ty),size=20,color=col)
    ty+=1

#グラフの初期視点の角度を指定する
ax.view_init(45,45)

plt.show()