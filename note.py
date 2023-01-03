import sympy as sym

M=sym.Matrix([
    [0,3,3],
    [-3,0,2],
    [-3,-2,0]])
print(M.eigenvects())




import my_module

for i in range(10):
    print(my_module.fib(i))


data=[1,5,6,4,2,8,3,1,5,7,9,3,5,6,8,4,2]
print(sorted(data))

print(my_module.find_down(data,2))

print(my_module.find_up(data,2))

print(my_module.bs_count(data,2))


A=[4,2,5,9,7,6,6,4,7,1]
B=[8,6,4,2,5,7,5,2,1,5]

print(my_module.merge(A,B))


a=[1,9,2,8,2,3,7,6,4,6,5,9]
print(my_module.mergesort(a))

print(my_module.sndmax(a))

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap



def draw_circle(X,Y):
    Z=[]
    for i in range(len(X)):
        if X[i]**2+Y[i]**2<=0.25:
            Z.append(3)
        elif (X[i]-0.5)**2+Y[i]**2<=0.25:
            Z.append(4)
        elif (X[i]+0.5)**2+Y[i]**2<=0.25:
            Z.append(5)
        else:
            Z.append(2)
    return np.array(Z)

def draw_boudary(X,Y,pred,target,xlabel='',ylabel=''):
    cmap_dots=ListedColormap(['#1f77b4','#ff7f0e','#2ca02c'])
    cmap_fills=ListedColormap(['#c6dcec','#ffdec2','#cae7ca'])
    plt.figure(figsize=(5,5))
    
    XX,YY=np.meshgrid(
        np.linspace(X.min()-1,X.max()+1,200),
        np.linspace(Y.min()-1,Y.max()+1,200)
        )
    plt.pcolormesh(XX,YY,pred,cmap=cmap_fills,shading='auto')
    plt.contour(XX,YY,pred,colors='gray')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)    
    plt.scatter(X,Y,c=target,cmap=cmap_dots)
    plt.show()

X,Y=np.meshgrid(
    np.linspace(-1,1,11),
    np.linspace(-1,1,11)
    )
X=X.flatten()
Y=Y.flatten()
print(X,Y)

XX,YY=np.meshgrid(
            np.linspace(X.min()-1,X.max()+1,200),
            np.linspace(Y.min()-1,Y.max()+1,200)
            )
        
pred=draw_circle(XX.flatten(),YY.flatten()).reshape(XX.shape)
target=draw_circle(X,Y)

draw_boudary(X,Y,pred,target)


