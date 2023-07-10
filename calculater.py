import numpy as np
fw = 0.74
v = 1.43###
sigma = 60
m =5###
fb = 3
y = 0.433###
F = fw*(6.1/(6.1+v))*sigma*m*fb*np.pi*m*y
print(F)

v = 1.43
m = 5
Z1 =20
Z2 =73
F= 6.1/(6.1 + v)*m*fb*np.pi*m*2*Z1*Z2/(Z1 + Z2)
print(F)