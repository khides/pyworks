
import sympy
sympy.init_printing()

from matplotlib import pyplot as plt
from matplotlib import patches as pat

def distance(x1,y1,x2,y2):
    d=(x1-x2)**2+(y1-y2)**2
    return sympy.sqrt(d)


def circum_circle_area(x1,y1,x2,y2,x3,y3):
    x=sympy.Symbol('x')
    y=sympy.Symbol('y')
    eq1=(x1-x)**2+(y1-y)**2-(x2-x)**2-(y2-y)**2
    eq2=(x1-x)**2+(y1-y)**2-(x3-x)**2-(y3-y)**2
    ans=sympy.solve([eq1,eq2])
    
    x,y=ans[x],ans[y]
    r=distance(x,y,x1,y1)
    s=sympy.pi*r**2

    ans_dict={'面積':s,'外心':(x,y),'半径':r}
    return ans_dict


x1,y1=0,0
x2,y2=1,1
x3,y3=2,0
ans=circum_circle_area(x1,y1,x2,y2,x3,y3)
print(ans)

fig,ax=plt.subplots()

ax.scatter([x1,x2,x3],[y1,y2,y3],marker='x',color='r')
p=pat.Polygon(xy=[(x1,y1),(x2,y2),(x3,y3)],fill=False,color='r')
c=pat.Circle(xy=ans['外心'],radius=ans['半径'],fill=False,color='b')
ax.add_patch(c)
ax.add_patch(p)
ax.grid()
ax.set_aspect('equal')
plt.show()




def inscribed_circle_area(x1,y1,x2,y2,x3,y3):
    d1=distance(x2,y2,x3,y3)
    d2=distance(x1,y1,x3,y3)
    d3=distance(x1,y1,x2,y2)
    Stri=abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2

    x=(d1*x1+d2*x2+d3*x3)/(d1+d2+d3)
    y=(d1*y1+d2*y2+d3*y3)/(d1+d2+d3)

    r=Stri*2/(d1+d2+d3)
    s=sympy.pi*r**2

    ans_dict={'面積':s,'内心':[x,y],'半径':r}
    return ans_dict

x1,y1=0,0
x2,y2=12,9
x3,y3=0,25
ans=inscribed_circle_area(x1,y1,x2,y2,x3,y3)
print(ans)

fig,ax=plt.subplots()

ax.scatter([x1,x2,x3],[y1,y2,y3],marker='x',color='r')
p=pat.Polygon(xy=[(x1,y1),(x2,y2),(x3,y3)],fill=False,color='r')
c=pat.Circle(xy=ans['内心'],radius=ans['半径'],fill=False,color='blue')
ax.add_patch(c)
ax.add_patch(p)
ax.set_aspect('equal')
ax.grid()
plt.show()