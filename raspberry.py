import numpy as np

sigma = 184
R = 6
r2 = 79
r1 = 35

T = (0.4*8*sigma*np.pi*R**2*(r2**3-r1**3))/(r2**2-r1**2)/3

print(T/1000/150)