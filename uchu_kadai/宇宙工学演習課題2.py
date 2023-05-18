# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:28:35 2022

@author: kumak
"""
import matplotlib.pyplot as plt
def T_f(m_r):
    n_O=m_r/(32*(1+m_r))
    n_H=1/(2*(1+m_r))
    if n_H>n_O*2:
        n_w=n_O*2
        n_r=n_H-n_O*2
    else:
        n_w=n_H
        n_r=n_O-n_H/2
    q=n_w*1000*241.9
    Delta_T=2*q/8.314/7/(n_w+n_r)
    ans=300+Delta_T
    if ans>2500:
        ans=(8.314*7/2*(n_w+n_r)*300+n_w*1000*241.9*2)/(8.314*7/2*(n_w+n_r)+n_w*1000*241.9/2500)
    return ans

def isp(m_r,T_f):
    n_O=m_r/(32*(1+m_r))
    n_H=1/(2*(1+m_r))
    if n_H>n_O*2:
        n_w=n_O*2
        n_r=n_H-n_O*2
    else:
        n_w=n_H
        n_r=n_O-n_H/2
    ans=(2*0.96*8.314*7/2*(n_w+n_r)*1000*T_f*(1-(0.1013/15)**(0.4/1.4)))**(1/2)/9.8
    return ans
def rho(m_r):
    m_O=m_r/(1+m_r)
    m_H=1/(1+m_r)
    V_O=m_O/1.14
    V_H=m_H/0.07
    ans=1/(V_H+V_O)
    return ans
def f(rho):
    ans=1/(1+(1/0.1-1)*rho/0.3)
    return ans
def Lambda(f,ISP):
    ans=(2.71828**(-7000/9.8/ISP)-f)/(1-f)
    return ans
def M(m_r):
    n_O=m_r/(32*(1+m_r))
    n_H=1/(2*(1+m_r))
    if n_H>n_O*2:
        n_w=n_O*2
        n_r=n_H-n_O*2
    else:
        n_w=n_H
        n_r=n_O-n_H/2
    return 1/(n_w+n_r)
x=[]
y=[]
TF= []
m_r_max=0
Lambda_max=0
z=0
for i in range(3000):
    m_r=i/100
    x.append(m_r)
    y.append(Lambda(f((rho(m_r))),isp(m_r,T_f(m_r))))
    TF.append(T_f(m_r))
    if(y[i]>Lambda_max):
        m_r_max=x[i]
        Lambda_max=y[i]
        z=rho(m_r)
print(TF)
plt.plot(x,y)
print(m_r_max)
print(z)
plt.show()

plt.plot(x, TF)
plt.show()