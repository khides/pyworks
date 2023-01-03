###階乗を計算する関数
def fact(n): 
    if n==0:
        return 1
    else:
        return n*fact(n-1)




###フィボナッチ数
def fib(n): 
    if n<1:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)




###指定したデータが昇順にした時何番目に初めて出現するか
def find_down(data,a): 
    data_up=sorted(data)
    start=0
    end=len(data)
    while start!=end:
        center=(start+end)//2
        if data_up[center]==a:
            while data_up[center]==a:
                center-=1
            return center+1
        if a<data_up[center]:
            end=center
        else:
            start=center+1




###指定したデータが昇順にしたとき何番目に最後に出現するか
def find_up(data,b):
    data_up=sorted(data)
    start=0
    end=len(data)
    while start!=end:
        center=(start+end)//2
        if data_up[center]==b:
            while data_up[center]==b:
                center+=1
            return center
        if b<data_up[center]:
            end=center
        else:
            start=center+1




###指定したデータがいくつリスト内に存在するか
def bs_count(data,a):
    return find_up(data,a)-find_down(data,a)
 




###二つのリストを比べて順に小さいほうからデータを取り上げる
import ita
def merge(a,b):
    r=ita.array.make1d(len(a)+len(b))
    A=a
    B=b
    if len(A)==0 and len(B)!=0:
        r=B
    elif len(A)!=0 and len(B)==0:
        r=A
    elif len(A)!=0 and len(B)!=0:
        if A[0]<=B[0]:
            X=ita.array.make1d(len(A)-1)
            X=A[1:]
            r=[A[0]]+merge(X,B)
        elif A[0]>B[0]:
            Y=ita.array.make1d(len(B)-1)
            Y=B[1:]
            r=[B[0]]+merge(A,Y)
    return r


import ita
def merge_rec(a,b):
    Ai=a
    Bi=b
    if len(Ai)==0 and len(Bi)!=0:
        return Bi
    elif len(Ai)!=0 and len(Bi)==0:
        return Ai
    elif len(Ai)!=0 and len(Bi)!=0:
        if Ai[0]>=Bi[0]:
            X=Bi[0]
            P=ita.array.make1d(len(Bi)-1)
            for i in range(len(Bi)-1):
                P[i]=Bi[i+1]
                Bi=P
            return [X]+merge_rec(Ai,Bi)
        else:
            Y=Ai[0]
            Q=ita.array.make1d(len(Ai)-1)
            for i in range(len(Ai)):
                Q[i]=Ai[i-1]
                Ai=Q
            return [Y]+merge_rec(Ai,Bi)




###sorted関数
def mergesort(a):
    n=len(a)
    if n<=1:
        return a
    else:
        l=mergesort(a[:n//2])
        r=mergesort(a[n//2:])
        return merge(l,r)





###最大公約数
def gcd(x,y):
    if x<y:
        x,y=y,x
    while y>0:
        x,y=y,x%y
    return x




###ユークリッドの互除法
def gcd_rec(n,m):
    if n<m:
        n,m=m,n
    elif m==0:
        return n
    else:
        return gcd_rec(m,n%m)




###二番目に大きい数
def sndmax(a):
    if len(a)<2:
        print('no')
    else:
        fst,sec=a[0],a[0]
        for x in a:
            if x>fst:
                sec=fst
                fst=x
            elif x>sec:
                sec=x
        return sec





###リストのi番目とm番目を入れ替える関数
def swap(a,i,m):
    tmp=a[i]
    a[i]=a[m]
    a[m]=tmp

###あるリストの要素で全体を割る
def prepare(a,k,i):
    factor=a[k][i]
    for j in range(0,len(a[k])):
        a[k][j]=a[k][j]/factor


def erase(a,j,i):
    factor=a[j][i]
    for k in range(0,len(a[j])):
        a[j][k]=a[j][k]-factor*a[i][k]
    
def maxrow(a,i):
#i行目以降でi列目の絶対値が最大の行
  m = i
  for j in range(i+1, len(a)):
    if abs(a[m][i]) < abs(a[j][i]):
      m = j
  return m


def fe(a):    # a は係数と右辺値を並べたもの
  for i in range(0,len(a)):
    swap(a, i, maxrow(a, i))
    prepare(a, i, i)     # a[i][i] を 1 にする 
    for j in range(i + 1, len(a)):
      erase(a, j, i)      
        


def calc_result(res, a, k):  # k 個目の変数値を求める
  res[k] = a[k][len(a[0]) - 1]   # まず右辺値を代入
  for j in range(k + 1, len(res)):
    res[k] = res[k] - res[j] * a[k][j] # 既知の変数の結果を反映




import ita
def bs(a):     # a は前進消去後を想定
  n = len(a[0])-1          # n 変数
  result = ita.array.make1d(n)
  for i in range(0, n):
    calc_result(result, a, n - i - 1)    # 後ろからi行目を使って解を計算 
  return result


###連立方程式を解く関数
def solve(a):   # a は係数と右辺値を並べたもの
  fe(a)
  return bs(a)


###学習した分類結果を塗りつぶす関数
from matplotlib import pyplot as plt
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