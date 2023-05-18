# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:04:24 2022

@author: Micro
"""
import numpy as np

mix_ratio = []
a = 0
while(a<10):
    mix_ratio.append(a)
    a += 0.01

l = len(mix_ratio)
    
raw = []  
M = []
Tf = []
for i in mix_ratio:
    raw_1 = 0.071/(1 + i) + 1.14*i/(1 + i)
    raw.append(raw_1)
    M_1 = 2.02/(1 + i) + 32*i/(1 + i)
    M.append(M_1)
    if(i<2.117):
        Tf_1 = (483800*i/465.584) + 300
    elif(i>=8):
        Tf_1 = (8729.7*i + 7810637.6)/(29.099*i + 1780.952)
    else:
        Tf_1 = (967600*i + 139675.2)/(193.52*i + 465.584)
    Tf.append(Tf_1)

Cp = []
for i in M:
    Cp_1 = (7/2)*(8.314*10**3/i)
    Cp.append(Cp_1)

finert = []
for i in range(l):
    finert_1 = 1/(30*raw[i] + 1)
    finert.append(finert_1)

Vj = []
for i in range(l):
    Vj_1 = np.sqrt(2*0.96*Cp[i]*Tf[i] * (1 - (0.01/12)**(2/7)))
    Vj.append(Vj_1)
    
ISP = []
for i in mix_ratio:
    ISP_1 = 3.97*np.sqrt((i+8)*(9.68*1000*i + 1.4*1000)/(i+1)/(1.94*i+4.66))
    ISP.append(ISP_1)

lamda = []
for i in range(l):
    lamda_1 = (np.exp(-7000/ISP[i]/9.80665) - finert[i])/(1-finert[i])
    lamda.append(lamda_1)
    
def most_near(A,n):
    a = 100
    for i in A:
        if(i<n):
            if(a > abs(i-n)):
                a = i
    return(a)

lamda_index = lamda.index(max(lamda))
mix_index = mix_ratio[lamda_index]
print("mix_ratio=", mix_index, "Tf=", Tf[lamda_index], "ISP=", ISP[lamda_index])
print(lamda[lamda_index])
#raw = 0.071/(1 + mix_ratio) + 1.14(1 - 1/(1 + mix_ratio))
#finert = 1/(30*raw + 1)
#M = 2.02/(1 + mix_ratio) + 32(1 - 1/(1 + mix_ratio))
#Cp = (7/2)*(8.314/M)
#Tf = (967600*mix_ratio + 139675.2)/(193.52*mix_ratio + 465.584)
#Vj = (2*0.96*Cp*Tf*(1 - 0.01/12)**(2/7))**0.5
#ISP = Vj/9.80665
#lamda = (np.exp(-7000/9.80665/ISP) - finert)/(1-finert)

from matplotlib import pyplot as plt 
plt.plot(mix_ratio, finert, color="blue")
#plt.plot(mix_ratio, lamda, label="rocket", color="green")
#plt.axhline(y=3600, linestyle='solid', color='red')
plt.xlabel("Mixture ratio [mo/mf]")
plt.ylabel("Combustion temperature")
plt.legend()
plt.show()