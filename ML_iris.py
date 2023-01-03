from sklearn import datasets
import pandas as pd
from matplotlib import pyplot as plt

iris=datasets.load_iris()
print('特徴量の名前＝',iris.feature_names)
print('分類の名前＝',iris.target_names)
print('分類の値＝',iris.target)

df=pd.DataFrame(iris.data)
df.columns=iris.feature_names
df['target']=iris.target

print(df.head())


df0=df[df['target']==0]
df1=df[df['target']==1]
df2=df[df['target']==2]



#histogram

xx='sepal width (cm)'
df0[xx].hist(color='red',alpha=0.5)
df1[xx].hist(color='blue',alpha=0.5)
df2[xx].hist(color='green',alpha=0.5)
plt.xlabel(xx)
plt.title('sepal width hist')
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
ax.hist(df0[xx])
ax.hist(df1[xx])
ax.hist(df2[xx])
plt.show()


plt.hist(df0[xx],color='red',alpha=0.5)
plt.hist(df1[xx],color='blue',alpha=0.5)
plt.hist(df2[xx],color='green',alpha=0.5)
plt.grid()
plt.xlabel(xx)
plt.title('sepal width hist')
plt.show()


#scatter

xx='sepal width (cm)'
yy='sepal length (cm)'

df0.plot.scatter(xx,yy,color='red')
plt.grid()
df1.plot.scatter(xx,yy,color='blue')
plt.grid()
df2.plot.scatter(xx,yy,color='green')
plt.grid()
plt.xlabel(xx)
plt.ylabel(yy)
plt.show()



plt.scatter(df0[xx],df0[yy],color='red')
plt.scatter(df1[xx],df1[yy],color='blue')
plt.scatter(df2[xx],df2[yy],color='green')
plt.grid()
plt.xlabel(xx)
plt.ylabel(yy)
plt.show()


#3d scatter
from mpl_toolkits.mplot3d import Axes3D
zz='petal length (cm)'

ax=Axes3D(plt.figure(figsize=(5,5)))
ax.scatter(df0[xx],df0[yy],df0[zz],color='red')
ax.scatter(df1[xx],df1[yy],df1[zz],color='blue')
ax.scatter(df2[xx],df2[yy],df2[zz],color='green')
ax.set_xlabel(xx)
ax.set_ylabel(yy)
ax.set_zlabel(zz)
ax.view_init(0,240)
plt.show()