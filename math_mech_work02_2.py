import sympy as sp
from matplotlib import pyplot as plt
from sympy.solvers.ode.systems import dsolve_system
import numpy as np
from matplotlib import animation

sp.init_printing()

def four_spring_motion(x0,y0,vx0,vy0,m=2,k=100,l=100):
    t=sp.Symbol('t')
    x=sp.Function('x')(t)
    y=sp.Function('y')(t)

    eq1=m*sp.Derivative(x,t,t)-(
        (k*(l-(x**2+(y-l)**2)*0.5))*x/((x**2+(y-l)**2)**0.5)-
        (k*(((x+l)**2+y**2)**0.5-l))*(x+l)/(((x+l)**2+y**2)**0.5)-
        (k*((x**2+(y+l)**2)**0.5-l))*x/((x**2+(y+l)**2)**0.5)+
        (k*(l-((x-l)**2+y**2)**0.5))*(x-l)/(((x-l)**2+y**2)**0.5)
    )
    eq2=m*sp.Derivative(y,t,t)-(
        (k*(l-(x**2+(y-l)**2)*0.5))*(y-l)/((x**2+(y-l)**2)**0.5)-
        (k*(((x+l)**2+y**2)**0.5-l))*y/(((x+l)**2+y**2)**0.5)-
        (k*((x**2+(y+l)**2)**0.5-l))*(y+l)/((x**2+(y+l)**2)**0.5)+
        (k*(l-((x-l)**2+y**2)**0.5))*y/(((x-l)**2+y**2)**0.5)
    )



    eq2=m*sp.Derivative(y,t,t)+2*k*y
    eqs=[eq1,eq2]

    ans=dsolve_system(eqs,ics={x.subs(t,0):x0,y.subs(t,0):y0,
        sp.diff(x,t,1).subs(t,0):vx0,sp.diff(y,t,1).subs(t,0):vy0})
    return ans

ans=four_spring_motion(1,0,0,10)
print(ans)

#print(ans[0][0].rhs,ans[0][1].rhs)

t=sp.Symbol('t')
x,y=ans[0][0].rhs,ans[0][1].rhs
#print(float(x.subs(t,1)))



fig,ax=plt.subplots()
#ax.set_aspect('equal')
ax.grid()

xlist=[]
ylist=[]
ims=[]
for i in np.linspace(0,5,500):
    xx=x.subs(t,i)
    yy=y.subs(t,i)
    xlist.append(xx)
    ylist.append(yy)
    im=ax.plot(xx,yy,'o',xlist,ylist,'--',color='r')
    ims.append(im)

ani=animation.ArtistAnimation(fig,ims)

plt.show()