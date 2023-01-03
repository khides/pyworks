
import numpy as np
print('配列')
Aa=np.array([[0,1],
             [2,3]])
print(Aa)
Ba=np.array([[1,2],
             [3,4]])
print(Ba)
print(Aa*Ba)
print(type(Aa*Ba))

print('行列')
Am=np.mat([[0,1],
           [2,3]])
print(Am)
Bm=np.mat([[1,2],
           [3,4]])
print(Bm)
print(Am*Bm)

print('配列×行列')
print(Aa*Bm)
print('行列×配列')
print(Am*Ba)
print(type(Am*Ba))

print('empty')
X=np.empty([2,2])
X[0][0]=0
X[0][1]=1
X[1][0]=2
X[1][1]=3
print(type(X))
print('')

print('ones')
X=np.ones([2,2])
print(X)
print(type(X))
print('')

print('ones_like1')
X=np.ones_like(Aa)
print(X)
print(type(X))
print('')

print('ones_like2')
X=np.ones_like(Am)
print(X)
print(type(X))
print('')

print('zeros')
X=np.zeros([2,2])
print(X)
print(type(X))
print('')

print('zeros_like1')
X=np.zeros_like(Aa)
print(X)
print(type(X))
print('')

print('zeros_like2')
X=np.zeros_like(Am)
print(X)
print(type(X))
print('')

E=np.eye(2)
print(E)

tri=np.tri(2)
print(tri)

tile=np.tile([1,2,3],3)
print(tile)
print('')

print('meshgrid')
X=np.meshgrid(Aa,Bm)
print(X)
print(type(X))
print('')

print('random')
X=np.random.random(5)
print(X)
print(type(X))
print('')

print('randint')
X=np.random.randint(0,10,[2,3])
print(X)
print(type(X))
print('')

print('copy')
X=Am.copy()
print(X)
print(type(X))
print('')

print('append')
X=np.append(Aa,Ba)
print(X)
print(type(X))
print('')

print('reshape')
X=Am.reshape(1,4)
print(X)
print(type(X))
print('')


print('astype')
X=Aa.astype(str)
print(X)
print(type(X))
print('')

print('vstack')
X=np.vstack([Aa,Bm])
print(X)
print(type(X))
print('')

print('allclose')
X=np.allclose(Aa,Am)
print(X)
print(type(X))
print('')

print('roll')
X=np.roll(Aa,1)
print(X)
print(type(X))
print('')

print('ndim')
X=Aa.ndim
print(X)
print(type(X))
print('')


print('shape')
X=Aa.shape
print(X)
print(type(X))
print('')

print('size')
X=Aa.size
print(X)
print(type(X))
print('')

print('nbytes')
X=Aa.nbytes
print(X)
print(type(X))
print('')

print('itemsize')
X=Aa.itemsize
print(X)
print(type(X))
print('')


print('where')
X=np.where(Aa>0)
print(X)
print(Aa[X])
print(type(X))
print('')


print('.A')
X=Am.A
print(X)
print(type(X))
print('')


print('matrix')
X=np.mat(Aa)
print(X)
print(type(X))
print('')


#print('')
#X=np.()
#print(X)
#print(type(X))
#print('')