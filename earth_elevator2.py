from matplotlib import pyplot as plt
from matplotlib import animation as ani
import sympy as sym
import numpy as np

fig=plt.figure()
ims=[]


m=1
G=6.6743*10**-11
p0=101325
T0=288.15
L0=0.0065
R0=8.31446
Mair=0.00289652
S=1*1*sym.pi
Cd=0.34
R=6400000

x=sym.Function('x')
t=sym.Symbol('t')

#def density(x):
#    if np.abs(x)<1300*10**3:
#        dense=13000-(13000-12600)*x/(1300*10**3)
#    elif np.abs(x)<3500*10**3:
#        dense=12200-(12200-9900)*(x-1300*10**3)/(3500*10**3-1300*10**3)
#    elif np.abs(x)<6345*10**3:
#        dense=5600-(5600-3300)*(x-3500*10**3)/(6345*10**3-3500*10**3)
#    elif np.abs(x)<6350*10**3:
#        dense=3000
#    elif np.abs(x)<6400*10**3:
#        dense=2700
#    return dense

#lg=density(x(t))
lg=5510
#g=G*4*sym.pi*x(t)*lg/3
g=9.8
#p=p0*(1-L0*(x(t)-R0)/T0)**(g*Mair/R0/L0)
#T=T0-L0*(x(t)-R0)
#lair=p*Mair/R0/T
lair=1.204
#k=1.8*10**-5

eq=-m*sym.Derivative(x(t),t,t)-m*g+(lair*S*Cd*(sym.Derivative(x(t),t))**2)/3
#eq=-m*sym.Derivative(x(t),t,t)-m*g-k*(sym.Derivative(x(t),t))




result=sym.dsolve(eq,x(t),ics={x(t).subs(t,0):R,sym.diff(x(t),t,1).subs(t,0):0})
print(result)
xresult=result.rhs
print(xresult)


tlist=np.linspace(0,100000,1000)
xsubs=[]
for i in range(len(tlist)):
    xsubs.append(xresult.subs(t,tlist[i]))

plt.plot(tlist,xsubs)
plt.show()
